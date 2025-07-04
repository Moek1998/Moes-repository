# Claude Code and Claude Squad

This repository contains two main components for working with Claude AI:

## Claude Code
A Python client library for interacting with the Claude AI API, providing easy-to-use methods for:
- Sending messages to Claude
- Managing conversations
- Handling API responses
- Configuration management

## Claude Squad
A team/session management system for organizing Claude interactions:
- Manage multiple Claude conversations
- Organize sessions by projects or teams
- Share and collaborate on Claude interactions
- Track conversation history

## Installation

```bash
pip install -r requirements.txt
```

## Quick Start

### Claude Code
```python
from claude_code import ClaudeClient

client = ClaudeClient(api_key="your-api-key")
response = client.send_message("Hello, Claude!")
print(response)
```

### Claude Squad
```python
from claude_squad import Squad

squad = Squad("my-project")
squad.add_session("session-1", "Planning discussion")
squad.get_sessions()
```

## CLI Usage

```bash
# Claude Code CLI
python -m claude_code --message "Hello, Claude!"

# Claude Squad CLI
python -m claude_squad --create-squad "project-name"
```

## Configuration

Create a `.env` file with your API credentials:
```
CLAUDE_API_KEY=your-api-key-here
```

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test your changes
5. Submit a pull request