"""
Squad management for organizing Claude sessions
"""

import json
import os
from datetime import datetime
from typing import Dict, List, Optional, Any
from .session import Session
from .exceptions import SquadError, SquadNotFoundError


class Squad:
    """Manages a collection of Claude sessions"""
    
    def __init__(self, squad_name: str, base_directory: str = "squads"):
        self.squad_name = squad_name
        self.base_directory = base_directory
        self.squad_directory = os.path.join(base_directory, squad_name)
        self.created_at = datetime.now().isoformat()
        self.updated_at = self.created_at
        self.sessions: Dict[str, Session] = {}
        self.metadata: Dict[str, Any] = {}
        
        # Create squad directory if it doesn't exist
        os.makedirs(self.squad_directory, exist_ok=True)
        
        # Load existing squad if it exists
        self._load_squad()
    
    def _load_squad(self):
        """Load existing squad configuration and sessions"""
        squad_config_path = os.path.join(self.squad_directory, "squad.json")
        
        if os.path.exists(squad_config_path):
            try:
                with open(squad_config_path, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    
                self.created_at = config.get("created_at", self.created_at)
                self.updated_at = config.get("updated_at", self.updated_at)
                self.metadata = config.get("metadata", {})
                
                # Load sessions
                sessions_dir = os.path.join(self.squad_directory, "sessions")
                if os.path.exists(sessions_dir):
                    for filename in os.listdir(sessions_dir):
                        if filename.endswith('.json'):
                            session_path = os.path.join(sessions_dir, filename)
                            try:
                                session = Session.load(session_path)
                                self.sessions[session.session_id] = session
                            except Exception as e:
                                print(f"Warning: Failed to load session {filename}: {e}")
                                
            except Exception as e:
                print(f"Warning: Failed to load squad configuration: {e}")
    
    def _save_squad_config(self):
        """Save squad configuration"""
        config = {
            "squad_name": self.squad_name,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "metadata": self.metadata,
            "sessions": list(self.sessions.keys())
        }
        
        squad_config_path = os.path.join(self.squad_directory, "squad.json")
        try:
            with open(squad_config_path, 'w', encoding='utf-8') as f:
                json.dump(config, f, indent=2, ensure_ascii=False)
        except Exception as e:
            raise SquadError(f"Failed to save squad configuration: {e}")
    
    def add_session(self, session_id: str, name: str, description: str = "") -> Session:
        """Add a new session to the squad"""
        if session_id in self.sessions:
            raise SquadError(f"Session '{session_id}' already exists")
            
        session = Session(session_id, name, description)
        self.sessions[session_id] = session
        self.updated_at = datetime.now().isoformat()
        
        # Save session and squad config
        sessions_dir = os.path.join(self.squad_directory, "sessions")
        session.save(sessions_dir)
        self._save_squad_config()
        
        return session
    
    def get_session(self, session_id: str) -> Session:
        """Get a session by ID"""
        if session_id not in self.sessions:
            raise SquadError(f"Session '{session_id}' not found")
        return self.sessions[session_id]
    
    def get_sessions(self) -> List[Session]:
        """Get all sessions in the squad"""
        return list(self.sessions.values())
    
    def remove_session(self, session_id: str):
        """Remove a session from the squad"""
        if session_id not in self.sessions:
            raise SquadError(f"Session '{session_id}' not found")
            
        # Remove session file
        sessions_dir = os.path.join(self.squad_directory, "sessions")
        session_file = os.path.join(sessions_dir, f"{session_id}.json")
        if os.path.exists(session_file):
            os.remove(session_file)
        
        # Remove from memory
        del self.sessions[session_id]
        self.updated_at = datetime.now().isoformat()
        
        # Update squad config
        self._save_squad_config()
    
    def save_session(self, session_id: str):
        """Save a specific session"""
        if session_id not in self.sessions:
            raise SquadError(f"Session '{session_id}' not found")
            
        sessions_dir = os.path.join(self.squad_directory, "sessions")
        self.sessions[session_id].save(sessions_dir)
        self.updated_at = datetime.now().isoformat()
        self._save_squad_config()
    
    def list_sessions(self) -> List[Dict[str, Any]]:
        """List all sessions with basic information"""
        return [
            {
                "session_id": session.session_id,
                "name": session.name,
                "description": session.description,
                "created_at": session.created_at,
                "updated_at": session.updated_at,
                "message_count": len(session.messages)
            }
            for session in self.sessions.values()
        ]
    
    def export_squad(self, export_path: str):
        """Export the entire squad to a single file"""
        squad_data = {
            "squad_name": self.squad_name,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "metadata": self.metadata,
            "sessions": [session.to_dict() for session in self.sessions.values()]
        }
        
        try:
            with open(export_path, 'w', encoding='utf-8') as f:
                json.dump(squad_data, f, indent=2, ensure_ascii=False)
        except Exception as e:
            raise SquadError(f"Failed to export squad: {e}")
    
    @classmethod
    def import_squad(cls, import_path: str, squad_name: str = None) -> 'Squad':
        """Import a squad from a file"""
        try:
            with open(import_path, 'r', encoding='utf-8') as f:
                squad_data = json.load(f)
            
            # Use provided name or original name
            name = squad_name or squad_data["squad_name"]
            squad = cls(name)
            
            # Import metadata
            squad.created_at = squad_data.get("created_at", squad.created_at)
            squad.metadata = squad_data.get("metadata", {})
            
            # Import sessions
            for session_data in squad_data.get("sessions", []):
                session = Session.from_dict(session_data)
                squad.sessions[session.session_id] = session
                
                # Save session
                sessions_dir = os.path.join(squad.squad_directory, "sessions")
                session.save(sessions_dir)
            
            # Save squad config
            squad._save_squad_config()
            
            return squad
            
        except Exception as e:
            raise SquadError(f"Failed to import squad: {e}")
    
    def __repr__(self):
        return f"Squad(name='{self.squad_name}', sessions={len(self.sessions)})"