# Cursor MCP Configuration Paths

This directory contains configuration files for different operating systems.

## Installation Instructions

### macOS
```bash
cp cursor-mcp-config.json ~/Library/Application\ Support/Cursor/User/mcp_servers.json
```

### Linux
```bash
cp cursor-mcp-config.json ~/.config/Cursor/User/mcp_servers.json
```

### Windows (PowerShell)
```powershell
Copy-Item cursor-mcp-config.json $env:APPDATA\Cursor\User\mcp_servers.json
```

## Alternative Configuration Locations

Some versions of Cursor may look for MCP configuration in different locations:

- `settings.json` in the user settings directory
- `mcp.json` in the workspace root
- Environment-specific configuration files

If the standard location doesn't work, try placing the configuration in your workspace's `.vscode/` or `.cursor/` directory.