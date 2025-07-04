@echo off

REM Windows Setup Script for Cursor MCP Integration

echo 🪟 Setting up MCP servers for Cursor IDE on Windows...

REM Run the main setup script (assuming WSL or Git Bash)
bash setup-mcp-servers.sh

REM Copy configuration to Windows Cursor directory
set CURSOR_CONFIG_DIR=%APPDATA%\Cursor\User
if not exist "%CURSOR_CONFIG_DIR%" mkdir "%CURSOR_CONFIG_DIR%"

echo 📁 Copying configuration to Cursor directory...
copy cursor-mcp-config.json "%CURSOR_CONFIG_DIR%\mcp_servers.json"

echo ✅ Windows setup complete!
echo 🔄 Please restart Cursor IDE to load the MCP servers.

pause