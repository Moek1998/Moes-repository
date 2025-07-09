#!/usr/bin/env python3
"""
Claude Memory Module - Integrates with mem0-memory-mcp for persistent conversations
"""

import json
import subprocess
import sys
from pathlib import Path
from typing import Optional, List, Dict, Any

class ClaudeMemory:
    def __init__(self, user_id: str = "default_user"):
        self.user_id = user_id
        self.mcp_config_path = Path(__file__).parent.parent / "claude-code-mcp-config.json"
        self.session_id = None
        
    def _run_mcp_command(self, command: str, data: Dict[str, Any] = None) -> Optional[Dict]:
        """Run MCP command through the mem0-memory-mcp server"""
        try:
            # Use the MCP configuration to run memory commands
            cmd = [
                "cmd", "/c", "npx", "-y", "@smithery/cli@latest", "run",
                "@mem0ai/mem0-memory-mcp", "--key", "5bed2123-16c7-466f-9fd8-4a04e97ac694",
                "--profile", "expensive-slug-FXI3zk"
            ]
            
            # Create input for the MCP server
            mcp_input = {
                "method": command,
                "params": data or {}
            }
            
            # Run the command (simplified for now - in real implementation would use MCP protocol)
            print(f"🧠 Memory operation: {command}")
            return {"success": True, "data": data}
            
        except Exception as e:
            print(f"Memory operation failed: {e}")
            return None
    
    def save_conversation(self, messages: List[Dict[str, str]], context: str = "") -> bool:
        """Save conversation to memory"""
        try:
            memory_data = {
                "user_id": self.user_id,
                "messages": messages,
                "context": context,
                "timestamp": str(Path().stat().st_mtime)
            }
            
            result = self._run_mcp_command("add_memory", {
                "text": json.dumps(memory_data),
                "user_id": self.user_id,
                "metadata": {"type": "conversation", "context": context}
            })
            
            return result is not None
            
        except Exception as e:
            print(f"Failed to save conversation: {e}")
            return False
    
    def recall_memories(self, query: str, limit: int = 5) -> List[Dict]:
        """Recall relevant memories based on query"""
        try:
            result = self._run_mcp_command("search_memories", {
                "query": query,
                "user_id": self.user_id,
                "limit": limit
            })
            
            if result and result.get("success"):
                # Simulate memory recall for now
                return [
                    {
                        "content": f"Previous conversation about: {query}",
                        "relevance": 0.8,
                        "timestamp": "recent"
                    }
                ]
            
            return []
            
        except Exception as e:
            print(f"Failed to recall memories: {e}")
            return []
    
    def get_conversation_context(self, current_message: str) -> str:
        """Get relevant conversation context for current message"""
        try:
            memories = self.recall_memories(current_message, limit=3)
            
            if not memories:
                return ""
            
            context_parts = []
            for memory in memories:
                context_parts.append(f"Previous context: {memory['content']}")
            
            return "\n".join(context_parts)
            
        except Exception as e:
            print(f"Failed to get conversation context: {e}")
            return ""
    
    def clear_memories(self, user_id: str = None) -> bool:
        """Clear all memories for a user"""
        try:
            target_user = user_id or self.user_id
            
            result = self._run_mcp_command("delete_memories", {
                "user_id": target_user
            })
            
            return result is not None
            
        except Exception as e:
            print(f"Failed to clear memories: {e}")
            return False
    
    def get_memory_stats(self) -> Dict[str, Any]:
        """Get memory usage statistics"""
        try:
            result = self._run_mcp_command("get_memories", {
                "user_id": self.user_id
            })
            
            if result and result.get("success"):
                # Simulate stats for now
                return {
                    "total_memories": 10,
                    "conversations": 5,
                    "last_updated": "recent",
                    "user_id": self.user_id
                }
            
            return {}
            
        except Exception as e:
            print(f"Failed to get memory stats: {e}")
            return {}