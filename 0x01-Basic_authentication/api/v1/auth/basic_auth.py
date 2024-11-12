#!/usr/bin/env python3
"""
basic authentification for the API
"""

from api.v1.auth.auth import Auth

class BasicAuth(Auth):
    """Class for Basic Authentication"""

    def extract_base64_authorization_header(self, authorization_header: str) -> str:
        """
        Extracts the Base64 part of the Authorization header for Basic Authentication.
        :param authorization_header: Authorization header value
        :return: Base64 part of the Authorization header or None
        """

        if authorization_header is None:
            return None
        if not isinstance(authorization_header, str):
            return None
        if not authorization_header.startswith("Basic "):
            return None

        return authorization_header[len("Basic "):]
