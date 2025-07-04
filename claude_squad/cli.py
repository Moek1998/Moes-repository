"""
Command-line interface for Claude Squad
"""

import click
import json
import os
from tabulate import tabulate
from .squad import Squad
from .exceptions import SquadError


@click.group()
@click.version_option()
def cli():
    """Claude Squad CLI - Manage Claude AI sessions and teams"""
    pass


@cli.command()
@click.argument('squad_name')
@click.option('--description', '-d', help='Squad description')
def create(squad_name, description):
    """Create a new squad"""
    try:
        squad = Squad(squad_name)
        if description:
            squad.metadata['description'] = description
            squad._save_squad_config()
        
        click.echo(f"Created squad: {squad_name}")
        
    except SquadError as e:
        click.echo(f"Error: {e}", err=True)
        exit(1)


@cli.command()
def list():
    """List all squads"""
    try:
        squads_dir = "squads"
        if not os.path.exists(squads_dir):
            click.echo("No squads found. Create one with 'claude-squad create <name>'")
            return
        
        squads = []
        for squad_name in os.listdir(squads_dir):
            squad_path = os.path.join(squads_dir, squad_name)
            if os.path.isdir(squad_path):
                try:
                    squad = Squad(squad_name)
                    description = squad.metadata.get('description', '')
                    squads.append([
                        squad_name,
                        len(squad.sessions),
                        description,
                        squad.created_at[:10]  # Just the date part
                    ])
                except Exception:
                    squads.append([squad_name, "Error", "Failed to load", "Unknown"])
        
        if squads:
            headers = ["Squad Name", "Sessions", "Description", "Created"]
            click.echo(tabulate(squads, headers=headers, tablefmt="grid"))
        else:
            click.echo("No squads found.")
            
    except Exception as e:
        click.echo(f"Error: {e}", err=True)


@cli.command()
@click.argument('squad_name')
@click.argument('session_id')
@click.argument('session_name')
@click.option('--description', '-d', help='Session description')
def add_session(squad_name, session_id, session_name, description):
    """Add a new session to a squad"""
    try:
        squad = Squad(squad_name)
        session = squad.add_session(session_id, session_name, description or "")
        click.echo(f"Added session '{session_id}' to squad '{squad_name}'")
        
    except SquadError as e:
        click.echo(f"Error: {e}", err=True)
        exit(1)


@cli.command()
@click.argument('squad_name')
def sessions(squad_name):
    """List sessions in a squad"""
    try:
        squad = Squad(squad_name)
        session_list = squad.list_sessions()
        
        if session_list:
            table_data = []
            for session in session_list:
                table_data.append([
                    session['session_id'],
                    session['name'],
                    session['message_count'],
                    session['description'][:50] + ('...' if len(session['description']) > 50 else ''),
                    session['created_at'][:10]
                ])
            
            headers = ["Session ID", "Name", "Messages", "Description", "Created"]
            click.echo(f"Sessions in squad '{squad_name}':")
            click.echo(tabulate(table_data, headers=headers, tablefmt="grid"))
        else:
            click.echo(f"No sessions found in squad '{squad_name}'")
            
    except SquadError as e:
        click.echo(f"Error: {e}", err=True)
        exit(1)


@cli.command()
@click.argument('squad_name')
@click.argument('session_id')
def show_session(squad_name, session_id):
    """Show details of a specific session"""
    try:
        squad = Squad(squad_name)
        session = squad.get_session(session_id)
        
        click.echo(f"Session: {session.name} ({session.session_id})")
        click.echo(f"Description: {session.description}")
        click.echo(f"Created: {session.created_at}")
        click.echo(f"Updated: {session.updated_at}")
        click.echo(f"Messages: {len(session.messages)}")
        click.echo("=" * 50)
        
        for i, msg in enumerate(session.messages, 1):
            role = msg['role'].capitalize()
            content = msg['content']
            timestamp = msg['timestamp'][:19].replace('T', ' ')  # Format timestamp
            
            click.echo(f"{i}. {role} ({timestamp}):")
            click.echo(f"   {content}")
            click.echo("-" * 30)
            
    except SquadError as e:
        click.echo(f"Error: {e}", err=True)
        exit(1)


@cli.command()
@click.argument('squad_name')
@click.argument('session_id')
@click.argument('role')
@click.argument('content')
def add_message(squad_name, session_id, role, content):
    """Add a message to a session"""
    try:
        squad = Squad(squad_name)
        session = squad.get_session(session_id)
        session.add_message(role, content)
        squad.save_session(session_id)
        
        click.echo(f"Added {role} message to session '{session_id}'")
        
    except SquadError as e:
        click.echo(f"Error: {e}", err=True)
        exit(1)


@cli.command()
@click.argument('squad_name')
@click.argument('session_id')
def remove_session(squad_name, session_id):
    """Remove a session from a squad"""
    try:
        squad = Squad(squad_name)
        
        # Confirm deletion
        if not click.confirm(f"Are you sure you want to remove session '{session_id}'?"):
            click.echo("Operation cancelled.")
            return
            
        squad.remove_session(session_id)
        click.echo(f"Removed session '{session_id}' from squad '{squad_name}'")
        
    except SquadError as e:
        click.echo(f"Error: {e}", err=True)
        exit(1)


@cli.command()
@click.argument('squad_name')
@click.argument('export_path')
def export(squad_name, export_path):
    """Export a squad to a file"""
    try:
        squad = Squad(squad_name)
        squad.export_squad(export_path)
        click.echo(f"Exported squad '{squad_name}' to {export_path}")
        
    except SquadError as e:
        click.echo(f"Error: {e}", err=True)
        exit(1)


@cli.command()
@click.argument('import_path')
@click.option('--name', help='New squad name (if different from original)')
def import_squad(import_path, name):
    """Import a squad from a file"""
    try:
        squad = Squad.import_squad(import_path, name)
        click.echo(f"Imported squad '{squad.squad_name}'")
        
    except SquadError as e:
        click.echo(f"Error: {e}", err=True)
        exit(1)


def main():
    """Main entry point for the CLI"""
    cli()


if __name__ == '__main__':
    main()