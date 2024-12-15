from typing import Optional
from datetime import datetime
from dataclasses import dataclass, field
from src.core.entities.unique_entity_id import UniqueEntityID
from src.domain.transactions.enterprise.entities.literals.category import Category
from src.domain.transactions.enterprise.entities.literals.transaction_type import TransactionType

@dataclass
class Transaction:
    id: UniqueEntityID
    user_id: UniqueEntityID
    value_in_cents: int
    category: Category
    type: TransactionType
    description: str
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: Optional[datetime] = None
