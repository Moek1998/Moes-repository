#!/bin/bash

# Linux Setup Script for Cursor MCP Integration

echo "🐧 Setting up MCP servers for Cursor IDE on Linux..."

# Run the main setup script
./setup-mcp-servers.sh

# Copy configuration to Linux Cursor directory
CURSOR_CONFIG_DIR="$HOME/.config/Cursor/User"
mkdir -p "$CURSOR_CONFIG_DIR"

echo "📁 Copying configuration to Cursor directory..."
cp cursor-mcp-config.json "$CURSOR_CONFIG_DIR/mcp_servers.json"

echo "✅ Linux setup complete!"
echo "🔄 Please restart Cursor IDE to load the MCP servers."