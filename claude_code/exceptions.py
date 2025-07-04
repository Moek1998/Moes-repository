"""
Custom exceptions for Claude Code
"""


class ClaudeError(Exception):
    """Base exception for Claude Code"""
    pass


class ClaudeAPIError(ClaudeError):
    """Exception for API-related errors"""
    
    def __init__(self, message: str, status_code: int = None):
        super().__init__(message)
        self.status_code = status_code


class ClaudeConfigError(ClaudeError):
    """Exception for configuration errors"""
    pass