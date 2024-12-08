from abc import ABC, abstractmethod
from typing import Awaitable

class HashComparer(ABC):
    @abstractmethod
    async def compare(self, plain: str, password_hash: str) -> Awaitable[bool]:
        pass
