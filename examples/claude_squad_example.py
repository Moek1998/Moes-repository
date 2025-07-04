#!/usr/bin/env python3
"""
Example script demonstrating Claude Squad usage
"""

from claude_squad import Squad
from claude_squad.exceptions import SquadError

def main():
    """Example usage of Claude Squad"""
    
    try:
        # Create a new squad
        print("Creating a new squad...")
        squad = Squad("example-project")
        squad.metadata['description'] = "Example project for testing Claude Squad"
        
        # Add sessions
        print("\nAdding sessions to the squad...")
        session1 = squad.add_session("planning", "Project Planning", "Planning session for the project")
        session2 = squad.add_session("development", "Development Discussion", "Technical development discussions")
        session3 = squad.add_session("testing", "Testing Strategy", "Testing and QA discussions")
        
        # Add some messages to sessions
        print("\nAdding messages to sessions...")
        session1.add_message("user", "Let's discuss the project timeline")
        session1.add_message("assistant", "I'd be happy to help with project planning. What's the scope of your project?")
        session1.add_message("user", "We need to build a web application with user authentication")
        
        session2.add_message("user", "What technology stack should we use?")
        session2.add_message("assistant", "For a web application with authentication, I'd recommend...")
        
        # Save sessions
        print("\nSaving sessions...")
        squad.save_session("planning")
        squad.save_session("development")
        squad.save_session("testing")
        
        # List sessions
        print("\nListing sessions in the squad:")
        sessions = squad.list_sessions()
        for session in sessions:
            print(f"- {session['session_id']}: {session['name']} ({session['message_count']} messages)")
        
        # Show session details
        print("\nShowing details of planning session:")
        planning_session = squad.get_session("planning")
        print(f"Session: {planning_session.name}")
        print(f"Description: {planning_session.description}")
        print(f"Messages: {len(planning_session.messages)}")
        
        for i, msg in enumerate(planning_session.messages, 1):
            print(f"{i}. {msg['role'].capitalize()}: {msg['content'][:100]}...")
        
        # Export squad
        print("\nExporting squad...")
        squad.export_squad("example_squad_export.json")
        print("Squad exported to example_squad_export.json")
        
        # Demonstrate importing
        print("\nImporting squad with new name...")
        imported_squad = Squad.import_squad("example_squad_export.json", "imported-example")
        print(f"Imported squad '{imported_squad.squad_name}' with {len(imported_squad.sessions)} sessions")
        
    except SquadError as e:
        print(f"Squad Error: {e}")
    except Exception as e:
        print(f"Unexpected error: {e}")

if __name__ == "__main__":
    main()