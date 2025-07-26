#!/usr/bin/env python3
"""
Claude CLI - A command-line interface for interacting with Claude AI
Supports both API access and Claude Pro features where possible
"""

import sys
import os
import json
from pathlib import Path
import configparser
from .client import ClaudeClient

class ClaudeCLI:
    def __init__(self):
        self.config_dir = Path.home() / '.claude'
        self.config_file = self.config_dir / 'config.ini'
        self.api_key = None
        
        # Available Claude models
        self.available_models = {
            'claude-3-5-sonnet-20241022': 'Claude 3.5 Sonnet (Latest)',
            'claude-3-sonnet-20240229': 'Claude 3 Sonnet',
            'claude-3-opus-20240229': 'Claude 3 Opus (Most Capable)',
            'claude-3-haiku-20240307': 'Claude 3 Haiku (Fastest)',
            'claude-2.1': 'Claude 2.1 (Legacy)'
        }
        
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
            'subscription_type': 'api'  # api, pro, team, or enterprise
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

    def setup_api_key(self, api_key):
        """Setup API key in config file"""
        config = configparser.ConfigParser()
        config.read(self.config_file)
        config.set('DEFAULT', 'api_key', api_key)
        
        with open(self.config_file, 'w') as f:
            config.write(f)
        
        self.api_key = api_key
        self.client.api_key = api_key
        print("API key saved successfully!")

    def chat(self, message, system_prompt=None, model=None):
        """Send a message to Claude and get response"""
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

        messages = [{"role": "user", "content": message}]
        
        # Use provided model or default
        current_model = model or self.model
        
        return self.client.send_message(
            model=current_model,
            max_tokens=self.max_tokens,
            messages=messages,
            temperature=self.temperature,
            system_prompt=system_prompt
# Use provided model or default
        current_model = model or self.model
        
        try:
            return self.client.send_message(
                model=current_model,
                max_tokens=self.max_tokens,
                messages=messages,
                temperature=self.temperature,
                system_prompt=system_prompt
            )
        except Exception as e:
            print(f"Error occurred while sending message: {str(e)}")
            return None

    def show_subscription_info(self):
        """Show information about Claude subscription types"""

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

if __name__ == '__main__':
    from .cli import main
    main()