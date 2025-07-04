"""
Configuration management for Claude Code
"""

import os
from typing import Optional
from dotenv import load_dotenv

load_dotenv()


class Config:
    """Configuration class for Claude Code"""
    
    def __init__(self, api_key: Optional[str] = None):
        self.api_key = api_key or os.getenv("CLAUDE_API_KEY")
        self.base_url = os.getenv("CLAUDE_BASE_URL", "https://api.anthropic.com")
        self.model = os.getenv("CLAUDE_MODEL", "claude-3-sonnet-20240229")
        self.max_tokens = int(os.getenv("CLAUDE_MAX_TOKENS", "1000"))
        self.temperature = float(os.getenv("CLAUDE_TEMPERATURE", "0.7"))
        
    def validate(self) -> bool:
        """Validate configuration"""
        if not self.api_key:
            raise ValueError("API key is required. Set CLAUDE_API_KEY environment variable or pass api_key parameter.")
        return True