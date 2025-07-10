# Claude CLI Installation Guide

## Prerequisites

### System Requirements
- **Operating System**: Linux, macOS, Windows, or WSL
- **Python**: Version 3.7 or higher
- **pip**: Python package installer
- **Internet Connection**: Required for API access

### Python Installation
If Python is not installed, download it from [python.org](https://python.org)

**Linux/macOS:**
```bash
# Check if Python is installed
python3 --version

# Install Python (Ubuntu/Debian)
sudo apt update
sudo apt install python3 python3-pip

# Install Python (macOS with Homebrew)
brew install python3
```

**Windows:**
1. Download from [python.org](https://python.org)
2. Run installer with "Add to PATH" option
3. Verify installation: `python --version`

## Installation Methods

### Method 1: Automated Installation (Recommended)

#### Linux/WSL
```bash
# Clone or download the repository
git clone <repository-url>
cd claude-cli

# Run installation script
chmod +x install.sh
./install.sh
```

#### Windows (PowerShell)
```powershell
# Run PowerShell as Administrator
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser

# Navigate to project directory
cd claude-cli

# Run installation script
.\install.ps1
```

### Method 2: Manual Installation

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Copy Files**
   ```bash
   # Create installation directory
   mkdir -p ~/.local/bin
   
   # Copy main script
   cp claude.py ~/.local/bin/
   cp claude ~/.local/bin/
   chmod +x ~/.local/bin/claude
   ```

3. **Add to PATH** (if not already done)
   ```bash
   echo 'export PATH="$PATH:$HOME/.local/bin"' >> ~/.bashrc
   source ~/.bashrc
   ```

## Post-Installation Setup

### 1. Get API Key
1. Visit [Anthropic Console](https://console.anthropic.com/)
2. Create account or sign in
3. Generate API key
4. Copy the key for next step

### 2. Configure API Key

**Option A: Using CLI**
```bash
claude --setup-key YOUR_API_KEY_HERE
```

**Option B: Environment Variable**
```bash
export ANTHROPIC_API_KEY=your_api_key_here
```

**Option C: Config File**
```bash
claude --config  # Shows config file location
# Edit the file and add your API key
```

### 3. Test Installation
```bash
# Test basic functionality
claude "Hello Claude!"

# Test interactive mode
claude -i

# Show available models
claude --models
```

## Troubleshooting

### "claude: command not found"
The installation directory is not in your PATH.

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

### Python/pip not found
Install Python 3.7+ from [python.org](https://python.org) and ensure it's in your PATH.

### Permission Denied (Linux)
```bash
chmod +x install.sh
chmod +x claude
```

### PowerShell Execution Policy (Windows)
```powershell
Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser
```

## Verification

After installation, verify everything works:

```bash
# Check version and help
claude --help

# Test API connection
claude "What is 2+2?"

# Test interactive mode
claude -i
# Type: Hello Claude!
# Type: exit
```

## Uninstallation

To remove the Claude CLI:

1. **Remove from PATH** (if manually added)
2. **Delete installation files:**
   ```bash
   rm ~/.local/bin/claude
   rm ~/.local/bin/claude.py
   ```
3. **Remove configuration** (optional):
   ```bash
   rm -rf ~/.claude
   ```

## Support

For issues and support:
- Check the troubleshooting section above
- Review the main README.md
- Check API documentation at [console.anthropic.com](https://console.anthropic.com/)