from abc import ABC, abstractmethod

class UseCaseError(ABC):
    @property
    @abstractmethod
    def message(self) -> str:
        pass
