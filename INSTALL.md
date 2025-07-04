# Installation Guide for MCP Servers with Cursor IDE

This guide walks you through setting up Context 7 and Toolbox MCP servers for use with Cursor IDE.

## Prerequisites

- Node.js (version 16 or higher)
- Cursor IDE
- Basic command line knowledge

## Quick Installation

### 1. Run the Setup Script

Choose the appropriate setup method for your operating system:

**All platforms (Universal):**
```bash
./setup-mcp-servers-simple.sh
```

**macOS specific:**
```bash
./config/setup-macos.sh
```

**Linux specific:**
```bash
./config/setup-linux.sh
```

**Windows specific:**
```bash
./config/setup-windows.bat
```

### 2. Configure Cursor IDE

The setup script will create the necessary MCP server files. You now need to tell Cursor IDE about them:

#### Option A: Automatic Configuration (Recommended)
If you used the platform-specific setup scripts, the configuration should be automatically copied to the correct location.

#### Option B: Manual Configuration
1. Copy `cursor-mcp-config.json` to your Cursor configuration directory:
   - **macOS**: `~/Library/Application Support/Cursor/User/mcp_servers.json`
   - **Linux**: `~/.config/Cursor/User/mcp_servers.json`
   - **Windows**: `%APPDATA%\Cursor\User\mcp_servers.json`

2. Alternatively, you can place the configuration in your project root as `.cursor-mcp.json`

### 3. Restart Cursor IDE

After copying the configuration file, restart Cursor IDE to load the MCP servers.

## Verification

### Test the MCP Servers

Run the test script to verify the servers are working:

```bash
./test-mcp-servers.sh
```

You should see output indicating both servers started and responded correctly.

### Check in Cursor IDE

1. Open Cursor IDE
2. The MCP servers should appear in the IDE's tool palette
3. You can now use the Context 7 and Toolbox tools in your conversations

## Available Tools

### Context 7 MCP Server

- **get_context**: Retrieve conversation context with configurable depth
- **set_context**: Set conversation context

### Toolbox MCP Server

- **execute_command**: Execute shell commands
- **file_operations**: Read, write, and list files
- **text_processing**: Process text (word count, case conversion, etc.)

## Troubleshooting

### Common Issues

1. **MCP servers not appearing in Cursor**
   - Verify the configuration file is in the correct location
   - Check file permissions
   - Restart Cursor IDE

2. **Permission errors**
   - Ensure setup scripts have execute permissions: `chmod +x setup-mcp-servers-simple.sh`
   - Check Node.js installation

3. **Node.js errors**
   - Verify Node.js is installed: `node --version`
   - Ensure version is 16 or higher

### Debug Mode

To debug issues, run the servers manually:

```bash
# Test Context 7 server
cd mcp-servers/context-7
node index.js

# Test Toolbox server
cd mcp-servers/toolbox
node index.js
```

The servers will start and wait for JSON-RPC messages on stdin.

## Manual Server Testing

You can test the servers manually by sending JSON-RPC requests:

### Initialize Context 7 Server
```bash
echo '{"id": 1, "method": "initialize", "params": {"protocolVersion": "2024-11-05", "capabilities": {}}}' | node mcp-servers/context-7/index.js
```

### List Available Tools
```bash
echo '{"id": 2, "method": "tools/list", "params": {}}' | node mcp-servers/context-7/index.js
```

## Configuration Details

The `cursor-mcp-config.json` file contains:

```json
{
  "mcpServers": {
    "context-7": {
      "command": "node",
      "args": ["./mcp-servers/context-7/index.js"],
      "env": {
        "NODE_ENV": "production"
      }
    },
    "toolbox": {
      "command": "node", 
      "args": ["./mcp-servers/toolbox/index.js"],
      "env": {
        "NODE_ENV": "production"
      }
    }
  }
}
```

## Next Steps

Once installed, you can:

1. Use the Context 7 server to manage conversation context
2. Use the Toolbox server to execute commands and process files
3. Extend the servers with additional functionality as needed

## Support

If you encounter issues:

1. Check the troubleshooting section above
2. Ensure all prerequisites are met
3. Review the server logs for error messages
4. Test the servers manually to isolate issues