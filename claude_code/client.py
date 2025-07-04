"""
Main Claude client for interacting with Claude AI
"""

import json
import logging
from typing import Dict, List, Optional, Any
from anthropic import Anthropic
from .config import Config
from .exceptions import ClaudeError, ClaudeAPIError

logger = logging.getLogger(__name__)


class ClaudeClient:
    """Main client class for interacting with Claude AI"""
    
    def __init__(self, api_key: Optional[str] = None, config: Optional[Config] = None):
        self.config = config or Config(api_key=api_key)
        self.config.validate()
        
        self.client = Anthropic(api_key=self.config.api_key)
        self.conversation_history: List[Dict[str, str]] = []
        
    def send_message(self, message: str, system_prompt: Optional[str] = None) -> str:
        """Send a message to Claude and return the response"""
        try:
            # Add user message to history
            self.conversation_history.append({"role": "user", "content": message})
            
            # Prepare messages for API
            messages = self.conversation_history.copy()
            
            # Send request to Claude
            response = self.client.messages.create(
                model=self.config.model,
                max_tokens=self.config.max_tokens,
                temperature=self.config.temperature,
                system=system_prompt or "You are a helpful assistant.",
                messages=messages
            )
            
            # Extract response content
            response_content = response.content[0].text
            
            # Add assistant response to history
            self.conversation_history.append({"role": "assistant", "content": response_content})
            
            return response_content
            
        except Exception as e:
            logger.error(f"Error sending message to Claude: {e}")
            raise ClaudeAPIError(f"Failed to send message: {str(e)}")
    
    def clear_history(self):
        """Clear conversation history"""
        self.conversation_history.clear()
    
    def get_history(self) -> List[Dict[str, str]]:
        """Get conversation history"""
        return self.conversation_history.copy()
    
    def save_conversation(self, filename: str):
        """Save conversation history to a file"""
        try:
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(self.conversation_history, f, indent=2, ensure_ascii=False)
        except Exception as e:
            raise ClaudeError(f"Failed to save conversation: {str(e)}")
    
    def load_conversation(self, filename: str):
        """Load conversation history from a file"""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                self.conversation_history = json.load(f)
        except Exception as e:
            raise ClaudeError(f"Failed to load conversation: {str(e)}")