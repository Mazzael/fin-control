from typing import Optional, TypedDict
from datetime import datetime
from pydantic import BaseModel, Field
from src.core.entities.entity import Entity
from src.core.entities.unique_entity_id import UniqueEntityID

class UserPropsDict(TypedDict, total=False):
    name: str
    cpf: str
    password_hash: str
    created_at: datetime
    updated_at: Optional[datetime]

class UserProps(BaseModel):
    name: str
    cpf: str
    password_hash: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = None


class User(Entity[UserProps]):
    @property
    def name(self) -> str:
        return self.props.name

    @property
    def cpf(self) -> str:
        return self.props.cpf

    @property
    def password_hash(self) -> str:
        return self.props.password_hash

    @property
    def created_at(self) -> datetime:
        return self.props.created_at

    @property
    def updated_at(self) -> Optional[datetime]:
        return self.props.updated_at

    def _touch(self):
        self.props.updated_at = datetime.now()

    def change_password(self, new_password_hash: str):
        self.props.password_hash = new_password_hash
        self._touch()

    @staticmethod
    def create(
        props: UserPropsDict, entity_id: Optional[UniqueEntityID] = None
    ) -> "User":
        """
        Cria uma instância de User, preenchendo campos opcionais automaticamente.
        """
        user_props = UserProps(**props)
        return User(user_props, entity_id or UniqueEntityID())
