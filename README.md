# Claude CLI

A command-line interface for interacting with Claude AI from Anthropic. Run `claude` from anywhere in your terminal to chat with Claude!

## Features

- 🚀 Global access from any directory
- 💬 Interactive chat mode
- 🔧 Configurable settings
- 🔑 Secure API key management
- 🖥️ Cross-platform support (Linux, WSL, Windows)
- 📝 System prompts support
- ⚡ Fast and lightweight

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

# Ask with a system prompt
claude -s "You are a helpful coding assistant" "How do I reverse a string in Python?"

# Start interactive mode
claude -i

# Show help
claude --help

# Show config file location
claude --config
```

### Interactive Mode

```bash
claude -i
```

In interactive mode, you can:
- Type messages and get responses
- Type `exit` or `quit` to leave
- Type `clear` to clear the screen
- Use Ctrl+C to exit

### Command Line Options

- `message`: Send a message to Claude (if no message provided, starts interactive mode)
- `-i, --interactive`: Start interactive mode explicitly
- `-s, --system`: Provide a system prompt
- `--setup-key`: Set up your API key
- `--config`: Show config file location
- `--help`: Show help message

## Configuration

The CLI stores configuration in `~/.claude/config.ini`:

```ini
[DEFAULT]
api_key = your_api_key_here
model = claude-3-sonnet-20240229
max_tokens = 1000
```

You can edit this file to change:
- `model`: The Claude model to use
- `max_tokens`: Maximum tokens in responses
- `api_key`: Your Anthropic API key (optional if using environment variable)

## Examples

```bash
# Simple question
claude "Explain quantum computing in simple terms"

# Coding help
claude "Write a Python function to find prime numbers"

# Creative writing
claude -s "You are a creative writer" "Write a short story about a robot learning to paint"

# Interactive coding session
claude -i
You: I need help with a React component
Claude: I'd be happy to help you with your React component! What specific functionality are you trying to implement?
You: I want to create a todo list
Claude: Great! Here's a simple todo list component...
```

## Troubleshooting

### "claude: command not found"

The installation directory is not in your PATH. Add it:

**Linux/WSL:**
```bash
echo 'export PATH="$PATH:$HOME/.local/bin"' >> ~/.bashrc
source ~/.bashrc
```

**Windows:**
Add `%USERPROFILE%\.local\bin` to your PATH environment variable.

### "No API key found"

Set up your API key:
```bash
claude --setup-key your_api_key_here
```

Or set the environment variable:
```bash
export ANTHROPIC_API_KEY=your_api_key_here
```

### Python/pip not found

Install Python 3.7+ from [python.org](https://python.org) and ensure it's in your PATH.

## Requirements

- Python 3.7 or higher
- `requests` library
- Valid Anthropic API key

## License

This project is open source and available under the MIT License.