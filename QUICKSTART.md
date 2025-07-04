# Quick Start Guide

## 🚀 Get Started in 3 Steps

### Step 1: Run Setup
```bash
./setup-mcp-servers-simple.sh
```

### Step 2: Configure Cursor
Copy the configuration to your Cursor directory:

**macOS:**
```bash
cp cursor-mcp-config.json ~/Library/Application\ Support/Cursor/User/mcp_servers.json
```

**Linux:**
```bash
cp cursor-mcp-config.json ~/.config/Cursor/User/mcp_servers.json
```

**Windows:**
```powershell
Copy-Item cursor-mcp-config.json $env:APPDATA\Cursor\User\mcp_servers.json
```

### Step 3: Restart Cursor
Restart Cursor IDE and your MCP servers will be available!

## 🧪 Test Your Setup
```bash
./test-mcp-servers.sh
```

## 🎯 What You Get

- **Context 7 Server**: Manage conversation context with depth control
- **Toolbox Server**: Execute commands, handle files, process text

## 📚 Need More Help?

- Read the full [README.md](README.md)
- Check the [INSTALL.md](INSTALL.md) for detailed instructions
- Review the [config/README.md](config/README.md) for configuration options