from abc import ABC, abstractmethod

class UseCaseError(ABC, Exception):
    @property
    @abstractmethod
    def message(self) -> str:
        pass
