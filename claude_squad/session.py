"""
Session management for Claude Squad
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Any
from .exceptions import SessionError


class Session:
    """Represents a Claude conversation session"""
    
    def __init__(self, session_id: str, name: str, description: str = ""):
        self.session_id = session_id
        self.name = name
        self.description = description
        self.created_at = datetime.now().isoformat()
        self.updated_at = self.created_at
        self.messages: List[Dict[str, Any]] = []
        self.metadata: Dict[str, Any] = {}
        
    def add_message(self, role: str, content: str, metadata: Optional[Dict[str, Any]] = None):
        """Add a message to the session"""
        message = {
            "role": role,
            "content": content,
            "timestamp": datetime.now().isoformat(),
            "metadata": metadata or {}
        }
        self.messages.append(message)
        self.updated_at = datetime.now().isoformat()
    
    def get_messages(self) -> List[Dict[str, Any]]:
        """Get all messages in the session"""
        return self.messages.copy()
    
    def clear_messages(self):
        """Clear all messages from the session"""
        self.messages.clear()
        self.updated_at = datetime.now().isoformat()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert session to dictionary"""
        return {
            "session_id": self.session_id,
            "name": self.name,
            "description": self.description,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "messages": self.messages,
            "metadata": self.metadata
        }
    
    @classmethod
    def from_dict(cls, data: Dict[str, Any]) -> 'Session':
        """Create session from dictionary"""
        session = cls(
            session_id=data["session_id"],
            name=data["name"],
            description=data.get("description", "")
        )
        session.created_at = data["created_at"]
        session.updated_at = data["updated_at"]
        session.messages = data.get("messages", [])
        session.metadata = data.get("metadata", {})
        return session
    
    def save(self, directory: str):
        """Save session to file"""
        try:
            os.makedirs(directory, exist_ok=True)
            filepath = os.path.join(directory, f"{self.session_id}.json")
            
            with open(filepath, 'w', encoding='utf-8') as f:
                json.dump(self.to_dict(), f, indent=2, ensure_ascii=False)
                
        except Exception as e:
            raise SessionError(f"Failed to save session: {e}")
    
    @classmethod
    def load(cls, filepath: str) -> 'Session':
        """Load session from file"""
        try:
            with open(filepath, 'r', encoding='utf-8') as f:
                data = json.load(f)
            return cls.from_dict(data)
            
        except Exception as e:
            raise SessionError(f"Failed to load session: {e}")
    
    def __repr__(self):
        return f"Session(id='{self.session_id}', name='{self.name}', messages={len(self.messages)})"