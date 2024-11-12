#!/usr/bin/env python3
"""
Module for authentication
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Template class for all authentication systems"""

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Determines if authentication is required
        :param path: string path to be checked
        :param excluded_paths: list of paths that do not require authentication
        :return: False for now, implementation will be updated later
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the authorization header from the request
        :param request: Flask request object
        :return: None for now, implementation will be updated later
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current user from the request
        :param request: Flask request object
        :return: None for now, implementation will be updated later
        """
        return None
