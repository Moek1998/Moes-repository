#!/usr/bin/env python3
"""
Basic tests for Claude Squad functionality
"""

import unittest
import os
import tempfile
import shutil
from claude_squad import Squad, Session
from claude_squad.exceptions import SquadError, SessionError


class TestSession(unittest.TestCase):
    """Test session functionality"""
    
    def setUp(self):
        """Set up test session"""
        self.session = Session("test-session", "Test Session", "Test description")
    
    def test_session_initialization(self):
        """Test session initialization"""
        self.assertEqual(self.session.session_id, "test-session")
        self.assertEqual(self.session.name, "Test Session")
        self.assertEqual(self.session.description, "Test description")
        self.assertEqual(len(self.session.messages), 0)
    
    def test_add_message(self):
        """Test adding messages to session"""
        self.session.add_message("user", "Hello")
        self.session.add_message("assistant", "Hi there!")
        
        self.assertEqual(len(self.session.messages), 2)
        self.assertEqual(self.session.messages[0]["role"], "user")
        self.assertEqual(self.session.messages[0]["content"], "Hello")
        self.assertEqual(self.session.messages[1]["role"], "assistant")
        self.assertEqual(self.session.messages[1]["content"], "Hi there!")
    
    def test_get_messages(self):
        """Test getting messages from session"""
        self.session.add_message("user", "Test message")
        messages = self.session.get_messages()
        
        self.assertEqual(len(messages), 1)
        self.assertEqual(messages[0]["content"], "Test message")
    
    def test_clear_messages(self):
        """Test clearing messages from session"""
        self.session.add_message("user", "Test message")
        self.session.clear_messages()
        
        self.assertEqual(len(self.session.messages), 0)
    
    def test_to_dict(self):
        """Test converting session to dictionary"""
        self.session.add_message("user", "Test message")
        session_dict = self.session.to_dict()
        
        self.assertEqual(session_dict["session_id"], "test-session")
        self.assertEqual(session_dict["name"], "Test Session")
        self.assertEqual(len(session_dict["messages"]), 1)
    
    def test_from_dict(self):
        """Test creating session from dictionary"""
        session_data = {
            "session_id": "test-session",
            "name": "Test Session",
            "description": "Test description",
            "created_at": "2023-01-01T00:00:00",
            "updated_at": "2023-01-01T00:00:00",
            "messages": [{"role": "user", "content": "Test"}],
            "metadata": {}
        }
        
        session = Session.from_dict(session_data)
        
        self.assertEqual(session.session_id, "test-session")
        self.assertEqual(session.name, "Test Session")
        self.assertEqual(len(session.messages), 1)


class TestSquad(unittest.TestCase):
    """Test squad functionality"""
    
    def setUp(self):
        """Set up test squad"""
        self.temp_dir = tempfile.mkdtemp()
        self.squad = Squad("test-squad", base_directory=self.temp_dir)
    
    def tearDown(self):
        """Clean up test squad"""
        shutil.rmtree(self.temp_dir)
    
    def test_squad_initialization(self):
        """Test squad initialization"""
        self.assertEqual(self.squad.squad_name, "test-squad")
        self.assertEqual(len(self.squad.sessions), 0)
        self.assertTrue(os.path.exists(self.squad.squad_directory))
    
    def test_add_session(self):
        """Test adding session to squad"""
        session = self.squad.add_session("test-session", "Test Session", "Test description")
        
        self.assertEqual(len(self.squad.sessions), 1)
        self.assertEqual(session.session_id, "test-session")
        self.assertEqual(session.name, "Test Session")
        self.assertIn("test-session", self.squad.sessions)
    
    def test_get_session(self):
        """Test getting session from squad"""
        self.squad.add_session("test-session", "Test Session")
        session = self.squad.get_session("test-session")
        
        self.assertEqual(session.session_id, "test-session")
        self.assertEqual(session.name, "Test Session")
    
    def test_get_session_not_found(self):
        """Test getting non-existent session"""
        with self.assertRaises(SquadError):
            self.squad.get_session("non-existent")
    
    def test_get_sessions(self):
        """Test getting all sessions"""
        self.squad.add_session("session1", "Session 1")
        self.squad.add_session("session2", "Session 2")
        
        sessions = self.squad.get_sessions()
        self.assertEqual(len(sessions), 2)
    
    def test_remove_session(self):
        """Test removing session from squad"""
        self.squad.add_session("test-session", "Test Session")
        self.assertEqual(len(self.squad.sessions), 1)
        
        self.squad.remove_session("test-session")
        self.assertEqual(len(self.squad.sessions), 0)
    
    def test_list_sessions(self):
        """Test listing sessions with details"""
        self.squad.add_session("test-session", "Test Session", "Test description")
        session_list = self.squad.list_sessions()
        
        self.assertEqual(len(session_list), 1)
        self.assertEqual(session_list[0]["session_id"], "test-session")
        self.assertEqual(session_list[0]["name"], "Test Session")
        self.assertEqual(session_list[0]["message_count"], 0)
    
    def test_export_import_squad(self):
        """Test exporting and importing squad"""
        # Add some sessions
        self.squad.add_session("session1", "Session 1")
        self.squad.add_session("session2", "Session 2")
        
        # Add messages
        session1 = self.squad.get_session("session1")
        session1.add_message("user", "Test message")
        self.squad.save_session("session1")
        
        # Export squad
        export_file = os.path.join(self.temp_dir, "export.json")
        self.squad.export_squad(export_file)
        
        # Import squad
        imported_squad = Squad.import_squad(export_file, "imported-squad")
        
        self.assertEqual(imported_squad.squad_name, "imported-squad")
        self.assertEqual(len(imported_squad.sessions), 2)
        
        # Check imported session
        imported_session = imported_squad.get_session("session1")
        self.assertEqual(len(imported_session.messages), 1)
        self.assertEqual(imported_session.messages[0]["content"], "Test message")


if __name__ == '__main__':
    unittest.main()