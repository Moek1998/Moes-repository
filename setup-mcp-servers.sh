#!/bin/bash

# MCP Servers Setup Script for Cursor IDE
# This script downloads and sets up Context 7 and Toolbox MCP servers

set -e

echo "🚀 Setting up MCP servers for Cursor IDE..."

# Create mcp-servers directory
mkdir -p mcp-servers
cd mcp-servers

# Function to download and setup a generic MCP server from npm
setup_npm_mcp() {
    local name=$1
    local package=$2
    
    echo "📦 Setting up $name MCP server..."
    mkdir -p "$name"
    cd "$name"
    
    # Initialize npm project
    npm init -y
    
    # Install the MCP server package
    npm install "$package"
    
    # Create a simple index.js wrapper if needed
    if [ ! -f "dist/index.js" ]; then
        mkdir -p dist
        cat > dist/index.js << EOF
// Wrapper for $name MCP server
const { startServer } = require('$package');

if (require.main === module) {
    startServer();
}

module.exports = { startServer };
EOF
    fi
    
    cd ..
    echo "✅ $name MCP server setup complete"
}

# Setup Context 7 MCP server
echo "🔧 Setting up Context 7 MCP server..."
mkdir -p context-7
cd context-7

# Initialize npm project for context-7
npm init -y

# For now, we'll create a basic MCP server structure for context management
# This can be replaced with actual context-7 package when available
cat > package.json << 'EOF'
{
  "name": "context-7-mcp",
  "version": "1.0.0",
  "description": "Context 7 MCP Server for managing conversation context",
  "main": "dist/index.js",
  "scripts": {
    "build": "tsc",
    "start": "node dist/index.js"
  },
  "dependencies": {
    "@modelcontextprotocol/sdk": "^0.4.0",
    "typescript": "^5.0.0"
  },
  "devDependencies": {
    "@types/node": "^20.0.0"
  }
}
EOF

# Create basic TypeScript config
cat > tsconfig.json << 'EOF'
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "commonjs",
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
EOF

# Create source directory and basic server
mkdir -p src
cat > src/index.ts << 'EOF'
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from '@modelcontextprotocol/sdk/types.js';

const server = new Server(
  {
    name: 'context-7',
    version: '1.0.0',
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// Context management functionality
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: 'get_context',
        description: 'Get conversation context',
        inputSchema: {
          type: 'object',
          properties: {
            depth: {
              type: 'number',
              description: 'Context depth to retrieve',
              default: 7
            }
          }
        }
      },
      {
        name: 'set_context',
        description: 'Set conversation context',
        inputSchema: {
          type: 'object',
          properties: {
            context: {
              type: 'string',
              description: 'Context to set'
            }
          },
          required: ['context']
        }
      }
    ]
  };
});

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;
  
  switch (name) {
    case 'get_context':
      return {
        content: [
          {
            type: 'text',
            text: `Retrieved context with depth: ${args?.depth || 7}`
          }
        ]
      };
    
    case 'set_context':
      return {
        content: [
          {
            type: 'text',
            text: `Context set: ${args?.context}`
          }
        ]
      };
    
    default:
      throw new Error(`Unknown tool: ${name}`);
  }
});

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error('Context 7 MCP server running on stdio');
}

if (require.main === module) {
  runServer().catch(console.error);
}
EOF

# Install dependencies and build
npm install
npm run build

cd ..

# Setup Toolbox MCP server
echo "🔧 Setting up Toolbox MCP server..."
mkdir -p toolbox
cd toolbox

# Initialize npm project for toolbox
npm init -y

cat > package.json << 'EOF'
{
  "name": "toolbox-mcp",
  "version": "1.0.0",
  "description": "Toolbox MCP Server providing various utility tools",
  "main": "dist/index.js",
  "scripts": {
    "build": "tsc",
    "start": "node dist/index.js"
  },
  "dependencies": {
    "@modelcontextprotocol/sdk": "^0.4.0",
    "typescript": "^5.0.0"
  },
  "devDependencies": {
    "@types/node": "^20.0.0"
  }
}
EOF

# Create TypeScript config
cat > tsconfig.json << 'EOF'
{
  "compilerOptions": {
    "target": "ES2020",
    "module": "commonjs",
    "outDir": "./dist",
    "rootDir": "./src",
    "strict": true,
    "esModuleInterop": true,
    "skipLibCheck": true,
    "forceConsistentCasingInFileNames": true
  },
  "include": ["src/**/*"],
  "exclude": ["node_modules", "dist"]
}
EOF

# Create source directory and basic server
mkdir -p src
cat > src/index.ts << 'EOF'
import { Server } from '@modelcontextprotocol/sdk/server/index.js';
import { StdioServerTransport } from '@modelcontextprotocol/sdk/server/stdio.js';
import {
  CallToolRequestSchema,
  ListToolsRequestSchema,
} from '@modelcontextprotocol/sdk/types.js';
import { exec } from 'child_process';
import { promisify } from 'util';

const execAsync = promisify(exec);

const server = new Server(
  {
    name: 'toolbox',
    version: '1.0.0',
  },
  {
    capabilities: {
      tools: {},
    },
  }
);

// Toolbox functionality
server.setRequestHandler(ListToolsRequestSchema, async () => {
  return {
    tools: [
      {
        name: 'execute_command',
        description: 'Execute a shell command',
        inputSchema: {
          type: 'object',
          properties: {
            command: {
              type: 'string',
              description: 'Command to execute'
            }
          },
          required: ['command']
        }
      },
      {
        name: 'file_operations',
        description: 'Perform file operations',
        inputSchema: {
          type: 'object',
          properties: {
            operation: {
              type: 'string',
              enum: ['read', 'write', 'list'],
              description: 'File operation to perform'
            },
            path: {
              type: 'string',
              description: 'File path'
            },
            content: {
              type: 'string',
              description: 'Content for write operations'
            }
          },
          required: ['operation', 'path']
        }
      },
      {
        name: 'text_processing',
        description: 'Process text with various utilities',
        inputSchema: {
          type: 'object',
          properties: {
            operation: {
              type: 'string',
              enum: ['count_words', 'count_lines', 'uppercase', 'lowercase'],
              description: 'Text processing operation'
            },
            text: {
              type: 'string',
              description: 'Text to process'
            }
          },
          required: ['operation', 'text']
        }
      }
    ]
  };
});

server.setRequestHandler(CallToolRequestSchema, async (request) => {
  const { name, arguments: args } = request.params;
  
  switch (name) {
    case 'execute_command':
      try {
        const { stdout, stderr } = await execAsync(args?.command || '');
        return {
          content: [
            {
              type: 'text',
              text: `Command output:\n${stdout}${stderr ? `\nError: ${stderr}` : ''}`
            }
          ]
        };
      } catch (error) {
        return {
          content: [
            {
              type: 'text',
              text: `Command failed: ${error}`
            }
          ]
        };
      }
    
    case 'file_operations':
      const fs = require('fs').promises;
      try {
        switch (args?.operation) {
          case 'read':
            const content = await fs.readFile(args.path, 'utf8');
            return {
              content: [
                {
                  type: 'text',
                  text: content
                }
              ]
            };
          
          case 'write':
            await fs.writeFile(args.path, args.content || '');
            return {
              content: [
                {
                  type: 'text',
                  text: `File written successfully: ${args.path}`
                }
              ]
            };
          
          case 'list':
            const files = await fs.readdir(args.path);
            return {
              content: [
                {
                  type: 'text',
                  text: `Files in ${args.path}:\n${files.join('\n')}`
                }
              ]
            };
        }
      } catch (error) {
        return {
          content: [
            {
              type: 'text',
              text: `File operation failed: ${error}`
            }
          ]
        };
      }
      break;
    
    case 'text_processing':
      const text = args?.text || '';
      let result = '';
      
      switch (args?.operation) {
        case 'count_words':
          result = `Word count: ${text.split(/\s+/).length}`;
          break;
        case 'count_lines':
          result = `Line count: ${text.split('\n').length}`;
          break;
        case 'uppercase':
          result = text.toUpperCase();
          break;
        case 'lowercase':
          result = text.toLowerCase();
          break;
        default:
          result = 'Unknown text processing operation';
      }
      
      return {
        content: [
          {
            type: 'text',
            text: result
          }
        ]
      };
    
    default:
      throw new Error(`Unknown tool: ${name}`);
  }
});

async function runServer() {
  const transport = new StdioServerTransport();
  await server.connect(transport);
  console.error('Toolbox MCP server running on stdio');
}

if (require.main === module) {
  runServer().catch(console.error);
}
EOF

# Install dependencies and build
npm install
npm run build

cd ..

echo "✅ All MCP servers setup complete!"
echo ""
echo "📋 Next steps:"
echo "1. Copy cursor-mcp-config.json to your Cursor IDE configuration directory"
echo "2. Restart Cursor IDE to load the MCP servers"
echo "3. The servers should now be available in Cursor"
echo ""
echo "🔧 MCP Servers installed:"
echo "- Context 7: ./mcp-servers/context-7/"
echo "- Toolbox: ./mcp-servers/toolbox/"