# Claude CLI

A command-line interface for interacting with Claude AI from Anthropic. Run `claude` from anywhere in your terminal to chat with Claude! ✨

## 🎯 Claude Pro vs API Access

**Important:** This CLI uses **API access** which is separate from Claude Pro subscriptions:

- **Claude Pro ($20/month)**: Web interface with Squad, Code, priority access at [claude.ai](https://claude.ai)
- **API Access (Pay-per-use)**: For developers, integrations, and this CLI tool
- **This CLI**: Uses API access but simulates Pro features like Squad and Code modes

## Features

- 🚀 Global access from any directory
- 💬 Enhanced interactive chat mode with conversation history
- 👥 **Claude Squad Simulator** - Team collaboration features
- 💻 **Claude Code Simulator** - Advanced coding assistance
- 🤖 Multiple Claude model support (3.5 Sonnet, Opus, Haiku, etc.)
- 🔧 Configurable settings (model, temperature, tokens)
- 🔑 Secure API key management
- 🖥️ Cross-platform support (Linux, WSL, Windows)
- 📝 System prompts support
- ⚡ Fast and lightweight
- 🔌 MCP (Model Context Protocol) server support

## Installation

### Linux / WSL

1. Clone or download this repository
2. Run the installation script:
   ```bash
   chmod +x install.sh
   ./install.sh
   ```
3. If the installer warns about PATH, add the install directory to your PATH:
   ```bash
   echo 'export PATH="$PATH:$HOME/.local/bin"' >> ~/.bashrc
   source ~/.bashrc
   ```

### Windows (PowerShell)

1. Clone or download this repository
2. Run PowerShell as Administrator and execute:
   ```powershell
   Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
   .\install.ps1
   ```
3. If needed, add the install directory to your PATH environment variable

### Manual Installation

1. Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Copy the files to a directory in your PATH
3. Make the script executable (Linux/WSL):
   ```bash
   chmod +x claude
   ```

## Setup

1. Get your Anthropic API key from [https://console.anthropic.com/](https://console.anthropic.com/)

2. Set up your API key (choose one method):

   **Method 1: Using the CLI**
   ```bash
   claude --setup-key your_api_key_here
   ```

   **Method 2: Environment variable**
   ```bash
   export ANTHROPIC_API_KEY=your_api_key_here
   ```

   **Method 3: Config file**
   ```bash
   claude --config  # Shows config file location
   # Edit the config file and add your API key
   ```

## Usage

### Quick Commands

```bash
# Ask a single question
claude "What is the capital of France?"

# Use a specific model
claude -m claude-3-opus-20240229 "Explain quantum computing"

# Ask with a system prompt
claude -s "You are a helpful coding assistant" "How do I reverse a string in Python?"

# Interactive chat mode
claude -i

# Claude Squad mode (team collaboration)
claude --squad

# Claude Code mode (advanced coding)
claude --code

# Show available models
claude --models

# Configure settings
claude --config
```

### Interactive Mode

Start an interactive conversation with Claude:

```bash
claude -i
```

In interactive mode:
- Type your messages and press Enter
- Use `/exit` or `/quit` to leave
- Use `/clear` to clear conversation history
- Use `/save filename` to save conversation
- Use `/load filename` to load a previous conversation
- Use `/model model-name` to switch models mid-conversation
- Use `/system "prompt"` to set a system prompt
- Use `/squad` to switch to Squad mode
- Use `/code` to switch to Code mode

### Claude Squad Mode

Experience team collaboration features:

```bash
claude --squad
```

Squad mode provides:
- Multiple AI perspectives on problems
- Collaborative brainstorming
- Role-based responses (researcher, analyst, creative, etc.)
- Team decision-making simulation

### Claude Code Mode

Advanced coding assistance:

```bash
claude --code
```

Code mode offers:
- Enhanced code analysis and generation
- Project-aware suggestions
- Code review and optimization
- Multi-language support
- Architecture recommendations

### Configuration

View and modify settings:

```bash
claude --config
```

Available settings:
- `model`: Default Claude model to use
- `temperature`: Response creativity (0.0-1.0)
- `max_tokens`: Maximum response length
- `api_key`: Your Anthropic API key
- `system_prompt`: Default system prompt

### Models

View available models:

```bash
claude --models
```

Supported models:
- `claude-3-5-sonnet-20241022` (Latest, most capable)
- `claude-3-5-sonnet-20240620` (Previous version)
- `claude-3-opus-20240229` (Most powerful, slower)
- `claude-3-sonnet-20240229` (Balanced)
- `claude-3-haiku-20240307` (Fastest, most economical)

## Advanced Features

### System Prompts

Customize Claude's behavior with system prompts:

```bash
# Use a predefined system prompt
claude -s "You are a helpful coding assistant specializing in Python" "How do I optimize this function?"

# Set a persistent system prompt
claude --config
# Then edit the system_prompt setting
```

### Conversation Management

Save and load conversations:

```bash
# In interactive mode
/save my-conversation
/load my-conversation

# Or specify full paths
/save /path/to/conversations/project-discussion
```

### Model Switching

Switch models during conversation:

```bash
# In interactive mode
/model claude-3-opus-20240229
```

### Temperature Control

Adjust response creativity:

```bash
claude -t 0.7 "Write a creative story about AI"  # More creative
claude -t 0.1 "What is 2+2?"                     # More factual
```

## Examples

### Basic Usage
```bash
# Simple question
claude "Explain machine learning in simple terms"

# Code help
claude "How do I read a CSV file in Python?"

# Creative writing
claude -t 0.8 "Write a short poem about programming"
```

### Interactive Sessions
```bash
# Start interactive mode
claude -i

# Example conversation:
> Hello! I'm working on a Python project and need help with error handling.
> /system "You are an expert Python developer focused on best practices"
> Can you show me the best way to handle file operations with proper exception handling?
> /save python-error-handling
> /exit
```

### Squad Collaboration
```bash
# Start Squad mode
claude --squad

# Example usage:
> I need to design a new mobile app. Can the team help brainstorm features?
# Squad will provide multiple perspectives: UX designer, developer, product manager, etc.
```

### Code Analysis
```bash
# Start Code mode
claude --code

# Example usage:
> Can you review this Python function and suggest improvements?
> [paste your code]
# Code mode provides detailed analysis, optimization suggestions, and best practices
```

## Troubleshooting

### Common Issues

1. **API Key Issues**
   ```bash
   # Verify your API key is set
   claude --config
   
   # Re-set your API key
   claude --setup-key your_new_api_key
   ```

2. **Permission Errors (Linux/WSL)**
   ```bash
   # Make sure the script is executable
   chmod +x ~/.local/bin/claude
   
   # Check if the directory is in PATH
   echo $PATH | grep -o ~/.local/bin
   ```

3. **Python Dependencies**
   ```bash
   # Reinstall dependencies
   pip install -r requirements.txt --upgrade
   ```

4. **Rate Limiting**
   - The CLI respects Anthropic's rate limits
   - If you encounter rate limit errors, wait a moment before retrying
   - Consider using a less powerful model (like Haiku) for simple queries

### Error Messages

- **"API key not found"**: Set your API key using one of the setup methods
- **"Invalid model"**: Use `claude --models` to see available models
- **"Rate limit exceeded"**: Wait and retry, or check your API usage
- **"Network error"**: Check your internet connection

## Development

### Project Structure
```
claude-cli/
├── src/
│   ├── claude.py          # Main CLI script
│   └── requirements.txt   # Python dependencies
├── tools/
│   └── claude            # Executable wrapper
├── scripts/
│   └── scripts.zip       # Installation scripts
├── .claude/
│   └── CLAUDE.md         # Documentation
└── README.md
```

### Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

### Requirements

- Python 3.7 or higher
- `anthropic` library (for API access)
- `requests` library
- Valid Anthropic API key

### Python/pip not found

Install Python 3.7+ from [python.org](https://python.org) and ensure it's in your PATH.

## Running Tests

To run the unit tests, run:
```bash
python -m unittest discover tests
```

## Requirements

- Python 3.7+
- `anthropic` library (for API access)
- `requests` library
- Valid Anthropic API key

## License

This project is open source and available under the MIT License.
