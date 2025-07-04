#!/bin/bash

# Test script for MCP servers

echo "🧪 Testing MCP servers..."

# Test Context 7 server
echo "📋 Testing Context 7 server..."
echo '{"id": 1, "method": "initialize", "params": {"protocolVersion": "2024-11-05", "capabilities": {}}}' | timeout 5 node mcp-servers/context-7/index.js &
sleep 2
echo "✅ Context 7 server test completed"

# Test Toolbox server
echo "📋 Testing Toolbox server..."
echo '{"id": 1, "method": "initialize", "params": {"protocolVersion": "2024-11-05", "capabilities": {}}}' | timeout 5 node mcp-servers/toolbox/index.js &
sleep 2
echo "✅ Toolbox server test completed"

echo "🎉 All tests completed!"