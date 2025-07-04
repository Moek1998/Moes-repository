"""
Command-line interface for Claude Code
"""

import click
import json
import os
from .client import ClaudeClient
from .exceptions import ClaudeError


@click.group()
@click.version_option()
def cli():
    """Claude Code CLI - Interact with Claude AI from the command line"""
    pass


@cli.command()
@click.option('--message', '-m', required=True, help='Message to send to Claude')
@click.option('--system-prompt', '-s', help='System prompt for Claude')
@click.option('--api-key', '-k', help='Claude API key (or set CLAUDE_API_KEY env var)')
@click.option('--save', help='Save conversation to file')
@click.option('--load', help='Load conversation from file')
def chat(message, system_prompt, api_key, save, load):
    """Send a message to Claude"""
    try:
        client = ClaudeClient(api_key=api_key)
        
        # Load conversation if specified
        if load and os.path.exists(load):
            client.load_conversation(load)
            click.echo(f"Loaded conversation from {load}")
        
        # Send message
        response = client.send_message(message, system_prompt)
        
        # Display response
        click.echo(f"\nClaude: {response}")
        
        # Save conversation if specified
        if save:
            client.save_conversation(save)
            click.echo(f"\nConversation saved to {save}")
            
    except ClaudeError as e:
        click.echo(f"Error: {e}", err=True)
        exit(1)


@cli.command()
@click.option('--file', '-f', required=True, help='Conversation file to display')
def history(file):
    """Display conversation history from a file"""
    try:
        if not os.path.exists(file):
            click.echo(f"File not found: {file}", err=True)
            return
            
        with open(file, 'r', encoding='utf-8') as f:
            conversation = json.load(f)
            
        click.echo(f"Conversation history from {file}:")
        click.echo("=" * 50)
        
        for msg in conversation:
            role = msg['role'].capitalize()
            content = msg['content']
            click.echo(f"{role}: {content}")
            click.echo("-" * 30)
            
    except Exception as e:
        click.echo(f"Error reading history: {e}", err=True)


@cli.command()
def interactive():
    """Start an interactive chat session with Claude"""
    try:
        client = ClaudeClient()
        click.echo("Claude Code Interactive Chat")
        click.echo("Type 'quit' or 'exit' to end the session")
        click.echo("Type 'clear' to clear conversation history")
        click.echo("Type 'save <filename>' to save conversation")
        click.echo("=" * 50)
        
        while True:
            try:
                user_input = input("\nYou: ").strip()
                
                if user_input.lower() in ['quit', 'exit']:
                    click.echo("Goodbye!")
                    break
                elif user_input.lower() == 'clear':
                    client.clear_history()
                    click.echo("Conversation history cleared.")
                    continue
                elif user_input.lower().startswith('save '):
                    filename = user_input[5:].strip()
                    if filename:
                        client.save_conversation(filename)
                        click.echo(f"Conversation saved to {filename}")
                    else:
                        click.echo("Please provide a filename.")
                    continue
                elif not user_input:
                    continue
                
                response = client.send_message(user_input)
                click.echo(f"Claude: {response}")
                
            except KeyboardInterrupt:
                click.echo("\nGoodbye!")
                break
                
    except ClaudeError as e:
        click.echo(f"Error: {e}", err=True)
        exit(1)


def main():
    """Main entry point for the CLI"""
    cli()


if __name__ == '__main__':
    main()