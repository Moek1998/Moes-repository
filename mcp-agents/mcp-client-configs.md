# MCP Client Configuration Examples

This document provides configuration examples for connecting various MCP clients to your Context7 servers.

## Server Details

- **Coding Agent 1**: Port 3001
- **Coding Agent 2**: Port 3002  
- **Coding Agent 3**: Port 3003

## Starting the Servers

Use the control script to manage servers:

```bash
# Start all servers
/workspace/mcp-agents/context7-control.sh start all

# Start a specific server
/workspace/mcp-agents/context7-control.sh start 1

# Check status
/workspace/mcp-agents/context7-control.sh status

# Stop all servers
/workspace/mcp-agents/context7-control.sh stop all
```

## Client Configurations

### Cursor Configuration

Add to `~/.cursor/mcp.json`:

```json
{
  "mcpServers": {
    "context7-agent1": {
      "url": "http://localhost:3001/mcp"
    },
    "context7-agent2": {
      "url": "http://localhost:3002/mcp"
    },
    "context7-agent3": {
      "url": "http://localhost:3003/mcp"
    }
  }
}
```

Or for local stdio connection:

```json
{
  "mcpServers": {
    "context7-agent1": {
      "command": "node",
      "args": ["/workspace/mcp-agents/coding-agent-1/context7/dist/index.js"]
    },
    "context7-agent2": {
      "command": "node",
      "args": ["/workspace/mcp-agents/coding-agent-2/context7/dist/index.js"]
    },
    "context7-agent3": {
      "command": "node",
      "args": ["/workspace/mcp-agents/coding-agent-3/context7/dist/index.js"]
    }
  }
}
```

### Claude Desktop Configuration

Add to Claude Desktop's `claude_desktop_config.json`:

```json
{
  "mcpServers": {
    "Context7-Agent1": {
      "command": "node",
      "args": ["/workspace/mcp-agents/coding-agent-1/context7/dist/index.js"]
    },
    "Context7-Agent2": {
      "command": "node",
      "args": ["/workspace/mcp-agents/coding-agent-2/context7/dist/index.js"]
    },
    "Context7-Agent3": {
      "command": "node",
      "args": ["/workspace/mcp-agents/coding-agent-3/context7/dist/index.js"]
    }
  }
}
```

### VS Code Configuration

Add to VS Code settings:

```json
{
  "mcp": {
    "servers": {
      "context7-agent1": {
        "type": "http",
        "url": "http://localhost:3001/mcp"
      },
      "context7-agent2": {
        "type": "http",
        "url": "http://localhost:3002/mcp"
      },
      "context7-agent3": {
        "type": "http",
        "url": "http://localhost:3003/mcp"
      }
    }
  }
}
```

### Windsurf Configuration

For Windsurf MCP config:

```json
{
  "mcpServers": {
    "context7-agent1": {
      "serverUrl": "http://localhost:3001/sse"
    },
    "context7-agent2": {
      "serverUrl": "http://localhost:3002/sse"
    },
    "context7-agent3": {
      "serverUrl": "http://localhost:3003/sse"
    }
  }
}
```

## Using Context7

Once configured, you can use Context7 in your prompts by adding `use context7` to your queries:

```
Create a React component with TypeScript that fetches data from an API. use context7
```

```
Show me how to configure Next.js middleware for authentication. use context7
```

## Troubleshooting

1. **Check if servers are running:**
   ```bash
   /workspace/mcp-agents/context7-control.sh status
   ```

2. **View server logs:**
   ```bash
   tail -f /workspace/mcp-agents/coding-agent-1/context7.log
   ```

3. **Test server connectivity:**
   ```bash
   /workspace/mcp-agents/context7-control.sh test
   ```

4. **Restart servers:**
   ```bash
   /workspace/mcp-agents/context7-control.sh restart all
   ```