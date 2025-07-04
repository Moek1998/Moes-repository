"""
Claude Code - A Python client library for interacting with Claude AI
"""

__version__ = "0.1.0"
__author__ = "Moe"

from .client import ClaudeClient
from .config import Config
from .exceptions import ClaudeError, ClaudeAPIError

__all__ = ["ClaudeClient", "Config", "ClaudeError", "ClaudeAPIError"]