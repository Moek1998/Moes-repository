#!/usr/bin/env python3
"""
Claude Webhooks Module - n8n Integration for Claude CLI
Provides webhook endpoints for n8n workflow automation
"""

import json
import threading
import time
from http.server import HTTPServer, BaseHTTPRequestHandler
from urllib.parse import urlparse, parse_qs
from pathlib import Path
import logging

class ClaudeWebhookHandler(BaseHTTPRequestHandler):
    """HTTP request handler for Claude webhook endpoints"""
    
    def __init__(self, *args, claude_instance=None, **kwargs):
        self.claude_instance = claude_instance
        super().__init__(*args, **kwargs)
    
    def do_GET(self):
        """Handle GET requests - webhook status and info"""
        parsed_path = urlparse(self.path)
        
        if parsed_path.path == '/status':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            status = {
                "status": "active",
                "claude_available": self.claude_instance is not None,
                "memory_enabled": getattr(self.claude_instance, 'use_memory', False) if self.claude_instance else False,
                "endpoints": [
                    "/chat - POST: Send message to Claude",
                    "/memory/stats - GET: Get memory statistics", 
                    "/memory/clear - POST: Clear memories",
                    "/memory/recall - POST: Search memories",
                    "/mcp/status - GET: Get MCP services status",
                    "/mcp/desktop - POST: Execute desktop commands",
                    "/mcp/toolbox - POST: Use toolbox tools",
                    "/mcp/context - POST: Manage contexts",
                    "/workflow/list - GET: List workflows",
                    "/workflow/create - POST: Create workflow",
                    "/workflow/execute - POST: Execute workflow",
                    "/workflow/status - GET: Get workflow status",
                    "/automation/memory - GET: Get shared memory",
                    "/status - GET: Webhook status"
                ]
            }
            
            self.wfile.write(json.dumps(status, indent=2).encode())
            
        elif parsed_path.path == '/memory/stats':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            if self.claude_instance and hasattr(self.claude_instance, 'memory'):
                stats = self.claude_instance.memory.get_memory_stats()
                self.wfile.write(json.dumps(stats, indent=2).encode())
            else:
                error = {"error": "Memory system not available"}
                self.wfile.write(json.dumps(error).encode())
        
        elif parsed_path.path == '/mcp/status':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            if self.claude_instance:
                status = self.claude_instance.get_mcp_services_status()
                self.wfile.write(json.dumps(status, indent=2).encode())
            else:
                error = {"error": "Claude instance not available"}
                self.wfile.write(json.dumps(error).encode())
        
        elif parsed_path.path == '/workflow/list':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            if self.claude_instance:
                workflows = self.claude_instance.list_workflows()
                self.wfile.write(json.dumps(workflows, indent=2).encode())
            else:
                error = {"error": "Claude instance not available"}
                self.wfile.write(json.dumps(error).encode())
        
        elif parsed_path.path.startswith('/workflow/status'):
            parsed_query = parse_qs(parsed_path.query)
            workflow_id = parsed_query.get('id', [''])[0]
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            if self.claude_instance and workflow_id:
                status = self.claude_instance.get_workflow_status(workflow_id)
                self.wfile.write(json.dumps(status, indent=2).encode())
            else:
                error = {"error": "Claude instance not available or workflow ID missing"}
                self.wfile.write(json.dumps(error).encode())
        
        elif parsed_path.path == '/automation/memory':
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            if self.claude_instance:
                memory = self.claude_instance.get_shared_memory()
                self.wfile.write(json.dumps(memory, indent=2).encode())
            else:
                error = {"error": "Claude instance not available"}
                self.wfile.write(json.dumps(error).encode())
        
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Endpoint not found')
    
    def do_POST(self):
        """Handle POST requests - Claude interactions"""
        parsed_path = urlparse(self.path)
        content_length = int(self.headers['Content-Length'])
        post_data = self.rfile.read(content_length)
        
        try:
            data = json.loads(post_data.decode('utf-8'))
        except json.JSONDecodeError:
            self.send_response(400)
            self.end_headers()
            self.wfile.write(b'Invalid JSON')
            return
        
        if parsed_path.path == '/chat':
            self._handle_chat(data)
        elif parsed_path.path == '/memory/clear':
            self._handle_memory_clear(data)
        elif parsed_path.path == '/memory/recall':
            self._handle_memory_recall(data)
        elif parsed_path.path == '/mcp/desktop':
            self._handle_mcp_desktop(data)
        elif parsed_path.path == '/mcp/toolbox':
            self._handle_mcp_toolbox(data)
        elif parsed_path.path == '/mcp/context':
            self._handle_mcp_context(data)
        elif parsed_path.path == '/workflow/create':
            self._handle_workflow_create(data)
        elif parsed_path.path == '/workflow/execute':
            self._handle_workflow_execute(data)
        else:
            self.send_response(404)
            self.end_headers()
            self.wfile.write(b'Endpoint not found')
    
    def _handle_chat(self, data):
        """Handle chat requests from n8n"""
        message = data.get('message', '')
        system_prompt = data.get('system_prompt')
        model = data.get('model')
        save_to_memory = data.get('save_to_memory', True)
        
        if not message:
            self.send_response(400)
            self.end_headers()
            error = {"error": "Message is required"}
            self.wfile.write(json.dumps(error).encode())
            return
        
        if not self.claude_instance:
            self.send_response(500)
            self.end_headers()
            error = {"error": "Claude instance not available"}
            self.wfile.write(json.dumps(error).encode())
            return
        
        try:
            response = self.claude_instance.chat(
                message=message,
                system_prompt=system_prompt,
                model=model,
                save_to_memory=save_to_memory
            )
            
            if response:
                self.send_response(200)
                self.send_header('Content-type', 'application/json')
                self.end_headers()
                
                result = {
                    "response": response,
                    "model_used": model or self.claude_instance.model,
                    "memory_saved": save_to_memory and self.claude_instance.use_memory,
                    "timestamp": time.time()
                }
                
                self.wfile.write(json.dumps(result, indent=2).encode())
            else:
                self.send_response(500)
                self.end_headers()
                error = {"error": "Failed to get response from Claude"}
                self.wfile.write(json.dumps(error).encode())
                
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            error = {"error": f"Internal error: {str(e)}"}
            self.wfile.write(json.dumps(error).encode())
    
    def _handle_memory_clear(self, data):
        """Handle memory clear requests"""
        if not self.claude_instance or not hasattr(self.claude_instance, 'memory'):
            self.send_response(500)
            self.end_headers()
            error = {"error": "Memory system not available"}
            self.wfile.write(json.dumps(error).encode())
            return
        
        try:
            success = self.claude_instance.memory.clear_memories()
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            result = {
                "success": success,
                "message": "Memories cleared" if success else "Failed to clear memories"
            }
            
            self.wfile.write(json.dumps(result).encode())
            
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            error = {"error": f"Error clearing memories: {str(e)}"}
            self.wfile.write(json.dumps(error).encode())
    
    def _handle_memory_recall(self, data):
        """Handle memory recall requests"""
        query = data.get('query', '')
        limit = data.get('limit', 5)
        
        if not query:
            self.send_response(400)
            self.end_headers()
            error = {"error": "Query is required"}
            self.wfile.write(json.dumps(error).encode())
            return
        
        if not self.claude_instance or not hasattr(self.claude_instance, 'memory'):
            self.send_response(500)
            self.end_headers()
            error = {"error": "Memory system not available"}
            self.wfile.write(json.dumps(error).encode())
            return
        
        try:
            memories = self.claude_instance.memory.recall_memories(query, limit)
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            result = {
                "query": query,
                "memories": memories,
                "count": len(memories)
            }
            
            self.wfile.write(json.dumps(result, indent=2).encode())
            
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            error = {"error": f"Error recalling memories: {str(e)}"}
            self.wfile.write(json.dumps(error).encode())
    
    def _handle_mcp_desktop(self, data):
        """Handle desktop command requests"""
        command = data.get('command', '')
        args = data.get('args', [])
        
        if not command:
            self.send_response(400)
            self.end_headers()
            error = {"error": "Command is required"}
            self.wfile.write(json.dumps(error).encode())
            return
        
        if not self.claude_instance:
            self.send_response(500)
            self.end_headers()
            error = {"error": "Claude instance not available"}
            self.wfile.write(json.dumps(error).encode())
            return
        
        try:
            result = self.claude_instance.execute_desktop_command(command, args)
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            response = {
                "success": result is not None,
                "command": command,
                "args": args,
                "result": result.get('result', 'No result') if result else "Command failed"
            }
            
            self.wfile.write(json.dumps(response, indent=2).encode())
            
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            error = {"error": f"Error executing desktop command: {str(e)}"}
            self.wfile.write(json.dumps(error).encode())
    
    def _handle_mcp_toolbox(self, data):
        """Handle toolbox tool requests"""
        tool_name = data.get('tool_name', '')
        parameters = data.get('parameters', {})
        
        if not tool_name:
            self.send_response(400)
            self.end_headers()
            error = {"error": "Tool name is required"}
            self.wfile.write(json.dumps(error).encode())
            return
        
        if not self.claude_instance:
            self.send_response(500)
            self.end_headers()
            error = {"error": "Claude instance not available"}
            self.wfile.write(json.dumps(error).encode())
            return
        
        try:
            result = self.claude_instance.use_toolbox_tool(tool_name, parameters)
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            response = {
                "success": result is not None,
                "tool_name": tool_name,
                "parameters": parameters,
                "result": result.get('result', 'No result') if result else "Tool execution failed"
            }
            
            self.wfile.write(json.dumps(response, indent=2).encode())
            
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            error = {"error": f"Error executing toolbox tool: {str(e)}"}
            self.wfile.write(json.dumps(error).encode())
    
    def _handle_mcp_context(self, data):
        """Handle context management requests"""
        action = data.get('action', '')
        name = data.get('name', '')
        content = data.get('content', '')
        query = data.get('query', '')
        
        if not action:
            self.send_response(400)
            self.end_headers()
            error = {"error": "Action is required"}
            self.wfile.write(json.dumps(error).encode())
            return
        
        if not self.claude_instance:
            self.send_response(500)
            self.end_headers()
            error = {"error": "Claude instance not available"}
            self.wfile.write(json.dumps(error).encode())
            return
        
        try:
            result = self.claude_instance.manage_context(
                action=action,
                name=name if name else None,
                content=content if content else None,
                query=query if query else None
            )
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            response = {
                "success": result is not None,
                "action": action,
                "result": result.get('result', 'No result') if result else "Context operation failed"
            }
            
            self.wfile.write(json.dumps(response, indent=2).encode())
            
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            error = {"error": f"Error managing context: {str(e)}"}
            self.wfile.write(json.dumps(error).encode())
    
    def _handle_workflow_create(self, data):
        """Handle workflow creation requests"""
        name = data.get('name', '')
        description = data.get('description', '')
        tasks = data.get('tasks', [])
        
        if not name:
            self.send_response(400)
            self.end_headers()
            error = {"error": "Workflow name is required"}
            self.wfile.write(json.dumps(error).encode())
            return
        
        if not self.claude_instance:
            self.send_response(500)
            self.end_headers()
            error = {"error": "Claude instance not available"}
            self.wfile.write(json.dumps(error).encode())
            return
        
        try:
            workflow_id = self.claude_instance.create_workflow(name, description)
            
            # Add tasks if provided
            for task_def in tasks:
                task_type = task_def.get('type', 'claude')
                task_name = task_def.get('name', 'Unnamed Task')
                parameters = task_def.get('parameters', {})
                
                self.claude_instance.add_workflow_task(workflow_id, task_type, task_name, parameters)
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            response = {
                "success": True,
                "workflow_id": workflow_id,
                "name": name,
                "description": description,
                "tasks_added": len(tasks)
            }
            
            self.wfile.write(json.dumps(response, indent=2).encode())
            
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            error = {"error": f"Error creating workflow: {str(e)}"}
            self.wfile.write(json.dumps(error).encode())
    
    def _handle_workflow_execute(self, data):
        """Handle workflow execution requests"""
        workflow_id = data.get('workflow_id', '')
        context = data.get('context', {})
        
        if not workflow_id:
            self.send_response(400)
            self.end_headers()
            error = {"error": "Workflow ID is required"}
            self.wfile.write(json.dumps(error).encode())
            return
        
        if not self.claude_instance:
            self.send_response(500)
            self.end_headers()
            error = {"error": "Claude instance not available"}
            self.wfile.write(json.dumps(error).encode())
            return
        
        try:
            result = self.claude_instance.execute_workflow(workflow_id, context)
            
            self.send_response(200)
            self.send_header('Content-type', 'application/json')
            self.end_headers()
            
            self.wfile.write(json.dumps(result, indent=2).encode())
            
        except Exception as e:
            self.send_response(500)
            self.end_headers()
            error = {"error": f"Error executing workflow: {str(e)}"}
            self.wfile.write(json.dumps(error).encode())
    
    def log_message(self, format, *args):
        """Override to customize logging"""
        logging.info(f"Webhook: {format % args}")


class ClaudeWebhookServer:
    """Webhook server for n8n integration"""
    
    def __init__(self, claude_instance, host='localhost', port=8080):
        self.claude_instance = claude_instance
        self.host = host
        self.port = port
        self.server = None
        self.server_thread = None
        
        # Setup logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
    
    def start(self):
        """Start the webhook server"""
        try:
            # Create handler class with claude instance
            handler_class = lambda *args, **kwargs: ClaudeWebhookHandler(
                *args, claude_instance=self.claude_instance, **kwargs
            )
            
            self.server = HTTPServer((self.host, self.port), handler_class)
            
            print(f"🌐 Claude Webhook Server starting on http://{self.host}:{self.port}")
            print(f"📡 n8n Integration Endpoints:")
            print(f"   • POST http://{self.host}:{self.port}/chat")
            print(f"   • GET  http://{self.host}:{self.port}/status")
            print(f"   • GET  http://{self.host}:{self.port}/memory/stats")
            print(f"   • POST http://{self.host}:{self.port}/memory/clear")
            print(f"   • POST http://{self.host}:{self.port}/memory/recall")
            
            # Start server in separate thread
            self.server_thread = threading.Thread(target=self.server.serve_forever)
            self.server_thread.daemon = True
            self.server_thread.start()
            
            logging.info(f"Webhook server started on {self.host}:{self.port}")
            return True
            
        except Exception as e:
            print(f"❌ Failed to start webhook server: {e}")
            return False
    
    def stop(self):
        """Stop the webhook server"""
        if self.server:
            self.server.shutdown()
            self.server.server_close()
            if self.server_thread:
                self.server_thread.join()
            print("🛑 Webhook server stopped")
            logging.info("Webhook server stopped")
    
    def is_running(self):
        """Check if server is running"""
        return self.server is not None and self.server_thread is not None and self.server_thread.is_alive()