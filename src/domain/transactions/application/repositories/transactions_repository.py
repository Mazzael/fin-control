from abc import ABC, abstractmethod
from typing import Optional, List
from src.domain.transactions.enterprise.entities.transaction import Transaction

class TransactionsRepository(ABC):
    @abstractmethod
    async def find_by_id(self, transaction_id: str) -> Optional[Transaction]:
        pass

    @abstractmethod
    async def find_many_by_user_id(self, user_id: str) -> Optional[List[Transaction]]:
        pass

    @abstractmethod
    async def create(self, transaction: Transaction) -> None:
        pass

    @abstractmethod
    async def save(self, transaction: Transaction) -> None:
        pass

    @abstractmethod
    async def delete(self, transaction: Transaction) -> None:
        pass
    