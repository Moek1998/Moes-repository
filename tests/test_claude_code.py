#!/usr/bin/env python3
"""
Basic tests for Claude Code functionality
"""

import unittest
import os
import tempfile
import json
from unittest.mock import patch, MagicMock
from claude_code import ClaudeClient, Config
from claude_code.exceptions import ClaudeError, ClaudeAPIError


class TestConfig(unittest.TestCase):
    """Test configuration functionality"""
    
    def test_config_initialization(self):
        """Test config initialization with API key"""
        config = Config(api_key="test-key")
        self.assertEqual(config.api_key, "test-key")
        self.assertEqual(config.model, "claude-3-sonnet-20240229")
    
    def test_config_validation_success(self):
        """Test successful config validation"""
        config = Config(api_key="test-key")
        self.assertTrue(config.validate())
    
    def test_config_validation_failure(self):
        """Test config validation failure without API key"""
        config = Config()
        with self.assertRaises(ValueError):
            config.validate()


class TestClaudeClient(unittest.TestCase):
    """Test Claude client functionality"""
    
    def setUp(self):
        """Set up test client"""
        self.client = ClaudeClient(api_key="test-key")
    
    def test_client_initialization(self):
        """Test client initialization"""
        self.assertIsNotNone(self.client.config)
        self.assertEqual(self.client.config.api_key, "test-key")
        self.assertEqual(len(self.client.conversation_history), 0)
    
    @patch('claude_code.client.Anthropic')
    def test_send_message(self, mock_anthropic):
        """Test sending a message"""
        # Mock the Anthropic client response
        mock_response = MagicMock()
        mock_response.content = [MagicMock(text="Hello! How can I help you?")]
        mock_anthropic.return_value.messages.create.return_value = mock_response
        
        # Create a new client to use the mocked Anthropic
        client = ClaudeClient(api_key="test-key")
        response = client.send_message("Hello")
        
        self.assertEqual(response, "Hello! How can I help you?")
        self.assertEqual(len(client.conversation_history), 2)  # user + assistant
    
    def test_clear_history(self):
        """Test clearing conversation history"""
        self.client.conversation_history = [{"role": "user", "content": "test"}]
        self.client.clear_history()
        self.assertEqual(len(self.client.conversation_history), 0)
    
    def test_get_history(self):
        """Test getting conversation history"""
        test_history = [{"role": "user", "content": "test"}]
        self.client.conversation_history = test_history
        history = self.client.get_history()
        self.assertEqual(history, test_history)
    
    def test_save_conversation(self):
        """Test saving conversation to file"""
        self.client.conversation_history = [
            {"role": "user", "content": "Hello"},
            {"role": "assistant", "content": "Hi there!"}
        ]
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
            temp_file = f.name
        
        try:
            self.client.save_conversation(temp_file)
            
            # Verify file contents
            with open(temp_file, 'r') as f:
                saved_data = json.load(f)
            
            self.assertEqual(saved_data, self.client.conversation_history)
        finally:
            os.unlink(temp_file)
    
    def test_load_conversation(self):
        """Test loading conversation from file"""
        test_conversation = [
            {"role": "user", "content": "Hello"},
            {"role": "assistant", "content": "Hi there!"}
        ]
        
        with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as f:
            json.dump(test_conversation, f)
            temp_file = f.name
        
        try:
            self.client.load_conversation(temp_file)
            self.assertEqual(self.client.conversation_history, test_conversation)
        finally:
            os.unlink(temp_file)


if __name__ == '__main__':
    unittest.main()