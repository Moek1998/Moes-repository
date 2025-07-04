#!/usr/bin/env node

// Simple MCP server implementation for Toolbox
// This provides various utility tools

const readline = require('readline');
const { exec } = require('child_process');
const fs = require('fs').promises;
const { promisify } = require('util');

const execAsync = promisify(exec);

class ToolboxServer {
  constructor() {
    // Initialize any state if needed
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
                name: 'toolbox',
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
            }
          };
        
        case 'tools/call':
          const { name, arguments: args } = params;
          
          switch (name) {
            case 'execute_command':
              try {
                const { stdout, stderr } = await execAsync(args?.command || '');
                return {
                  id,
                  result: {
                    content: [
                      {
                        type: 'text',
                        text: `Command output:\n${stdout}${stderr ? `\nError: ${stderr}` : ''}`
                      }
                    ]
                  }
                };
              } catch (error) {
                return {
                  id,
                  result: {
                    content: [
                      {
                        type: 'text',
                        text: `Command failed: ${error.message}`
                      }
                    ]
                  }
                };
              }
            
            case 'file_operations':
              try {
                switch (args?.operation) {
                  case 'read':
                    const content = await fs.readFile(args.path, 'utf8');
                    return {
                      id,
                      result: {
                        content: [
                          {
                            type: 'text',
                            text: content
                          }
                        ]
                      }
                    };
                  
                  case 'write':
                    await fs.writeFile(args.path, args.content || '');
                    return {
                      id,
                      result: {
                        content: [
                          {
                            type: 'text',
                            text: `File written successfully: ${args.path}`
                          }
                        ]
                      }
                    };
                  
                  case 'list':
                    const files = await fs.readdir(args.path);
                    return {
                      id,
                      result: {
                        content: [
                          {
                            type: 'text',
                            text: `Files in ${args.path}:\n${files.join('\n')}`
                          }
                        ]
                      }
                    };
                  
                  default:
                    throw new Error(`Unknown file operation: ${args?.operation}`);
                }
              } catch (error) {
                return {
                  id,
                  result: {
                    content: [
                      {
                        type: 'text',
                        text: `File operation failed: ${error.message}`
                      }
                    ]
                  }
                };
              }
            
            case 'text_processing':
              const text = args?.text || '';
              let result = '';
              
              switch (args?.operation) {
                case 'count_words':
                  result = `Word count: ${text.split(/\s+/).filter(w => w.length > 0).length}`;
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
                id,
                result: {
                  content: [
                    {
                      type: 'text',
                      text: result
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

    console.error('Toolbox MCP server started');

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
      console.error('Toolbox MCP server stopped');
      process.exit(0);
    });
  }
}

if (require.main === module) {
  const server = new ToolboxServer();
  server.start();
}

module.exports = ToolboxServer;
