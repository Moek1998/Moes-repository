#!/bin/bash
# Claude CLI Installation Script

set -e

echo "Installing Claude CLI..."

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

# Check if Python 3 is installed
if ! command -v python3 &> /dev/null; then
    echo -e "${RED}Error: Python 3 is required but not installed.${NC}"
    echo "Please install Python 3 and try again."
    exit 1
fi

# Check if pip is installed
if ! command -v pip3 &> /dev/null && ! command -v pip &> /dev/null; then
    echo -e "${RED}Error: pip is required but not installed.${NC}"
    echo "Please install pip and try again."
    exit 1
fi

# Install Python dependencies
echo "Installing Python dependencies..."
if command -v pip3 &> /dev/null; then
    pip3 install -r requirements.txt --user
else
    pip install -r requirements.txt --user
fi

# Create installation directory
INSTALL_DIR="$HOME/.local/bin"
mkdir -p "$INSTALL_DIR"

# Copy files to installation directory
echo "Installing Claude CLI to $INSTALL_DIR..."
cp claude.py "$INSTALL_DIR/"
cp claude "$INSTALL_DIR/"
chmod +x "$INSTALL_DIR/claude"

# Check if the install directory is in PATH
if [[ ":$PATH:" != *":$INSTALL_DIR:"* ]]; then
    echo -e "${YELLOW}Warning: $INSTALL_DIR is not in your PATH.${NC}"
    echo "To make the 'claude' command available globally, add this line to your ~/.bashrc or ~/.zshrc:"
    echo "export PATH=\"\$PATH:$INSTALL_DIR\""
    echo ""
    echo "Or run this command now:"
    echo "echo 'export PATH=\"\$PATH:$INSTALL_DIR\"' >> ~/.bashrc && source ~/.bashrc"
    echo ""
fi

echo -e "${GREEN}Installation completed successfully!${NC}"
echo ""
echo "🚀 CLAUDE CLI READY!"
echo "=" * 30
echo ""
echo "📋 GETTING STARTED:"
echo "1. Learn about Claude access types:"
echo "   claude --info"
echo ""
echo "2. Set up your Anthropic API key:"
echo "   claude --setup-key YOUR_API_KEY"
echo "   OR"
echo "   export ANTHROPIC_API_KEY=your_api_key_here"
echo "   Get key: https://console.anthropic.com/"
echo ""
echo "3. Try the new features:"
echo "   claude 'Hello Claude!'                    # Quick question"
echo "   claude -i                                # Interactive mode"
echo "   claude --squad                           # Team collaboration"
echo "   claude --code                            # Coding assistant"
echo "   claude --models                          # Show available models"
echo ""
echo "💡 PRO TIP: This CLI uses API access (pay-per-use)"
echo "   For Claude Pro features like real Squad & Code,"
echo "   visit: https://claude.ai/ ($20/month)"
echo ""
echo "📚 For help: claude --help"