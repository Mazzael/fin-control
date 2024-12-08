from typing import Optional, TypedDict
from datetime import datetime
from pydantic import BaseModel, Field
from src.core.entities.entity import Entity
from src.core.entities.unique_entity_id import UniqueEntityID
from src.domain.transactions.enterprise.entities.literals.transaction_type import TransactionType

class UserPropsDict(TypedDict, total=False):
    name: str
    cpf: str
    password_hash: str
    current_funds_in_cents: int
    created_at: datetime
    updated_at: Optional[datetime]

class UserProps(BaseModel):
    name: str
    cpf: str
    password_hash: str
    current_funds_in_cents: int
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
    def current_funds_in_cents(self) -> int:
        return self.props.current_funds_in_cents

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

    def update_current_fund(self, transaction_value_in_cents: int, transaction_type: TransactionType):
        if transaction_type == 'Debit':
            self.props.current_funds_in_cents -= transaction_value_in_cents
        else:
            self.props.current_funds_in_cents += transaction_value_in_cents

        self._touch()

    @staticmethod
    def create(
        props: UserPropsDict, entity_id: Optional[UniqueEntityID] = None
    ) -> "User":
        user_props = UserProps(**props)
        return User(user_props, entity_id or UniqueEntityID())
