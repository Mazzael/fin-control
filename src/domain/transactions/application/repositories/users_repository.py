from abc import ABC, abstractmethod
from typing import Optional
from src.domain.transactions.enterprise.entities.user import User

class UsersRepository(ABC):
    @abstractmethod
    async def find_by_id(self, user_id: str) -> Optional[User]:
        pass

    @abstractmethod
    async def find_by_cpf(self, cpf: str) -> Optional[User]:
        pass

    @abstractmethod
    async def create(self, user: User) -> None:
        pass

    @abstractmethod
    async def save(self, user: User) -> None:
        pass

    @abstractmethod
    async def delete(self, user: User) -> None:
        pass
    