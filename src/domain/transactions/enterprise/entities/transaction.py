from typing import Optional, TypedDict
from datetime import datetime
from pydantic import BaseModel, Field
from src.core.entities.entity import Entity
from src.core.entities.unique_entity_id import UniqueEntityID
from src.domain.transactions.enterprise.entities.literals.category import Category
from src.domain.transactions.enterprise.entities.literals.transaction_type import TransactionType


class TransactionPropsDict(TypedDict, total=False):
    value_in_cents: int
    user_id: UniqueEntityID
    category: Category
    type: TransactionType
    description: str
    created_at: datetime
    updated_at: Optional[datetime]

class TransactionProps(BaseModel):
    user_id: UniqueEntityID
    value_in_cents: int
    category: Category
    type: TransactionType
    description: str
    created_at: datetime = Field(default_factory=datetime.now)
    updated_at: Optional[datetime] = None

    class Config:
        arbitrary_types_allowed = True


class Transaction(Entity[TransactionProps]):
    @property
    def user_id(self) -> UniqueEntityID:
        return self.props.user_id
    
    @property
    def value_in_cents(self) -> int:
        return self.props.value_in_cents

    @property
    def category(self) -> Category:
        return self.props.category
    
    @property
    def type(self) -> TransactionType:
        return self.props.type

    @property
    def description(self) -> str:
        return self.props.description

    @property
    def created_at(self) -> datetime:
        return self.props.created_at

    @property
    def updated_at(self) -> Optional[datetime]:
        return self.props.updated_at

    def _touch(self):
        self.props.updated_at = datetime.now()

    @staticmethod
    def create(
        props: TransactionPropsDict, entity_id: Optional[UniqueEntityID] = None
    ) -> "Transaction":
        """
        Cria uma instância de Transaction, preenchendo campos opcionais automaticamente.
        """
        transaction_props = TransactionProps(**props)
        return Transaction(transaction_props, entity_id or UniqueEntityID())
