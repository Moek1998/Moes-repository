#!/bin/bash

# Start Context7 MCP Server for Coding Agent 2
echo "Starting Context7 MCP Server for Coding Agent 2..."

cd "$(dirname "$0")/context7"

# Run the server with stdio transport (default for local MCP)
# You can also use --transport http for HTTP transport
node dist/index.js

# Alternative commands:
# For HTTP transport on a specific port:
# node dist/index.js --transport http --port 3002
# 
# Using bun:
# bun dist/index.js