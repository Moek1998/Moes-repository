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

# Start interactive mode
claude -i

# Claude Squad simulation (team collaboration)
claude --squad

# Claude Code simulation (coding assistant)
claude --code

# Show available models
claude --models

# Show Claude subscription info
claude --info

# Show config and help
claude --config
claude --help
```

### 🎯 Special Modes

#### Claude Squad Simulator
```bash
claude --squad
```
Simulates Claude Pro's Squad features:
- Team collaboration interface
- Shared conversation history
- Enhanced context management
- Multiple AI personas

#### Claude Code Simulator
```bash
claude --code
```
Simulates Claude Pro's Code features:
- Expert programming assistant
- Code review and optimization
- Multi-language support
- Best practices guidance

### Interactive Mode

```bash
claude -i
```

Enhanced interactive features:
- Type messages and get responses
- `exit` or `quit` to leave
- `clear` to clear screen and history
- `help` for available commands
- `models` to show available models
- `info` for subscription information
- `model <name>` to switch models
- Use Ctrl+C to exit

### Command Line Options

- `message`: Send a message to Claude (if no message provided, starts interactive mode)
- `-i, --interactive`: Start interactive mode explicitly
- `-s, --system`: Provide a system prompt
- `-m, --model`: Specify Claude model to use
- `--squad`: Start Squad simulation mode
- `--code`: Start Code simulation mode
- `--models`: Show available models
- `--info`: Show Claude subscription information
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

## 🤖 Available Models

This CLI supports all Claude models:

| Model | Description | Best For |
|-------|-------------|----------|
| `claude-3-5-sonnet-20241022` | Latest & most capable | General use, coding, analysis |
| `claude-3-opus-20240229` | Most powerful reasoning | Complex tasks, research |
| `claude-3-sonnet-20240229` | Balanced performance | Most applications |
| `claude-3-haiku-20240307` | Fastest & cheapest | Quick responses, high volume |
| `claude-2.1` | Legacy model | Established workflows |

## 🎯 Understanding Claude Access Types

| Access Type | Cost | What You Get | How to Access |
|-------------|------|--------------|---------------|
| **Claude Free** | Free | Limited daily usage | [claude.ai](https://claude.ai) |
| **Claude Pro** | $20/month | 5x usage, Squad, Code, priority | [claude.ai](https://claude.ai) |
| **Claude Team** | $25/user/month | Team features, admin tools | Contact Anthropic |
| **Claude Enterprise** | Custom | SSO, security, custom training | Contact Anthropic |
| **API Access** | Pay-per-use | Developer integrations, this CLI | [console.anthropic.com](https://console.anthropic.com) |

## Examples

```bash
# Simple question
claude "Explain quantum computing in simple terms"

# Use the most powerful model
claude -m claude-3-opus-20240229 "Analyze this complex dataset"

# Coding help with Code simulator
claude --code
[Code] You: Write a Python function to find prime numbers
[Code] Claude: Here's an efficient prime number finder using the Sieve of Eratosthenes...

# Team collaboration with Squad simulator
claude --squad
[Squad] You: Help me plan a project roadmap
[Squad] Claude: I'll help you create a comprehensive project roadmap...

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

## Running Tests

To run the unit tests, run:
```bash
python -m unittest discover tests
```

## Requirements

- Python 3.7 or higher
- `requests` library
- Valid Anthropic API key

## License

This project is open source and available under the MIT License.