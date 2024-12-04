from typing import Optional
import uuid

class UniqueEntityID:
    _value: str

    def __init__(self, value: Optional[str] = None):
        self._value = value or str(uuid.uuid4())

    def to_string(self) -> str:
        return self._value

    def to_value(self) -> str:
        return self._value

    def equals(self, other: "UniqueEntityID") -> bool:
        return self._value == other.to_value()
