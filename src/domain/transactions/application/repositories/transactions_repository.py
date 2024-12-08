from abc import ABC, abstractmethod
from typing import Optional, List, Awaitable
from src.domain.transactions.enterprise.entities.transaction import Transaction

class TransactionsRepository(ABC):
    @abstractmethod
    def find_by_id(self, transaction_id: str) -> Awaitable[Optional[Transaction]]:
        pass

    @abstractmethod
    def find_many_by_user_id(self, user_id: str) -> Awaitable[Optional[List[Transaction]]]:
        pass

    @abstractmethod
    def create(self, transaction: Transaction) -> Awaitable[None]:
        pass

    @abstractmethod
    def save(self, transaction: Transaction) -> Awaitable[None]:
        pass

    @abstractmethod
    def delete(self, transaction: Transaction) -> Awaitable[None]:
        pass
    