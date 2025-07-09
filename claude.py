#!/usr/bin/env python3
"""
Claude CLI - A command-line interface for interacting with Claude AI
Supports both API access and Claude Pro features where possible
"""

import sys
import os
import argparse
import json
import requests
from pathlib import Path
import configparser
from typing import List, Dict
from claude_memory import ClaudeMemory
from claude_webhooks import ClaudeWebhookServer
from claude_mcp_services import mcp_manager
from claude_automation_platform import get_automation_platform, AutomationTask, WorkflowDefinition

class ClaudeCLI:
    def __init__(self):
        self.config_dir = Path.home() / '.claude'
        self.config_file = self.config_dir / 'config.ini'
        self.api_key = None
        self.api_url = "https://api.anthropic.com/v1/messages"
        
        # Available Claude models
        self.available_models = {
            'claude-3-5-sonnet-20241022': 'Claude 3.5 Sonnet (Latest)',
            'claude-3-sonnet-20240229': 'Claude 3 Sonnet',
            'claude-3-opus-20240229': 'Claude 3 Opus (Most Capable)',
            'claude-3-haiku-20240307': 'Claude 3 Haiku (Fastest)',
            'claude-2.1': 'Claude 2.1 (Legacy)'
        }
        
        # Initialize memory system
        self.memory = ClaudeMemory()
        self.use_memory = True
        
        # Initialize webhook server
        self.webhook_server = None
        self.webhook_enabled = False
        
        # Initialize MCP services
        self.mcp_services = mcp_manager
        
        # Initialize automation platform
        self.automation_platform = get_automation_platform(self)
        
        self.setup_config()

    def setup_config(self):
        """Setup configuration directory and file"""
        self.config_dir.mkdir(exist_ok=True)
        
        if not self.config_file.exists():
            self.create_default_config()
        
        self.load_config()

    def create_default_config(self):
        """Create default configuration file"""
        config = configparser.ConfigParser()
        config['DEFAULT'] = {
            'api_key': '',
            'model': 'claude-3-5-sonnet-20241022',
            'max_tokens': '1000',
            'temperature': '0.7',
            'subscription_type': 'api',  # api, pro, team, or enterprise
            'use_memory': 'true',
            'memory_user_id': 'default_user',
            'webhook_enabled': 'false',
            'webhook_host': 'localhost',
            'webhook_port': '8080'
        }
        
        config['PRO_FEATURES'] = {
            'priority_bandwidth': 'false',
            'early_access': 'false',
            'usage_5x_limit': 'false'
        }
        
        with open(self.config_file, 'w') as f:
            config.write(f)
        
        print(f"Created config file at {self.config_file}")
        print("\n🔑 CLAUDE ACCESS SETUP:")
        print("=" * 50)
        print("Claude offers different access methods:")
        print("1. API Access (Pay-per-use) - For developers")
        print("2. Claude Pro ($20/month) - Web interface + priority")
        print("3. Claude Team ($25/user/month) - Team collaboration")
        print("4. Claude Enterprise - Custom pricing")
        print("\n📝 IMPORTANT NOTES:")
        print("• Claude Pro subscription ≠ API access")
        print("• Squad & Code features are Pro/Team web features")
        print("• This CLI uses API access (separate billing)")
        print("\nGet your API key: https://console.anthropic.com/")

    def load_config(self):
        """Load configuration from file"""
        config = configparser.ConfigParser()
        config.read(self.config_file)
        
        # Try to get API key from config file or environment variable
        self.api_key = (
            os.getenv('ANTHROPIC_API_KEY') or 
            config.get('DEFAULT', 'api_key', fallback='')
        )
        
        self.model = config.get('DEFAULT', 'model', fallback='claude-3-5-sonnet-20241022')
        self.max_tokens = config.getint('DEFAULT', 'max_tokens', fallback=1000)
        self.temperature = config.getfloat('DEFAULT', 'temperature', fallback=0.7)
        self.subscription_type = config.get('DEFAULT', 'subscription_type', fallback='api')
        self.use_memory = config.getboolean('DEFAULT', 'use_memory', fallback=True)
        memory_user_id = config.get('DEFAULT', 'memory_user_id', fallback='default_user')
        
        # Initialize memory with user ID
        if self.use_memory:
            self.memory = ClaudeMemory(memory_user_id)
        
        # Initialize webhook settings
        self.webhook_enabled = config.getboolean('DEFAULT', 'webhook_enabled', fallback=False)
        self.webhook_host = config.get('DEFAULT', 'webhook_host', fallback='localhost')
        self.webhook_port = config.getint('DEFAULT', 'webhook_port', fallback=8080)

    def setup_api_key(self, api_key):
        """Setup API key in config file"""
        config = configparser.ConfigParser()
        config.read(self.config_file)
        config.set('DEFAULT', 'api_key', api_key)
        
        with open(self.config_file, 'w') as f:
            config.write(f)
        
        self.api_key = api_key
        print("API key saved successfully!")
    
    def start_webhook_server(self):
        """Start the webhook server for n8n integration"""
        if self.webhook_server and self.webhook_server.is_running():
            print("🌐 Webhook server is already running")
            return True
        
        try:
            self.webhook_server = ClaudeWebhookServer(
                claude_instance=self,
                host=self.webhook_host,
                port=self.webhook_port
            )
            
            if self.webhook_server.start():
                self.webhook_enabled = True
                print("✅ Webhook server started successfully")
                return True
            else:
                print("❌ Failed to start webhook server")
                return False
                
        except Exception as e:
            print(f"❌ Error starting webhook server: {e}")
            return False
    
    def stop_webhook_server(self):
        """Stop the webhook server"""
        if self.webhook_server and self.webhook_server.is_running():
            self.webhook_server.stop()
            self.webhook_enabled = False
            print("🛑 Webhook server stopped")
            return True
        else:
            print("🌐 Webhook server is not running")
            return False
    
    def get_webhook_status(self):
        """Get webhook server status"""
        if self.webhook_server and self.webhook_server.is_running():
            return {
                "status": "running",
                "host": self.webhook_host,
                "port": self.webhook_port,
                "endpoints": [
                    f"http://{self.webhook_host}:{self.webhook_port}/chat",
                    f"http://{self.webhook_host}:{self.webhook_port}/status",
                    f"http://{self.webhook_host}:{self.webhook_port}/memory/stats",
                    f"http://{self.webhook_host}:{self.webhook_port}/memory/clear",
                    f"http://{self.webhook_host}:{self.webhook_port}/memory/recall"
                ]
            }
        else:
            return {
                "status": "stopped",
                "host": self.webhook_host,
                "port": self.webhook_port
            }
    
    def get_mcp_services_status(self):
        """Get status of all MCP services"""
        return self.mcp_services.get_service_status()
    
    def execute_desktop_command(self, command: str, args: List[str] = None):
        """Execute desktop command via MCP"""
        desktop_service = self.mcp_services.get_service('desktop_commander')
        if desktop_service:
            return desktop_service.execute_command(command, args)
        return None
    
    def use_toolbox_tool(self, tool_name: str, parameters: Dict = None):
        """Use a toolbox tool via MCP"""
        toolbox_service = self.mcp_services.get_service('toolbox')
        if toolbox_service:
            return toolbox_service.execute_tool(tool_name, parameters)
        return None
    
    def manage_context(self, action: str, name: str = None, content: str = None, query: str = None):
        """Manage contexts via Context7 MCP"""
        context_service = self.mcp_services.get_service('context7')
        if not context_service:
            return None
        
        if action == 'create' and name and content:
            return context_service.create_context(name, content)
        elif action == 'get' and name:
            return context_service.get_context(name)
        elif action == 'search' and query:
            return context_service.search_contexts(query)
        elif action == 'list':
            return context_service.list_contexts()
        elif action == 'delete' and name:
            return context_service.delete_context(name)
        
        return None
    
    def create_workflow(self, name: str, description: str) -> str:
        """Create a new automation workflow"""
        return self.automation_platform.create_composite_workflow(name, description)
    
    def add_workflow_task(self, workflow_id: str, task_type: str, task_name: str, parameters: Dict) -> bool:
        """Add a task to a workflow"""
        import time
        task_id = f"task_{int(time.time())}"
        task = AutomationTask(
            id=task_id,
            name=task_name,
            type=task_type,
            parameters=parameters
        )
        return self.automation_platform.add_task_to_workflow(workflow_id, task)
    
    def execute_workflow(self, workflow_id: str, context: Dict = None) -> Dict:
        """Execute an automation workflow"""
        return self.automation_platform.execute_workflow(workflow_id, context)
    
    def list_workflows(self) -> List[Dict]:
        """List all automation workflows"""
        return self.automation_platform.list_workflows()
    
    def get_workflow_status(self, workflow_id: str) -> Dict:
        """Get workflow status"""
        return self.automation_platform.get_workflow_status(workflow_id)
    
    def get_shared_memory(self) -> Dict:
        """Get automation platform shared memory"""
        return self.automation_platform.get_shared_memory()
    
    def update_shared_memory(self, updates: Dict) -> None:
        """Update automation platform shared memory"""
        self.automation_platform.update_shared_memory(updates)
    
    def create_quick_workflow(self, name: str, tasks: List[Dict]) -> str:
        """Create and execute a quick workflow"""
        workflow_id = self.create_workflow(name, f"Quick workflow: {name}")
        
        for i, task_def in enumerate(tasks):
            task_name = task_def.get('name', f"Task {i+1}")
            task_type = task_def.get('type', 'claude')
            parameters = task_def.get('parameters', {})
            
            self.add_workflow_task(workflow_id, task_type, task_name, parameters)
        
        return workflow_id

    def chat(self, message, system_prompt=None, model=None, save_to_memory=True):
        """Send a message to Claude and get response with memory integration"""
        if not self.api_key:
            print("Error: No API key found. Please set up your API key first.")
            print("\n🔑 TWO WAYS TO GET CLAUDE ACCESS:")
            print("=" * 40)
            print("1. API Access (for this CLI):")
            print("   • Get API key: https://console.anthropic.com/")
            print("   • Use: claude --setup-key YOUR_API_KEY")
            print("   • Or: export ANTHROPIC_API_KEY=your_key")
            print("\n2. Claude Pro Subscription ($20/month):")
            print("   • Access at: https://claude.ai/")
            print("   • Includes Squad, Code, priority access")
            print("   • Note: Separate from API access")
            return None

        # Get memory context if enabled
        enhanced_message = message
        if self.use_memory and hasattr(self, 'memory'):
            memory_context = self.memory.get_conversation_context(message)
            if memory_context:
                enhanced_message = f"{memory_context}\n\nCurrent message: {message}"

        headers = {
            'Content-Type': 'application/json',
            'x-api-key': self.api_key,
            'anthropic-version': '2023-06-01'
        }

        messages = [{"role": "user", "content": enhanced_message}]
        
        # Use provided model or default
        current_model = model or self.model
        
        data = {
            'model': current_model,
            'max_tokens': self.max_tokens,
            'messages': messages,
            'temperature': self.temperature
        }
        
        if system_prompt:
            data['system'] = system_prompt

        try:
            response = requests.post(self.api_url, headers=headers, json=data)
            response.raise_for_status()
            
            result = response.json()
            claude_response = result['content'][0]['text']
            
            # Save conversation to memory if enabled
            if self.use_memory and hasattr(self, 'memory') and save_to_memory:
                conversation = [
                    {"role": "user", "content": message},
                    {"role": "assistant", "content": claude_response}
                ]
                self.memory.save_conversation(conversation, context=system_prompt or "")
            
            return claude_response
            
        except requests.exceptions.RequestException as e:
            if "unauthorized" in str(e).lower():
                print("❌ API key invalid or expired. Get a new one at: https://console.anthropic.com/")
            elif "rate_limit" in str(e).lower():
                print("⏰ Rate limit reached. Consider upgrading your API plan.")
            else:
                print(f"Error making request: {e}")
            return None
        except KeyError as e:
            print(f"Error parsing response: {e}")
            print(f"Response: {response.text}")
            return None

    def show_subscription_info(self):
        """Show information about Claude subscription types"""
        print("\n🎯 CLAUDE ACCESS OPTIONS:")
        print("=" * 50)
        print("1. 📱 Claude Free")
        print("   • Free access to Claude via web")
        print("   • Limited usage per day")
        print("   • Basic model access")
        
        print("\n2. 🚀 Claude Pro ($20/month)")
        print("   • 5x more usage than free")
        print("   • Priority bandwidth (faster responses)")
        print("   • Early access to new features")
        print("   • Claude Squad (team collaboration)")
        print("   • Claude Code (coding assistant)")
        print("   • Access via: https://claude.ai/")
        
        print("\n3. 👥 Claude Team ($25/user/month)")
        print("   • Everything in Pro")
        print("   • Team workspace & collaboration")
        print("   • Admin console & billing")
        print("   • Priority support")
        
        print("\n4. 🏢 Claude Enterprise")
        print("   • Custom pricing & features")
        print("   • SSO & advanced security")
        print("   • Dedicated support")
        print("   • Custom model training")
        
        print("\n5. 🔧 API Access (Pay-per-use)")
        print("   • For developers & integrations")
        print("   • This CLI uses API access")
        print("   • Separate from web subscriptions")
        print("   • Get key: https://console.anthropic.com/")

    def show_models(self):
        """Show available Claude models"""
        print("\n🤖 AVAILABLE CLAUDE MODELS:")
        print("=" * 50)
        for model_id, description in self.available_models.items():
            current = " (CURRENT)" if model_id == self.model else ""
            print(f"• {model_id}: {description}{current}")
        
        print(f"\n📊 Current Config:")
        print(f"• Model: {self.model}")
        print(f"• Max Tokens: {self.max_tokens}")
        print(f"• Temperature: {self.temperature}")
        print(f"• Subscription Type: {self.subscription_type}")

    def simulate_squad_features(self):
        """Simulate Claude Squad-like features for team collaboration"""
        print("\n👥 CLAUDE SQUAD SIMULATOR:")
        print("=" * 40)
        print("Note: This simulates Squad features using API access")
        print("For real Squad features, get Claude Pro at https://claude.ai/")
        print("\nSquad Features:")
        print("• Team project collaboration")
        print("• Shared conversation history")
        print("• Multiple AI personas")
        print("• Document analysis & synthesis")
        
        return self.interactive_mode_enhanced()

    def simulate_code_features(self):
        """Simulate Claude Code-like features for coding assistance"""
        print("\n💻 CLAUDE CODE SIMULATOR:")
        print("=" * 40)
        print("Note: This simulates Code features using API access")
        print("For real Code features, get Claude Pro at https://claude.ai/")
        
        # Set coding-optimized model and system prompt
        coding_prompt = """You are Claude Code, an expert programming assistant. You excel at:
- Writing clean, efficient code
- Debugging and troubleshooting
- Code review and optimization
- Explaining complex programming concepts
- Supporting multiple programming languages
- Following best practices and conventions

Always provide practical, working code examples when appropriate."""
        
        return self.interactive_mode_enhanced(system_prompt=coding_prompt)

    def interactive_mode_enhanced(self, system_prompt=None):
        """Enhanced interactive chat mode with special features"""
        mode_name = "Squad" if "team" in str(system_prompt).lower() else "Code" if system_prompt else "Standard"
        print(f"\nClaude CLI - {mode_name} Mode")
        print("Commands: 'exit'/'quit' to leave, 'clear' to clear screen")
        print("         'model <name>' to switch models, 'help' for commands")
        print("-" * 50)
        
        conversation_history = []
        
        while True:
            try:
                user_input = input(f"\n[{mode_name}] You: ").strip()
                
                if user_input.lower() in ['exit', 'quit']:
                    print("Goodbye!")
                    break
                
                if user_input.lower() == 'clear':
                    os.system('clear' if os.name == 'posix' else 'cls')
                    conversation_history = []
                    continue
                
                if user_input.lower() == 'help':
                    print("\nAvailable commands:")
                    print("• exit/quit - Leave the chat")
                    print("• clear - Clear screen and history")
                    print("• model <name> - Switch Claude model")
                    print("• models - Show available models")
                    print("• info - Show subscription information")
                    print("• memory stats - Show memory usage statistics")
                    print("• memory clear - Clear all memories")
                    print("• memory toggle - Toggle memory on/off")
                    print("• memory recall <query> - Search memories")
                    print("• webhook start - Start webhook server for n8n")
                    print("• webhook stop - Stop webhook server")
                    print("• webhook status - Show webhook status")
                    print("• mcp status - Show MCP services status")
                    print("• mcp desktop <command> - Execute desktop command")
                    print("• mcp toolbox <tool> - Use toolbox tool")
                    print("• mcp context <action> - Manage contexts")
                    print("• workflow list - List all workflows")
                    print("• workflow create <name> - Create new workflow")
                    print("• workflow execute <id> - Execute workflow")
                    print("• workflow status <id> - Get workflow status")
                    print("• memory shared - Show shared automation memory")
                    continue
                
                if user_input.lower() == 'models':
                    self.show_models()
                    continue
                
                if user_input.lower() == 'info':
                    self.show_subscription_info()
                    continue
                
                if user_input.lower().startswith('model '):
                    new_model = user_input[6:].strip()
                    if new_model in self.available_models:
                        self.model = new_model
                        print(f"✅ Switched to: {self.available_models[new_model]}")
                    else:
                        print(f"❌ Unknown model. Available models:")
                        for model_id in self.available_models:
                            print(f"   • {model_id}")
                    continue
                
                # Memory management commands
                if user_input.lower().startswith('memory '):
                    memory_cmd = user_input[7:].strip().lower()
                    
                    if memory_cmd == 'stats':
                        if hasattr(self, 'memory'):
                            stats = self.memory.get_memory_stats()
                            print(f"\n🧠 Memory Statistics:")
                            print(f"• Total memories: {stats.get('total_memories', 0)}")
                            print(f"• Conversations: {stats.get('conversations', 0)}")
                            print(f"• Last updated: {stats.get('last_updated', 'Never')}")
                            print(f"• User ID: {stats.get('user_id', 'Unknown')}")
                            print(f"• Memory enabled: {self.use_memory}")
                        else:
                            print("❌ Memory system not available")
                    
                    elif memory_cmd == 'clear':
                        if hasattr(self, 'memory'):
                            if self.memory.clear_memories():
                                print("✅ All memories cleared")
                            else:
                                print("❌ Failed to clear memories")
                        else:
                            print("❌ Memory system not available")
                    
                    elif memory_cmd == 'toggle':
                        self.use_memory = not self.use_memory
                        status = "enabled" if self.use_memory else "disabled"
                        print(f"🧠 Memory {status}")
                    
                    elif memory_cmd.startswith('recall '):
                        query = memory_cmd[7:].strip()
                        if hasattr(self, 'memory') and query:
                            memories = self.memory.recall_memories(query)
                            if memories:
                                print(f"\n🔍 Found {len(memories)} relevant memories:")
                                for i, memory in enumerate(memories, 1):
                                    print(f"{i}. {memory.get('content', 'No content')}")
                                    print(f"   Relevance: {memory.get('relevance', 0):.2f}")
                            else:
                                print("No relevant memories found")
                        else:
                            print("❌ Please provide a search query")
                    
                    else:
                        print("❌ Unknown memory command. Use: stats, clear, toggle, or recall <query>")
                    
                    continue
                
                # Webhook management commands
                if user_input.lower().startswith('webhook '):
                    webhook_cmd = user_input[8:].strip().lower()
                    
                    if webhook_cmd == 'start':
                        self.start_webhook_server()
                    
                    elif webhook_cmd == 'stop':
                        self.stop_webhook_server()
                    
                    elif webhook_cmd == 'status':
                        status = self.get_webhook_status()
                        print(f"\n🌐 Webhook Server Status:")
                        print(f"• Status: {status['status']}")
                        print(f"• Host: {status['host']}")
                        print(f"• Port: {status['port']}")
                        if status['status'] == 'running':
                            print(f"• Available endpoints:")
                            for endpoint in status['endpoints']:
                                print(f"  - {endpoint}")
                    
                    else:
                        print("❌ Unknown webhook command. Use: start, stop, or status")
                    
                    continue
                
                # MCP services commands
                if user_input.lower().startswith('mcp '):
                    mcp_cmd = user_input[4:].strip()
                    
                    if mcp_cmd == 'status':
                        status = self.get_mcp_services_status()
                        print(f"\n🔧 MCP Services Status:")
                        for service_name, service_status in status.items():
                            available = "✅" if service_status['available'] else "❌"
                            configured = "✅" if service_status['configured'] else "❌"
                            print(f"• {service_name}:")
                            print(f"  - Available: {available}")
                            print(f"  - Configured: {configured}")
                            print(f"  - Description: {service_status['description']}")
                    
                    elif mcp_cmd.startswith('desktop '):
                        command = mcp_cmd[8:].strip()
                        if command:
                            result = self.execute_desktop_command(command)
                            if result:
                                print(f"✅ Desktop command executed: {result.get('result', 'Success')}")
                            else:
                                print("❌ Failed to execute desktop command")
                        else:
                            print("❌ Please provide a command to execute")
                    
                    elif mcp_cmd.startswith('toolbox '):
                        tool_spec = mcp_cmd[8:].strip()
                        if tool_spec:
                            # Parse tool name and parameters
                            parts = tool_spec.split(' ', 1)
                            tool_name = parts[0]
                            params = {}
                            if len(parts) > 1:
                                try:
                                    params = json.loads(parts[1])
                                except:
                                    params = {"input": parts[1]}
                            
                            result = self.use_toolbox_tool(tool_name, params)
                            if result:
                                print(f"✅ Toolbox tool executed: {result.get('result', 'Success')}")
                            else:
                                print("❌ Failed to execute toolbox tool")
                        else:
                            print("❌ Please provide a tool name")
                    
                    elif mcp_cmd.startswith('context '):
                        context_spec = mcp_cmd[8:].strip()
                        parts = context_spec.split(' ', 2)
                        
                        if len(parts) >= 1:
                            action = parts[0]
                            
                            if action == 'list':
                                result = self.manage_context('list')
                                if result:
                                    print("📋 Available contexts:")
                                    contexts = result.get('result', [])
                                    for ctx in contexts:
                                        print(f"  • {ctx}")
                                else:
                                    print("❌ Failed to list contexts")
                            
                            elif action == 'search' and len(parts) >= 2:
                                query = ' '.join(parts[1:])
                                result = self.manage_context('search', query=query)
                                if result:
                                    print(f"🔍 Search results for '{query}':")
                                    results = result.get('result', [])
                                    for res in results:
                                        print(f"  • {res}")
                                else:
                                    print("❌ Failed to search contexts")
                            
                            elif action == 'get' and len(parts) >= 2:
                                name = parts[1]
                                result = self.manage_context('get', name=name)
                                if result:
                                    print(f"📄 Context '{name}':")
                                    print(result.get('result', 'No content'))
                                else:
                                    print(f"❌ Failed to get context '{name}'")
                            
                            else:
                                print("❌ Context commands: list, search <query>, get <name>")
                        else:
                            print("❌ Please provide a context action")
                    
                    else:
                        print("❌ Unknown MCP command. Use: status, desktop <cmd>, toolbox <tool>, context <action>")
                    
                    continue
                
                # Workflow management commands
                if user_input.lower().startswith('workflow '):
                    workflow_cmd = user_input[9:].strip()
                    
                    if workflow_cmd == 'list':
                        workflows = self.list_workflows()
                        if workflows:
                            print(f"\n🔄 Available Workflows:")
                            for wf in workflows:
                                status = "✅ Enabled" if wf['enabled'] else "❌ Disabled"
                                print(f"• {wf['id']}: {wf['name']} ({wf['task_count']} tasks) - {status}")
                                print(f"  Description: {wf['description']}")
                        else:
                            print("No workflows found")
                    
                    elif workflow_cmd.startswith('create '):
                        name = workflow_cmd[7:].strip()
                        if name:
                            workflow_id = self.create_workflow(name, f"Interactive workflow: {name}")
                            print(f"✅ Created workflow: {workflow_id}")
                        else:
                            print("❌ Please provide a workflow name")
                    
                    elif workflow_cmd.startswith('execute '):
                        workflow_id = workflow_cmd[8:].strip()
                        if workflow_id:
                            print(f"🔄 Executing workflow: {workflow_id}")
                            result = self.execute_workflow(workflow_id)
                            if result.get('status') == 'completed':
                                print(f"✅ Workflow completed in {result.get('duration', 0):.2f}s")
                                print(f"Results: {len(result.get('results', {}))} tasks executed")
                            else:
                                print(f"❌ Workflow failed: {result.get('error', 'Unknown error')}")
                        else:
                            print("❌ Please provide a workflow ID")
                    
                    elif workflow_cmd.startswith('status '):
                        workflow_id = workflow_cmd[7:].strip()
                        if workflow_id:
                            status = self.get_workflow_status(workflow_id)
                            if 'error' not in status:
                                print(f"\n📊 Workflow Status: {status['name']}")
                                print(f"• ID: {status['id']}")
                                print(f"• Description: {status['description']}")
                                print(f"• Enabled: {status['enabled']}")
                                print(f"• Tasks: {status['task_count']}")
                                if status['tasks']:
                                    print("• Task Details:")
                                    for task in status['tasks']:
                                        print(f"  - {task['name']} ({task['type']}) - {task['status']}")
                            else:
                                print(f"❌ {status['error']}")
                        else:
                            print("❌ Please provide a workflow ID")
                    
                    else:
                        print("❌ Unknown workflow command. Use: list, create <name>, execute <id>, status <id>")
                    
                    continue
                
                # Shared memory commands
                if user_input.lower().startswith('memory '):
                    memory_cmd = user_input[7:].strip().lower()
                    
                    if memory_cmd == 'shared':
                        shared_mem = self.get_shared_memory()
                        if shared_mem:
                            print(f"\n🧠 Shared Automation Memory:")
                            for key, value in shared_mem.items():
                                print(f"• {key}: {str(value)[:100]}{'...' if len(str(value)) > 100 else ''}")
                        else:
                            print("Shared memory is empty")
                        continue
                
                if not user_input:
                    continue
                
                # Display model info safely
                model_parts = self.model.split('-')
                if len(model_parts) >= 3:
                    model_display = f"{model_parts[1]} {model_parts[2]}"
                else:
                    model_display = self.model
                print(f"Claude ({model_display}): ", end="", flush=True)
                
                # Add conversation context for better responses
                context_message = user_input
                if conversation_history:
                    context_message = f"Previous context: {conversation_history[-2:]}\n\nCurrent question: {user_input}"
                
                response = self.chat(context_message, system_prompt)
                
                if response:
                    print(response)
                    conversation_history.append(f"User: {user_input}")
                    conversation_history.append(f"Claude: {response}")
                    # Keep only last 10 exchanges
                    if len(conversation_history) > 20:
                        conversation_history = conversation_history[-20:]
                else:
                    print("Sorry, I couldn't process your request.")
                    
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except EOFError:
                print("\nGoodbye!")
                break

    def interactive_mode(self):
        """Start interactive chat mode"""
        return self.interactive_mode_enhanced()

def main():
    parser = argparse.ArgumentParser(
        description='Claude CLI - Interact with Claude AI from the command line',
        epilog="""
Examples:
  claude "Hello Claude!"                    # Quick question
  claude -i                                # Interactive mode  
  claude --squad                           # Squad simulation mode
  claude --code                            # Code assistant mode
  claude -m claude-3-opus-20240229 "Help"  # Use specific model
  claude --info                            # Show subscription info
        """,
        formatter_class=argparse.RawDescriptionHelpFormatter
    )
    
    parser.add_argument('message', nargs='*', help='Message to send to Claude')
    parser.add_argument('-i', '--interactive', action='store_true', help='Start interactive mode')
    parser.add_argument('-s', '--system', help='System prompt for the conversation')
    parser.add_argument('-m', '--model', help='Claude model to use')
    parser.add_argument('--setup-key', help='Setup API key')
    parser.add_argument('--config', action='store_true', help='Show config file location')
    parser.add_argument('--models', action='store_true', help='Show available models')
    parser.add_argument('--info', action='store_true', help='Show Claude subscription information')
    parser.add_argument('--squad', action='store_true', help='Start Claude Squad simulation mode')
    parser.add_argument('--code', action='store_true', help='Start Claude Code simulation mode')
    parser.add_argument('--memory-stats', action='store_true', help='Show memory usage statistics')
    parser.add_argument('--memory-clear', action='store_true', help='Clear all memories')
    parser.add_argument('--memory-recall', help='Search and recall memories by query')
    parser.add_argument('--webhook-start', action='store_true', help='Start webhook server for n8n integration')
    parser.add_argument('--webhook-stop', action='store_true', help='Stop webhook server')
    parser.add_argument('--webhook-status', action='store_true', help='Show webhook server status')
    parser.add_argument('--mcp-status', action='store_true', help='Show MCP services status')
    parser.add_argument('--mcp-desktop', help='Execute desktop command via MCP')
    parser.add_argument('--mcp-toolbox', help='Use toolbox tool via MCP')
    parser.add_argument('--mcp-context', nargs='+', help='Manage contexts via MCP (action [args])')
    parser.add_argument('--workflow-list', action='store_true', help='List all automation workflows')
    parser.add_argument('--workflow-create', nargs=2, metavar=('NAME', 'DESCRIPTION'), help='Create new workflow')
    parser.add_argument('--workflow-execute', help='Execute workflow by ID')
    parser.add_argument('--workflow-status', help='Get workflow status by ID')
    parser.add_argument('--automation-memory', action='store_true', help='Show shared automation memory')
    
    args = parser.parse_args()
    
    claude = ClaudeCLI()
    
    if args.setup_key:
        claude.setup_api_key(args.setup_key)
        return
    
    if args.config:
        print(f"📂 Config file location: {claude.config_file}")
        print(f"📊 Current model: {claude.model}")
        print(f"🔑 API key configured: {'Yes' if claude.api_key else 'No'}")
        return
    
    if args.models:
        claude.show_models()
        return
    
    if args.info:
        claude.show_subscription_info()
        return
    
    if args.squad:
        claude.simulate_squad_features()
        return
    
    if args.code:
        claude.simulate_code_features()
        return
    
    if args.memory_stats:
        if hasattr(claude, 'memory'):
            stats = claude.memory.get_memory_stats()
            print(f"\n🧠 Memory Statistics:")
            print(f"• Total memories: {stats.get('total_memories', 0)}")
            print(f"• Conversations: {stats.get('conversations', 0)}")
            print(f"• Last updated: {stats.get('last_updated', 'Never')}")
            print(f"• User ID: {stats.get('user_id', 'Unknown')}")
            print(f"• Memory enabled: {claude.use_memory}")
        else:
            print("❌ Memory system not available")
        return
    
    if args.memory_clear:
        if hasattr(claude, 'memory'):
            if claude.memory.clear_memories():
                print("✅ All memories cleared")
            else:
                print("❌ Failed to clear memories")
        else:
            print("❌ Memory system not available")
        return
    
    if args.memory_recall:
        if hasattr(claude, 'memory'):
            memories = claude.memory.recall_memories(args.memory_recall)
            if memories:
                print(f"\n🔍 Found {len(memories)} relevant memories:")
                for i, memory in enumerate(memories, 1):
                    print(f"{i}. {memory.get('content', 'No content')}")
                    print(f"   Relevance: {memory.get('relevance', 0):.2f}")
            else:
                print("No relevant memories found")
        else:
            print("❌ Memory system not available")
        return
    
    if args.webhook_start:
        claude.start_webhook_server()
        return
    
    if args.webhook_stop:
        claude.stop_webhook_server()
        return
    
    if args.webhook_status:
        status = claude.get_webhook_status()
        print(f"\n🌐 Webhook Server Status:")
        print(f"• Status: {status['status']}")
        print(f"• Host: {status['host']}")
        print(f"• Port: {status['port']}")
        if status['status'] == 'running':
            print(f"• Available endpoints:")
            for endpoint in status['endpoints']:
                print(f"  - {endpoint}")
        return
    
    if args.mcp_status:
        status = claude.get_mcp_services_status()
        print(f"\n🔧 MCP Services Status:")
        for service_name, service_status in status.items():
            available = "✅" if service_status['available'] else "❌"
            configured = "✅" if service_status['configured'] else "❌"
            print(f"• {service_name}:")
            print(f"  - Available: {available}")
            print(f"  - Configured: {configured}")
            print(f"  - Description: {service_status['description']}")
        return
    
    if args.mcp_desktop:
        result = claude.execute_desktop_command(args.mcp_desktop)
        if result:
            print(f"✅ Desktop command executed: {result.get('result', 'Success')}")
        else:
            print("❌ Failed to execute desktop command")
        return
    
    if args.mcp_toolbox:
        result = claude.use_toolbox_tool(args.mcp_toolbox)
        if result:
            print(f"✅ Toolbox tool executed: {result.get('result', 'Success')}")
        else:
            print("❌ Failed to execute toolbox tool")
        return
    
    if args.mcp_context:
        if len(args.mcp_context) >= 1:
            action = args.mcp_context[0]
            
            if action == 'list':
                result = claude.manage_context('list')
                if result:
                    print("📋 Available contexts:")
                    contexts = result.get('result', [])
                    for ctx in contexts:
                        print(f"  • {ctx}")
                else:
                    print("❌ Failed to list contexts")
            
            elif action == 'search' and len(args.mcp_context) >= 2:
                query = ' '.join(args.mcp_context[1:])
                result = claude.manage_context('search', query=query)
                if result:
                    print(f"🔍 Search results for '{query}':")
                    results = result.get('result', [])
                    for res in results:
                        print(f"  • {res}")
                else:
                    print("❌ Failed to search contexts")
            
            elif action == 'get' and len(args.mcp_context) >= 2:
                name = args.mcp_context[1]
                result = claude.manage_context('get', name=name)
                if result:
                    print(f"📄 Context '{name}':")
                    print(result.get('result', 'No content'))
                else:
                    print(f"❌ Failed to get context '{name}'")
            
            else:
                print("❌ Context commands: list, search <query>, get <name>")
        else:
            print("❌ Please provide a context action")
        return
    
    if args.workflow_list:
        workflows = claude.list_workflows()
        if workflows:
            print(f"\n🔄 Available Workflows:")
            for wf in workflows:
                status = "✅ Enabled" if wf['enabled'] else "❌ Disabled"
                print(f"• {wf['id']}: {wf['name']} ({wf['task_count']} tasks) - {status}")
                print(f"  Description: {wf['description']}")
        else:
            print("No workflows found")
        return
    
    if args.workflow_create:
        name, description = args.workflow_create
        workflow_id = claude.create_workflow(name, description)
        print(f"✅ Created workflow: {workflow_id}")
        return
    
    if args.workflow_execute:
        print(f"🔄 Executing workflow: {args.workflow_execute}")
        result = claude.execute_workflow(args.workflow_execute)
        if result.get('status') == 'completed':
            print(f"✅ Workflow completed in {result.get('duration', 0):.2f}s")
            print(f"Results: {len(result.get('results', {}))} tasks executed")
        else:
            print(f"❌ Workflow failed: {result.get('error', 'Unknown error')}")
        return
    
    if args.workflow_status:
        status = claude.get_workflow_status(args.workflow_status)
        if 'error' not in status:
            print(f"\n📊 Workflow Status: {status['name']}")
            print(f"• ID: {status['id']}")
            print(f"• Description: {status['description']}")
            print(f"• Enabled: {status['enabled']}")
            print(f"• Tasks: {status['task_count']}")
            if status['tasks']:
                print("• Task Details:")
                for task in status['tasks']:
                    print(f"  - {task['name']} ({task['type']}) - {task['status']}")
        else:
            print(f"❌ {status['error']}")
        return
    
    if args.automation_memory:
        shared_mem = claude.get_shared_memory()
        if shared_mem:
            print(f"\n🧠 Shared Automation Memory:")
            for key, value in shared_mem.items():
                print(f"• {key}: {str(value)[:100]}{'...' if len(str(value)) > 100 else ''}")
        else:
            print("Shared memory is empty")
        return
    
    if args.interactive:
        claude.interactive_mode()
        return
    
    if args.message:
        message = ' '.join(args.message)
        response = claude.chat(message, args.system, args.model)
        if response:
            print(response)
    else:
        # If no message provided, show help and start interactive mode
        print("🤖 Claude CLI - AI Assistant")
        print("=" * 30)
        print("💡 Tip: Run 'claude --info' to learn about Claude Pro features")
        print("🔧 Tip: Run 'claude --models' to see available models")
        print("👥 Tip: Run 'claude --squad' for team collaboration features")
        print("💻 Tip: Run 'claude --code' for coding assistance")
        print("\nStarting interactive mode...\n")
        claude.interactive_mode()

if __name__ == '__main__':
    main()