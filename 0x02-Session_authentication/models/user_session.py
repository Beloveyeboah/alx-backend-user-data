#!/usr/bin/env python3
"""
UserSession model for storing session data in a database
"""

from models.base import Base


class UserSession(Base):
    """UserSession class that inherits from Base"""

    def __init__(self, *args: list, **kwargs: dict):
        """Initialize UserSession with user_id and session_id"""
        super().__init__(*args, **kwargs)
        self.user_id = kwargs.get('user_id')
        self.session_id = kwargs.get('session_id')
