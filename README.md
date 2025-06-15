# Auto Repo Setup

This repository contains a Python script (`setup_repo.py`) that bootstraps a local development environment for LLM-based workflows.

The script creates a project structure, installs dependencies, and generates configuration files. It is designed to integrate with AWS (including Bedrock), Google Cloud, and other LLM tooling like Claude (via aider/MCP integrations).

## Quick Start

1. Ensure Python 3.9+ is installed.
2. Run `python3 setup_repo.py --init` to generate project scaffolding.
3. Edit files under `config/` to add API keys and provider settings.
4. Run `pip install -r requirements.txt` to install required packages.

See `setup_repo.py --help` for all available options.
