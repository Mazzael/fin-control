from typing import Generic, TypeVar
from src.core.entities.unique_entity_id import UniqueEntityID

T = TypeVar('T')

class Entity(Generic[T]):
    _id: UniqueEntityID
    props: T

    def __init__(self, props: T, entity_id: UniqueEntityID):
        self._id = entity_id or UniqueEntityID()
        self.props = props

    @property
    def id(self) -> UniqueEntityID:
        return self._id

    def equals(self, entity: "Entity[T]") -> bool:
        if entity is self:
            return True

        if entity.id.equals(self._id):
            return True

        return False
