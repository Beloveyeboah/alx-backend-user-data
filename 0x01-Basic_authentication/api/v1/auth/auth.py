#!/usr/bin/env python3
"""
Module for authentication
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Template class for all authentication systems"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """ Determines if authentication is required
        :param path: string path to be checked
        :param excluded_paths: list of paths that do
        not require authentication
        return: True if authentication is required,
        False otherwise """
        if path is None:
            return True
        if not excluded_paths:
            return True
        # Normalize the path to ensure it has a trailing slash
        if not path.endswith('/'):
            path += '/'

        for excluded_path in excluded_paths:
            if excluded_path.endswith('/') and path == excluded_path:
                return False

        return True

    def authorization_header(self, request=None) -> str:
        """
        Retrieves the authorization header from the request
        :param request: Flask request object
        :return: None for now, implementation will be updated later
        """
        if request is None:
            return None
        if 'Authorization' not in request.headers:
            return None
        return request.headers['Authorization']

    def current_user(self, request=None) -> TypeVar('User'):
        """
        Retrieves the current user from the request
        :param request: Flask request object
        :return: None for now, implementation will be updated later
        """
        return None
