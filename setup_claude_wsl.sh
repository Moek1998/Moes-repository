#!/bin/bash

# Setup script for Claude CLI on WSL/Linux

echo "Setting up Claude CLI for WSL/Linux..."

# Get the directory where this script is located
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Make the Python script executable
chmod +x "$SCRIPT_DIR/claude.py"

# Create ~/.local/bin if it doesn't exist
mkdir -p ~/.local/bin

# Create a symlink in ~/.local/bin
ln -sf "$SCRIPT_DIR/claude.py" ~/.local/bin/claude

# Check if ~/.local/bin is in PATH
if [[ ":$PATH:" != *":$HOME/.local/bin:"* ]]; then
    echo "Adding ~/.local/bin to PATH..."
    
    # Determine which shell config file to use
    if [ -f ~/.bashrc ]; then
        SHELL_CONFIG=~/.bashrc
    elif [ -f ~/.zshrc ]; then
        SHELL_CONFIG=~/.zshrc
    else
        SHELL_CONFIG=~/.profile
    fi
    
    # Add to PATH
    echo '' >> "$SHELL_CONFIG"
    echo '# Added by Claude CLI setup' >> "$SHELL_CONFIG"
    echo 'export PATH="$HOME/.local/bin:$PATH"' >> "$SHELL_CONFIG"
    
    echo "Added ~/.local/bin to PATH in $SHELL_CONFIG"
    echo "Please run: source $SHELL_CONFIG"
    echo "Or restart your terminal for changes to take effect"
fi

# Install Python dependencies
echo "Installing Python dependencies..."
# Try different methods to install requests
if command -v pipx &> /dev/null; then
    echo "Using pipx is not suitable for this use case..."
fi

# Try with --break-system-packages flag (for newer Python versions)
if pip3 install --user --break-system-packages requests 2>/dev/null; then
    echo "Installed requests successfully"
elif pip3 install --user requests 2>/dev/null; then
    echo "Installed requests successfully"
else
    echo "Warning: Could not install requests automatically"
    echo "You may need to install it manually:"
    echo "  sudo apt install python3-requests"
    echo "  OR"
    echo "  pip3 install --user --break-system-packages requests"
fi

echo ""
echo "Claude CLI setup complete!"
echo ""
echo "Next steps:"
echo "1. Set your Claude API key:"
echo "   export CLAUDE_API_KEY='your-api-key-here'"
echo "   (Add this to your shell config file to make it permanent)"
echo ""
echo "2. If claude command is not found, run:"
echo "   source ~/.bashrc  (or source ~/.zshrc)"
echo ""
echo "3. Test the installation:"
echo "   claude --help"
echo ""
echo "Get your API key from: https://console.anthropic.com/"