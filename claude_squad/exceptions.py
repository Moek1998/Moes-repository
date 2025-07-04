"""
Custom exceptions for Claude Squad
"""


class SquadError(Exception):
    """Base exception for Claude Squad"""
    pass


class SessionError(SquadError):
    """Exception for session-related errors"""
    pass


class SquadNotFoundError(SquadError):
    """Exception when squad is not found"""
    pass