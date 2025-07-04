#!/usr/bin/env python3
"""
Example script demonstrating Claude Code usage
"""

import os
from claude_code import ClaudeClient
from claude_code.exceptions import ClaudeError

def main():
    """Example usage of Claude Code"""
    
    # Check if API key is set
    if not os.getenv('CLAUDE_API_KEY'):
        print("Please set your CLAUDE_API_KEY environment variable")
        print("You can create a .env file with: CLAUDE_API_KEY=your-api-key")
        return
    
    try:
        # Initialize the client
        print("Initializing Claude client...")
        client = ClaudeClient()
        
        # Send a simple message
        print("\nSending a message to Claude...")
        response = client.send_message("Hello Claude! Can you help me understand what you can do?")
        print(f"Claude's response: {response}")
        
        # Continue the conversation
        print("\nContinuing the conversation...")
        response = client.send_message("Can you write a short Python function to calculate factorial?")
        print(f"Claude's response: {response}")
        
        # Show conversation history
        print("\nConversation history:")
        for i, message in enumerate(client.get_history(), 1):
            print(f"{i}. {message['role'].capitalize()}: {message['content'][:100]}...")
        
        # Save conversation
        print("\nSaving conversation...")
        client.save_conversation("example_conversation.json")
        print("Conversation saved to example_conversation.json")
        
    except ClaudeError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()