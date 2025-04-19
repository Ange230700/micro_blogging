# authentication\service\application\use_cases.py

"""Use case layer for authentication operations."""

from authentication.service.application.repositories import AuthRepositoryInterface
from authentication.service.core.entities import AuthTokens


class AuthUseCase:
    """Use-case layer for auth operations"""

    def __init__(self, repo: AuthRepositoryInterface):
        self.repo = repo

    def register(self, username: str, email: str, password: str) -> None:
        """Register a new user with the given credentials.

        Args:
            username (str): The username for the new account
            email (str): The email address for the new account
            password (str): The password for the new account

        Returns:
            None
        """
        self.repo.register(username, email, password)

    def login(self, username: str, password: str) -> AuthTokens:
        """Authenticate a user with the given credentials.

        Args:
            username (str): The username of the account
            password (str): The password of the account

        Returns:
            AuthTokens: Authentication tokens for the user
        """
        return self.repo.authenticate(username, password)

    def logout(self, refresh_token: str) -> None:
        """Blacklist a refresh token to logout the user.

        Args:
            refresh_token (str): The refresh token to blacklist

        Returns:
            None
        """
        self.repo.blacklist(refresh_token)
