#!/usr/bin/env python3
"""
Claude CLI - A command-line interface for interacting with Claude
"""

import os
import sys
import argparse
import requests
import json
from typing import Optional

# ANSI color codes for better output
CYAN = '\033[96m'
GREEN = '\033[92m'
YELLOW = '\033[93m'
RED = '\033[91m'
RESET = '\033[0m'
BOLD = '\033[1m'

class ClaudeCLI:
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.environ.get('CLAUDE_API_KEY')
        if not self.api_key:
            print(f"{RED}Error: No API key found!{RESET}")
            print(f"Please set the CLAUDE_API_KEY environment variable or pass it as an argument.")
            print(f"You can get your API key from: https://console.anthropic.com/")
            sys.exit(1)
        
        self.api_url = "https://api.anthropic.com/v1/messages"
        self.headers = {
            "x-api-key": self.api_key,
            "anthropic-version": "2023-06-01",
            "content-type": "application/json"
        }
    
    def send_message(self, message: str, model: str = "claude-3-sonnet-20240229", 
                     max_tokens: int = 1024, temperature: float = 0.7):
        """Send a message to Claude and get a response"""
        
        data = {
            "model": model,
            "max_tokens": max_tokens,
            "temperature": temperature,
            "messages": [
                {"role": "user", "content": message}
            ]
        }
        
        try:
            print(f"{CYAN}Sending message to Claude...{RESET}")
            response = requests.post(self.api_url, headers=self.headers, json=data)
            response.raise_for_status()
            
            result = response.json()
            return result['content'][0]['text']
            
        except requests.exceptions.RequestException as e:
            print(f"{RED}Error communicating with Claude API: {e}{RESET}")
            if hasattr(e, 'response') and e.response is not None:
                print(f"Response: {e.response.text}")
            return None
    
    def interactive_mode(self):
        """Start an interactive chat session with Claude"""
        print(f"{GREEN}Claude CLI - Interactive Mode{RESET}")
        print(f"{YELLOW}Type 'exit' or 'quit' to end the session{RESET}")
        print(f"{YELLOW}Type 'clear' to clear the screen{RESET}")
        print("-" * 50)
        
        messages = []
        
        while True:
            try:
                user_input = input(f"{BOLD}You:{RESET} ").strip()
                
                if user_input.lower() in ['exit', 'quit']:
                    print(f"{GREEN}Goodbye!{RESET}")
                    break
                
                if user_input.lower() == 'clear':
                    os.system('clear' if os.name != 'nt' else 'cls')
                    continue
                
                if not user_input:
                    continue
                
                messages.append({"role": "user", "content": user_input})
                
                # Send the entire conversation history
                data = {
                    "model": "claude-3-sonnet-20240229",
                    "max_tokens": 1024,
                    "temperature": 0.7,
                    "messages": messages
                }
                
                response = requests.post(self.api_url, headers=self.headers, json=data)
                response.raise_for_status()
                
                result = response.json()
                assistant_response = result['content'][0]['text']
                
                print(f"\n{BOLD}{CYAN}Claude:{RESET} {assistant_response}\n")
                
                messages.append({"role": "assistant", "content": assistant_response})
                
            except KeyboardInterrupt:
                print(f"\n{GREEN}Goodbye!{RESET}")
                break
            except Exception as e:
                print(f"{RED}Error: {e}{RESET}")

def main():
    parser = argparse.ArgumentParser(
        description='Claude CLI - Command-line interface for Claude',
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  claude "What is the capital of France?"
  claude -i                              # Interactive mode
  claude -m claude-3-opus-20240229 "Explain quantum computing"
  claude -t 0.2 "Write a haiku about coding"
  claude --max-tokens 2048 "Write a short story"
        """
    )
    
    parser.add_argument('message', nargs='?', help='Message to send to Claude')
    parser.add_argument('-i', '--interactive', action='store_true', 
                        help='Start interactive chat mode')
    parser.add_argument('-m', '--model', default='claude-3-sonnet-20240229',
                        help='Claude model to use (default: claude-3-sonnet-20240229)')
    parser.add_argument('-t', '--temperature', type=float, default=0.7,
                        help='Temperature for response generation (0.0-1.0, default: 0.7)')
    parser.add_argument('--max-tokens', type=int, default=1024,
                        help='Maximum tokens in response (default: 1024)')
    parser.add_argument('-k', '--api-key', help='Claude API key (can also use CLAUDE_API_KEY env var)')
    
    args = parser.parse_args()
    
    # Initialize CLI
    cli = ClaudeCLI(api_key=args.api_key)
    
    if args.interactive:
        cli.interactive_mode()
    elif args.message:
        response = cli.send_message(
            args.message,
            model=args.model,
            max_tokens=args.max_tokens,
            temperature=args.temperature
        )
        if response:
            print(f"\n{BOLD}{CYAN}Claude:{RESET} {response}")
    else:
        parser.print_help()

if __name__ == '__main__':
    main()