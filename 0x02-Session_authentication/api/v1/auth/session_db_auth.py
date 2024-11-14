#!/usr/bin/env python3
"""
Session DB Authentication module for the API
"""

from datetime import datetime, timedelta
from api.v1.auth.session_exp_auth import SessionExpAuth
from models.user_session import UserSession


class SessionDBAuth(SessionExpAuth):
    """Session DB Authentication class"""

    def create_session(self, user_id=None):
        """Create a session and store it in the database"""
        session_id = super().create_session(user_id)
        if session_id is None:
            return None
        user_session = UserSession(user_id=user_id, session_id=session_id)
        user_session.save()
        return session_id

    def user_id_for_session_id(self, session_id=None):
        """Return the user_id by requesting
        UserSession in the database based on session_id"""
        if session_id is None:
            return None
        try:
            user_sessions = UserSession.search({'session_id': session_id})
        except Exception:
            return None
        if not user_sessions:
            return None

        user_session = user_sessions[0]
        if self.session_duration <= 0:
            return user_session.user_id

        if 'created_at' not in user_session.__dict__:
            return None

        created_at = user_session.__dict__.get('created_at')
        expiration_time = created_at + timedelta(seconds=self.session_duration)
        if expiration_time < datetime.now():
            return None

        return user_session.user_id

    def destroy_session(self, request=None):
        """Destroy the UserSession based on the
        Session ID from the request cookie"""
        if request is None:
            return False
        session_id = self.session_cookie(request)
        if session_id is None:
            return False

        try:
            user_sessions = UserSession.search({'session_id': session_id})
        except Exception:
            return False
        if not user_sessions:
            return False

        user_session = user_sessions[0]
        user_session.remove()
        return True
