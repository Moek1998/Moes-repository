#!/usr/bin/env node

// Simple MCP server implementation for Context 7
// This provides basic context management functionality

const readline = require('readline');

class Context7Server {
  constructor() {
    this.context = [];
    this.maxDepth = 7;
  }

  async handleRequest(request) {
    const { id, method, params } = request;
    
    try {
      switch (method) {
        case 'initialize':
          return {
            id,
            result: {
              protocolVersion: '2024-11-05',
              capabilities: {
                tools: {}
              },
              serverInfo: {
                name: 'context-7',
                version: '1.0.0'
              }
            }
          };
        
        case 'tools/list':
          return {
            id,
            result: {
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
            }
          };
        
        case 'tools/call':
          const { name, arguments: args } = params;
          
          switch (name) {
            case 'get_context':
              const depth = args?.depth || this.maxDepth;
              const contextSlice = this.context.slice(-depth);
              return {
                id,
                result: {
                  content: [
                    {
                      type: 'text',
                      text: `Retrieved context (depth: ${depth}):\n${contextSlice.join('\n')}`
                    }
                  ]
                }
              };
            
            case 'set_context':
              if (args?.context) {
                this.context.push(args.context);
                // Keep only the last maxDepth items
                if (this.context.length > this.maxDepth) {
                  this.context = this.context.slice(-this.maxDepth);
                }
              }
              return {
                id,
                result: {
                  content: [
                    {
                      type: 'text',
                      text: `Context set: ${args?.context}`
                    }
                  ]
                }
              };
            
            default:
              throw new Error(`Unknown tool: ${name}`);
          }
        
        default:
          throw new Error(`Unknown method: ${method}`);
      }
    } catch (error) {
      return {
        id,
        error: {
          code: -32000,
          message: error.message
        }
      };
    }
  }

  start() {
    const rl = readline.createInterface({
      input: process.stdin,
      output: process.stdout
    });

    console.error('Context 7 MCP server started');

    rl.on('line', async (line) => {
      if (line.trim()) {
        try {
          const request = JSON.parse(line);
          const response = await this.handleRequest(request);
          console.log(JSON.stringify(response));
        } catch (error) {
          console.error('Error processing request:', error);
        }
      }
    });

    rl.on('close', () => {
      console.error('Context 7 MCP server stopped');
      process.exit(0);
    });
  }
}

if (require.main === module) {
  const server = new Context7Server();
  server.start();
}

module.exports = Context7Server;
