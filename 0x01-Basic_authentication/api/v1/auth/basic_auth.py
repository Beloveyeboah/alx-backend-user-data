#!/usr/bin/env python3
"""
Module for authentication using Basic auth
"""


from typing import TypeVar
from api.v1.auth.auth import Auth
import base64

from models.user import User


class BasicAuth(Auth):
    """_summary_
    """

    def extract_base64_authorization_header(self,
                                            authorization_header: str) -> str:
        """_summary_

        Args:
                 authorization_header (str): _description_

        Returns:
                 str: _description_
        """
        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith('Basic '):
            return None

        token = authorization_header.split(' ')[-1]
        return token

    def decode_base64_authorization_header(
            self, base64_authorization_header: str) -> str:
        """_summary_

        Args:
                 base64_authorization_header (str): _description_

        Returns:
                  str: _description_
        """
        if base64_authorization_header is None:
            return None
        if not isinstance(base64_authorization_header, str):
            return None

        try:
            item_to_decode = base64_authorization_header.encode('utf-8')
            decoded = base64.b64decode(item_to_decode)
            return decoded.decode('utf-8')
        except Exception:
            return None

        def extract_user_credentials(
                self, decoded_base64_authorization_header: str) -> (str, str):
            """Extracts user email and password
            from Base64 decoded value
            """

            if decoded_base64_authorization_header is None:
                return (None, None)
            if not isinstance(decoded_base64_authorization_header, str):
                return (None, None)
            if ':' not in decoded_base64_authorization_header:
                return (None, None)

            email, password = decoded_base64_authorization_header.split(':')
            return (email, password)
