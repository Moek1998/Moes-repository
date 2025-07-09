#!/usr/bin/env python3
"""
Claude Automation Platform - Unified interface for all automation systems
Orchestrates Claude CLI, MCP services, n8n workflows, and SmartBots coordination
"""

import json
import asyncio
import logging
import time
from typing import Dict, List, Any, Optional
from pathlib import Path
import requests
from dataclasses import dataclass, asdict

@dataclass
class AutomationTask:
    """Represents an automation task"""
    id: str
    name: str
    type: str  # 'claude', 'mcp', 'n8n', 'smartbots', 'composite'
    parameters: Dict[str, Any]
    dependencies: List[str] = None
    status: str = 'pending'  # 'pending', 'running', 'completed', 'failed'
    result: Any = None
    created_at: float = None
    completed_at: float = None
    
    def __post_init__(self):
        if self.dependencies is None:
            self.dependencies = []
        if self.created_at is None:
            self.created_at = time.time()

@dataclass
class WorkflowDefinition:
    """Defines a complete automation workflow"""
    id: str
    name: str
    description: str
    tasks: List[AutomationTask]
    triggers: List[Dict[str, Any]] = None
    schedule: str = None
    enabled: bool = True
    
    def __post_init__(self):
        if self.triggers is None:
            self.triggers = []

class AutomationPlatform:
    """Central automation platform orchestrating all systems"""
    
    def __init__(self, claude_instance=None):
        self.claude_instance = claude_instance
        self.workflows = {}
        self.task_queue = []
        self.running_tasks = {}
        self.completed_tasks = {}
        self.shared_memory = {}
        
        # System integrations
        self.n8n_base_url = "http://localhost:5678"
        self.smartbots_base_url = "http://localhost:3000"
        self.webhook_base_url = "http://localhost:8080"
        
        # Setup logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)
    
    def register_workflow(self, workflow: WorkflowDefinition) -> bool:
        """Register a new automation workflow"""
        try:
            self.workflows[workflow.id] = workflow
            self.logger.info(f"Registered workflow: {workflow.name}")
            return True
        except Exception as e:
            self.logger.error(f"Failed to register workflow: {e}")
            return False
    
    def create_composite_workflow(self, name: str, description: str) -> str:
        """Create a new composite workflow"""
        workflow_id = f"workflow_{int(time.time())}"
        workflow = WorkflowDefinition(
            id=workflow_id,
            name=name,
            description=description,
            tasks=[]
        )
        self.register_workflow(workflow)
        return workflow_id
    
    def add_task_to_workflow(self, workflow_id: str, task: AutomationTask) -> bool:
        """Add a task to an existing workflow"""
        if workflow_id not in self.workflows:
            self.logger.error(f"Workflow {workflow_id} not found")
            return False
        
        self.workflows[workflow_id].tasks.append(task)
        self.logger.info(f"Added task {task.name} to workflow {workflow_id}")
        return True
    
    def execute_workflow(self, workflow_id: str, context: Dict[str, Any] = None) -> Dict[str, Any]:
        """Execute a complete workflow"""
        if workflow_id not in self.workflows:
            return {"error": f"Workflow {workflow_id} not found"}
        
        workflow = self.workflows[workflow_id]
        if not workflow.enabled:
            return {"error": f"Workflow {workflow_id} is disabled"}
        
        self.logger.info(f"Executing workflow: {workflow.name}")
        
        # Initialize execution context
        execution_context = {
            "workflow_id": workflow_id,
            "start_time": time.time(),
            "context": context or {},
            "results": {},
            "shared_memory": self.shared_memory.copy()
        }
        
        # Execute tasks in dependency order
        try:
            for task in self._resolve_task_dependencies(workflow.tasks):
                result = self.execute_task(task, execution_context)
                execution_context["results"][task.id] = result
                
                # Update shared memory with task results
                if result.get("memory_update"):
                    self.shared_memory.update(result["memory_update"])
                    execution_context["shared_memory"] = self.shared_memory
            
            execution_context["status"] = "completed"
            execution_context["end_time"] = time.time()
            execution_context["duration"] = execution_context["end_time"] - execution_context["start_time"]
            
            self.logger.info(f"Workflow {workflow.name} completed successfully")
            return execution_context
            
        except Exception as e:
            execution_context["status"] = "failed"
            execution_context["error"] = str(e)
            execution_context["end_time"] = time.time()
            
            self.logger.error(f"Workflow {workflow.name} failed: {e}")
            return execution_context
    
    def execute_task(self, task: AutomationTask, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute a single automation task"""
        self.logger.info(f"Executing task: {task.name} ({task.type})")
        
        task.status = 'running'
        start_time = time.time()
        
        try:
            if task.type == 'claude':
                result = self._execute_claude_task(task, context)
            elif task.type == 'mcp':
                result = self._execute_mcp_task(task, context)
            elif task.type == 'n8n':
                result = self._execute_n8n_task(task, context)
            elif task.type == 'smartbots':
                result = self._execute_smartbots_task(task, context)
            elif task.type == 'composite':
                result = self._execute_composite_task(task, context)
            else:
                raise ValueError(f"Unknown task type: {task.type}")
            
            task.status = 'completed'
            task.completed_at = time.time()
            task.result = result
            
            self.logger.info(f"Task {task.name} completed successfully")
            return {"success": True, "result": result, "duration": time.time() - start_time}
            
        except Exception as e:
            task.status = 'failed'
            task.completed_at = time.time()
            task.result = {"error": str(e)}
            
            self.logger.error(f"Task {task.name} failed: {e}")
            return {"success": False, "error": str(e), "duration": time.time() - start_time}
    
    def _execute_claude_task(self, task: AutomationTask, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute Claude AI task"""
        if not self.claude_instance:
            raise Exception("Claude instance not available")
        
        message = task.parameters.get('message', '')
        system_prompt = task.parameters.get('system_prompt')
        model = task.parameters.get('model')
        save_to_memory = task.parameters.get('save_to_memory', True)
        
        # Enhance message with context
        if context.get('shared_memory'):
            memory_context = str(context['shared_memory'])
            message = f"Context: {memory_context}\n\nTask: {message}"
        
        response = self.claude_instance.chat(
            message=message,
            system_prompt=system_prompt,
            model=model,
            save_to_memory=save_to_memory
        )
        
        return {
            "response": response,
            "model_used": model or self.claude_instance.model,
            "memory_update": {"last_claude_response": response} if save_to_memory else {}
        }
    
    def _execute_mcp_task(self, task: AutomationTask, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute MCP service task"""
        if not self.claude_instance or not hasattr(self.claude_instance, 'mcp_services'):
            raise Exception("MCP services not available")
        
        service_type = task.parameters.get('service', '')
        action = task.parameters.get('action', '')
        
        if service_type == 'desktop':
            command = task.parameters.get('command', '')
            args = task.parameters.get('args', [])
            result = self.claude_instance.execute_desktop_command(command, args)
        
        elif service_type == 'toolbox':
            tool_name = task.parameters.get('tool_name', '')
            parameters = task.parameters.get('parameters', {})
            result = self.claude_instance.use_toolbox_tool(tool_name, parameters)
        
        elif service_type == 'context':
            name = task.parameters.get('name')
            content = task.parameters.get('content')
            query = task.parameters.get('query')
            result = self.claude_instance.manage_context(action, name, content, query)
        
        else:
            raise ValueError(f"Unknown MCP service: {service_type}")
        
        return {
            "service": service_type,
            "action": action,
            "result": result,
            "memory_update": {f"mcp_{service_type}_result": result}
        }
    
    def _execute_n8n_task(self, task: AutomationTask, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute n8n workflow task"""
        workflow_id = task.parameters.get('workflow_id', '')
        webhook_url = task.parameters.get('webhook_url', '')
        data = task.parameters.get('data', {})
        
        # Add context data to the request
        enhanced_data = {
            **data,
            "context": context.get('shared_memory', {}),
            "workflow_context": context.get('context', {})
        }
        
        if webhook_url:
            # Execute via webhook
            response = requests.post(webhook_url, json=enhanced_data)
            response.raise_for_status()
            result = response.json()
        else:
            # Execute via n8n API (if available)
            url = f"{self.n8n_base_url}/api/v1/workflows/{workflow_id}/execute"
            response = requests.post(url, json=enhanced_data)
            response.raise_for_status()
            result = response.json()
        
        return {
            "workflow_id": workflow_id,
            "result": result,
            "memory_update": {"n8n_result": result}
        }
    
    def _execute_smartbots_task(self, task: AutomationTask, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute SmartBots coordination task"""
        action = task.parameters.get('action', '')
        bots = task.parameters.get('bots', [])
        commands = task.parameters.get('commands', [])
        
        # Prepare SmartBots request
        smartbots_data = {
            "action": action,
            "bots": bots,
            "commands": commands,
            "context": context.get('shared_memory', {})
        }
        
        # Execute SmartBots command
        url = f"{self.smartbots_base_url}/api/execute"
        response = requests.post(url, json=smartbots_data)
        response.raise_for_status()
        result = response.json()
        
        return {
            "action": action,
            "bots": bots,
            "result": result,
            "memory_update": {"smartbots_result": result}
        }
    
    def _execute_composite_task(self, task: AutomationTask, context: Dict[str, Any]) -> Dict[str, Any]:
        """Execute composite task (multiple sub-tasks)"""
        sub_tasks = task.parameters.get('sub_tasks', [])
        results = []
        
        for sub_task_def in sub_tasks:
            sub_task = AutomationTask(**sub_task_def)
            result = self.execute_task(sub_task, context)
            results.append(result)
            
            # Update context with sub-task results
            if result.get("memory_update"):
                context["shared_memory"].update(result["memory_update"])
        
        return {
            "sub_tasks_count": len(sub_tasks),
            "results": results,
            "memory_update": {"composite_task_completed": True}
        }
    
    def _resolve_task_dependencies(self, tasks: List[AutomationTask]) -> List[AutomationTask]:
        """Resolve task dependencies and return execution order"""
        # Simple dependency resolution (topological sort)
        resolved = []
        remaining = tasks.copy()
        
        while remaining:
            # Find tasks with no unresolved dependencies
            ready_tasks = [
                task for task in remaining 
                if all(dep_id in [t.id for t in resolved] for dep_id in task.dependencies)
            ]
            
            if not ready_tasks:
                # Circular dependency or missing dependency
                raise Exception("Circular dependency or missing dependency detected")
            
            # Add ready tasks to resolved list
            for task in ready_tasks:
                resolved.append(task)
                remaining.remove(task)
        
        return resolved
    
    def get_workflow_status(self, workflow_id: str) -> Dict[str, Any]:
        """Get status of a workflow"""
        if workflow_id not in self.workflows:
            return {"error": f"Workflow {workflow_id} not found"}
        
        workflow = self.workflows[workflow_id]
        return {
            "id": workflow.id,
            "name": workflow.name,
            "description": workflow.description,
            "enabled": workflow.enabled,
            "task_count": len(workflow.tasks),
            "tasks": [
                {
                    "id": task.id,
                    "name": task.name,
                    "type": task.type,
                    "status": task.status,
                    "dependencies": task.dependencies
                }
                for task in workflow.tasks
            ]
        }
    
    def list_workflows(self) -> List[Dict[str, Any]]:
        """List all registered workflows"""
        return [
            {
                "id": workflow.id,
                "name": workflow.name,
                "description": workflow.description,
                "enabled": workflow.enabled,
                "task_count": len(workflow.tasks)
            }
            for workflow in self.workflows.values()
        ]
    
    def get_shared_memory(self) -> Dict[str, Any]:
        """Get current shared memory state"""
        return self.shared_memory.copy()
    
    def update_shared_memory(self, updates: Dict[str, Any]) -> None:
        """Update shared memory"""
        self.shared_memory.update(updates)
        self.logger.info(f"Updated shared memory with {len(updates)} items")
    
    def clear_shared_memory(self) -> None:
        """Clear shared memory"""
        self.shared_memory.clear()
        self.logger.info("Cleared shared memory")


# Global automation platform instance
automation_platform = None

def get_automation_platform(claude_instance=None):
    """Get or create automation platform instance"""
    global automation_platform
    if automation_platform is None:
        automation_platform = AutomationPlatform(claude_instance)
    return automation_platform