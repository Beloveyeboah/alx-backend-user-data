#!/usr/bin/env python3
"""
Module for authentication
"""

from flask import request
from typing import List, TypeVar


class Auth:
    """Template class for all authentication systems"""
    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """_summary_

        Args:
                path (str): _description_
                excluded_paths (List[str]): _description_

        Returns:
                bool: _description_
        """
        if path is None:
            return True

        if excluded_paths is None or excluded_paths == []:
            return True

        if path in excluded_paths:
            return False

        for excluded_path in excluded_paths:
            if excluded_path.startswith(path):
                return False
            elif path.startswith(excluded_path):
                return False
            elif excluded_path[-1] == "*":
                if path.startswith(excluded_path[:-1]):
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
