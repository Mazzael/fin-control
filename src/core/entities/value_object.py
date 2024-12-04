from typing import TypeVar, Generic
import json

T = TypeVar('T')

class ValueObject(Generic[T]):
    _props: T

    def __init__(self, props: T):
        self._props = props

    @property
    def props(self):
        return self._props

    def equals(self, vo: "ValueObject[T]") -> bool:
        if vo.props is None:
            return False

        return json.dumps(vo.props) == json.dumps(self.props)
