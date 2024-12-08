from abc import ABC, abstractmethod
from typing import Dict, Awaitable, Any

class Encrypter(ABC):
    @abstractmethod
    async def encrypt(self, payload: Dict[str, Any]) -> Awaitable[str]:
        pass
