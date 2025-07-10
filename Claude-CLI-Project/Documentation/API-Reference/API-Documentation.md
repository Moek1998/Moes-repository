# Claude CLI API Reference

## Overview
This document provides detailed API reference for the Claude CLI project components.

## Core Components

### ClaudeCLI Class
The main class that handles all Claude API interactions.

#### Methods

##### `__init__()`
Initializes the Claude CLI with configuration setup.

##### `setup_config()`
Sets up the configuration directory and file structure.

##### `load_config()`
Loads configuration from the config file.

##### `chat(message, system_prompt=None, model=None)`
Sends a message to Claude and returns the response.

**Parameters:**
- `message` (str): The message to send to Claude
- `system_prompt` (str, optional): System prompt to use
- `model` (str, optional): Specific model to use

**Returns:**
- `str` or `None`: Claude's response or None if error

##### `show_subscription_info()`
Displays information about different Claude access types.

##### `show_models()`
Lists all available Claude models.

##### `simulate_squad_features()`
Simulates Claude Pro's Squad features.

##### `simulate_code_features()`
Simulates Claude Pro's Code features.

##### `interactive_mode_enhanced(system_prompt=None)`
Enhanced interactive mode with additional features.

## Configuration

### Config File Structure
Located at `~/.claude/config.ini`

```ini
[DEFAULT]
api_key = your_api_key_here
model = claude-3-5-sonnet-20241022
max_tokens = 1000
temperature = 0.7
subscription_type = api

[PRO_FEATURES]
priority_bandwidth = false
early_access = false
usage_5x_limit = false
```

## Available Models

| Model ID | Description | Use Case |
|----------|-------------|----------|
| `claude-3-5-sonnet-20241022` | Latest & most capable | General use, coding, analysis |
| `claude-3-opus-20240229` | Most powerful reasoning | Complex tasks, research |
| `claude-3-sonnet-20240229` | Balanced performance | Most applications |
| `claude-3-haiku-20240307` | Fastest & cheapest | Quick responses, high volume |
| `claude-2.1` | Legacy model | Established workflows |

## Error Handling

### Common Error Codes
- **401 Unauthorized**: Invalid or expired API key
- **429 Rate Limited**: Too many requests
- **500 Server Error**: Anthropic API issues

### Error Messages
- "No API key found": Set up API key using `--setup-key`
- "API key invalid": Get new key from console.anthropic.com
- "Rate limit reached": Consider upgrading API plan