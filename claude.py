#!/usr/bin/env python3
"""
Claude CLI - A command-line interface for interacting with Claude AI
"""

import sys
import os
import argparse
import json
import requests
from pathlib import Path
import configparser

class ClaudeCLI:
    def __init__(self):
        self.config_dir = Path.home() / '.claude'
        self.config_file = self.config_dir / 'config.ini'
        self.api_key = None
        self.api_url = "https://api.anthropic.com/v1/messages"
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
            'model': 'claude-3-sonnet-20240229',
            'max_tokens': '1000'
        }
        
        with open(self.config_file, 'w') as f:
            config.write(f)
        
        print(f"Created config file at {self.config_file}")
        print("Please add your Anthropic API key to the config file or set ANTHROPIC_API_KEY environment variable")

    def load_config(self):
        """Load configuration from file"""
        config = configparser.ConfigParser()
        config.read(self.config_file)
        
        # Try to get API key from config file or environment variable
        self.api_key = (
            os.getenv('ANTHROPIC_API_KEY') or 
            config.get('DEFAULT', 'api_key', fallback='')
        )
        
        self.model = config.get('DEFAULT', 'model', fallback='claude-3-sonnet-20240229')
        self.max_tokens = config.getint('DEFAULT', 'max_tokens', fallback=1000)

    def setup_api_key(self, api_key):
        """Setup API key in config file"""
        config = configparser.ConfigParser()
        config.read(self.config_file)
        config.set('DEFAULT', 'api_key', api_key)
        
        with open(self.config_file, 'w') as f:
            config.write(f)
        
        self.api_key = api_key
        print("API key saved successfully!")

    def chat(self, message, system_prompt=None):
        """Send a message to Claude and get response"""
        if not self.api_key:
            print("Error: No API key found. Please set up your API key first.")
            print("Use: claude --setup-key YOUR_API_KEY")
            print("Or set ANTHROPIC_API_KEY environment variable")
            return None

        headers = {
            'Content-Type': 'application/json',
            'x-api-key': self.api_key,
            'anthropic-version': '2023-06-01'
        }

        messages = [{"role": "user", "content": message}]
        
        data = {
            'model': self.model,
            'max_tokens': self.max_tokens,
            'messages': messages
        }
        
        if system_prompt:
            data['system'] = system_prompt

        try:
            response = requests.post(self.api_url, headers=headers, json=data)
            response.raise_for_status()
            
            result = response.json()
            return result['content'][0]['text']
            
        except requests.exceptions.RequestException as e:
            print(f"Error making request: {e}")
            return None
        except KeyError as e:
            print(f"Error parsing response: {e}")
            print(f"Response: {response.text}")
            return None

    def interactive_mode(self):
        """Start interactive chat mode"""
        print("Claude CLI - Interactive Mode")
        print("Type 'exit' or 'quit' to leave, 'clear' to clear screen")
        print("-" * 50)
        
        while True:
            try:
                user_input = input("\nYou: ").strip()
                
                if user_input.lower() in ['exit', 'quit']:
                    print("Goodbye!")
                    break
                
                if user_input.lower() == 'clear':
                    os.system('clear' if os.name == 'posix' else 'cls')
                    continue
                
                if not user_input:
                    continue
                
                print("Claude: ", end="", flush=True)
                response = self.chat(user_input)
                
                if response:
                    print(response)
                else:
                    print("Sorry, I couldn't process your request.")
                    
            except KeyboardInterrupt:
                print("\nGoodbye!")
                break
            except EOFError:
                print("\nGoodbye!")
                break

def main():
    parser = argparse.ArgumentParser(description='Claude CLI - Interact with Claude AI from the command line')
    parser.add_argument('message', nargs='*', help='Message to send to Claude')
    parser.add_argument('-i', '--interactive', action='store_true', help='Start interactive mode')
    parser.add_argument('-s', '--system', help='System prompt for the conversation')
    parser.add_argument('--setup-key', help='Setup API key')
    parser.add_argument('--config', action='store_true', help='Show config file location')
    
    args = parser.parse_args()
    
    claude = ClaudeCLI()
    
    if args.setup_key:
        claude.setup_api_key(args.setup_key)
        return
    
    if args.config:
        print(f"Config file location: {claude.config_file}")
        return
    
    if args.interactive:
        claude.interactive_mode()
        return
    
    if args.message:
        message = ' '.join(args.message)
        response = claude.chat(message, args.system)
        if response:
            print(response)
    else:
        # If no message provided, start interactive mode
        claude.interactive_mode()

if __name__ == '__main__':
    main()