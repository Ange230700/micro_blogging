# authentication/service/application/repositories/user_repository.py

from abc import ABC, abstractmethod
from service.core.entities.user import UserEntity

class UserRepositoryInterface(ABC):
    @abstractmethod
    def get_by_email(self, email: str) -> UserEntity:
        """Retrieve a user entity based on email."""
        pass
