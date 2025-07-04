# MCP Servers for Cursor IDE

This repository contains the setup and configuration for integrating Model Context Protocol (MCP) servers with Cursor IDE, specifically Context 7 and Toolbox MCP servers.

## Overview

Model Context Protocol (MCP) allows AI assistants to access external tools and resources. This setup provides:

- **Context 7 MCP Server**: Manages conversation context with configurable depth
- **Toolbox MCP Server**: Provides various utility tools for development

## Quick Start

1. **Run the setup script**:
   ```bash
   ./setup-mcp-servers.sh
   ```

2. **Configure Cursor IDE**:
   - Copy `cursor-mcp-config.json` to your Cursor configuration directory
   - The exact location depends on your OS:
     - **macOS**: `~/Library/Application Support/Cursor/User/`
     - **Linux**: `~/.config/Cursor/User/`
     - **Windows**: `%APPDATA%\Cursor\User\`

3. **Restart Cursor IDE** to load the MCP servers

## MCP Servers

### Context 7 MCP Server

The Context 7 server provides context management capabilities:

**Available Tools:**
- `get_context`: Retrieve conversation context with configurable depth
- `set_context`: Set conversation context

**Usage Example:**
```json
{
  "tool": "get_context",
  "arguments": {
    "depth": 7
  }
}
```

### Toolbox MCP Server

The Toolbox server provides various utility tools:

**Available Tools:**
- `execute_command`: Execute shell commands
- `file_operations`: Perform file operations (read, write, list)
- `text_processing`: Process text (word count, line count, case conversion)

**Usage Examples:**
```json
{
  "tool": "execute_command",
  "arguments": {
    "command": "ls -la"
  }
}
```

```json
{
  "tool": "file_operations",
  "arguments": {
    "operation": "read",
    "path": "./example.txt"
  }
}
```

```json
{
  "tool": "text_processing",
  "arguments": {
    "operation": "count_words",
    "text": "Hello world example text"
  }
}
```

## Configuration

### cursor-mcp-config.json

The main configuration file for Cursor IDE:

```json
{
  "mcpServers": {
    "context-7": {
      "command": "node",
      "args": ["./mcp-servers/context-7/dist/index.js"],
      "env": {
        "NODE_ENV": "production"
      }
    },
    "toolbox": {
      "command": "node", 
      "args": ["./mcp-servers/toolbox/dist/index.js"],
      "env": {
        "NODE_ENV": "production"
      }
    }
  }
}
```

## Directory Structure

```
├── cursor-mcp-config.json      # Cursor IDE MCP configuration
├── setup-mcp-servers.sh        # Setup script for MCP servers
├── README.md                   # This documentation
└── mcp-servers/                # MCP servers directory (created by setup)
    ├── context-7/              # Context 7 MCP server
    │   ├── src/
    │   ├── dist/
    │   └── package.json
    └── toolbox/                # Toolbox MCP server
        ├── src/
        ├── dist/
        └── package.json
```

## Requirements

- Node.js (version 18 or higher)
- npm
- Cursor IDE

## Development

### Building the MCP Servers

Each MCP server can be built individually:

```bash
# Build Context 7 server
cd mcp-servers/context-7
npm run build

# Build Toolbox server
cd mcp-servers/toolbox
npm run build
```

### Running MCP Servers Standalone

For testing purposes, you can run the MCP servers directly:

```bash
# Run Context 7 server
cd mcp-servers/context-7
npm start

# Run Toolbox server
cd mcp-servers/toolbox
npm start
```

## Troubleshooting

### Common Issues

1. **MCP servers not appearing in Cursor**:
   - Ensure the configuration file is in the correct location
   - Check that the paths in the configuration are correct
   - Restart Cursor IDE

2. **Build errors**:
   - Ensure Node.js and npm are properly installed
   - Run `npm install` in each server directory
   - Check for TypeScript compilation errors

3. **Permission errors**:
   - Ensure the setup script has execute permissions: `chmod +x setup-mcp-servers.sh`
   - Check file and directory permissions

### Logs

MCP servers output logs to stderr. To debug issues:

1. Check Cursor IDE's developer console
2. Run the MCP servers standalone to see error messages
3. Verify the configuration file syntax

## Contributing

To add new MCP servers:

1. Create a new directory in `mcp-servers/`
2. Follow the existing structure with TypeScript and MCP SDK
3. Add the server configuration to `cursor-mcp-config.json`
4. Update the setup script to include the new server

## License

This project is open source and available under the MIT License.