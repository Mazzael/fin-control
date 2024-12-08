from abc import ABC, abstractmethod

class HashGenerator(ABC):
    @abstractmethod
    async def hash(self, plain: str) -> str:
        pass
