"""
Claude Squad - Team/session management system for Claude interactions
"""

__version__ = "0.1.0"
__author__ = "Moe"

from .squad import Squad
from .session import Session
from .exceptions import SquadError

__all__ = ["Squad", "Session", "SquadError"]