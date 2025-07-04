# Claude CLI

A command-line interface for interacting with Claude AI from your terminal.

## Features

- 💬 Interactive chat mode
- 🚀 Quick one-off questions
- 🎨 Colored output for better readability
- 🔧 Configurable models and parameters
- 🌐 Works on WSL, Linux, macOS, and Windows PowerShell

## Prerequisites

- Python 3.6 or higher
- An Anthropic API key (get one at https://console.anthropic.com/)

## Installation

### For WSL/Linux/macOS

1. Clone or download this repository
2. Run the setup script:
   ```bash
   chmod +x setup_claude_wsl.sh
   ./setup_claude_wsl.sh
   ```
3. Set your API key:
   ```bash
   export CLAUDE_API_KEY='your-api-key-here'
   # Add to ~/.bashrc or ~/.zshrc to make it permanent
   echo "export CLAUDE_API_KEY='your-api-key-here'" >> ~/.bashrc
   ```
4. Reload your shell or run:
   ```bash
   source ~/.bashrc
   ```

### For Windows PowerShell

1. Clone or download this repository
2. Run the PowerShell setup script:
   ```powershell
   .\setup_claude_powershell.ps1
   ```
3. Set your API key:
   ```powershell
   $env:CLAUDE_API_KEY = 'your-api-key-here'
   # To make it permanent, add to your PowerShell profile or set as system environment variable
   ```
4. Reload your PowerShell profile:
   ```powershell
   . $PROFILE
   ```

### Manual Installation

If you prefer to install manually:

1. Make the script executable (Linux/macOS):
   ```bash
   chmod +x claude.py
   ```
2. Add the script to your PATH or create an alias
3. Install dependencies:
   ```bash
   pip install requests
   ```

## Usage

### Quick Question
```bash
claude "What is the capital of France?"
```

### Interactive Mode
```bash
claude -i
# or
claude --interactive
```

### Advanced Options
```bash
# Use a different model
claude -m claude-3-opus-20240229 "Explain quantum computing"

# Adjust temperature (0.0-1.0)
claude -t 0.2 "Write a haiku about coding"

# Set max tokens
claude --max-tokens 2048 "Write a short story about AI"

# Pass API key directly (not recommended for security)
claude -k "your-api-key" "Hello Claude"
```

### Available Models
- `claude-3-opus-20240229` (most capable)
- `claude-3-sonnet-20240229` (balanced, default)
- `claude-3-haiku-20240307` (fastest)

## Environment Variables

- `CLAUDE_API_KEY`: Your Anthropic API key (required)

## Examples

```bash
# Get help
claude --help

# Ask a simple question
claude "What are the benefits of using Python?"

# Start an interactive conversation
claude -i

# Use Claude Opus for complex tasks
claude -m claude-3-opus-20240229 "Write a Python function to calculate Fibonacci numbers"

# Get creative with high temperature
claude -t 0.9 "Write a creative story about a time-traveling programmer"

# Get focused answers with low temperature
claude -t 0.1 "List the steps to set up a Python virtual environment"
```

## Troubleshooting

### "claude: command not found"
- Make sure you've run the setup script
- Reload your shell configuration: `source ~/.bashrc` or restart your terminal
- Check if `~/.local/bin` is in your PATH: `echo $PATH`

### API Key Issues
- Ensure your API key is set: `echo $CLAUDE_API_KEY`
- Get your API key from: https://console.anthropic.com/
- Make sure the key is valid and has the necessary permissions

### Python Dependencies
- Install requests: `pip install --user requests`
- Make sure you're using Python 3.6+: `python --version`

## License

This project is provided as-is for personal use.

## Contributing

Feel free to submit issues and enhancement requests!