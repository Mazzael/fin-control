from typing import Optional
from datetime import datetime
from dataclasses import dataclass, field
from src.core.entities.unique_entity_id import UniqueEntityID
from src.domain.transactions.enterprise.entities.literals.transaction_type import TransactionType

@dataclass
class User:
    name: str
    cpf: str
    password_hash: str
    current_funds_in_cents: int
    id: UniqueEntityID = field(default_factory= lambda: UniqueEntityID())
    created_at: datetime = field(default_factory=datetime.now)
    updated_at: Optional[datetime] = None

    def _touch(self):
        self.updated_at = datetime.now()

    def change_password(self, new_password_hash: str):
        self.password_hash = new_password_hash
        self._touch()

    def update_current_fund(self, transaction_value_in_cents: int, transaction_type: TransactionType):
        if transaction_type == 'Debit':
            self.current_funds_in_cents -= transaction_value_in_cents
        else:
            self.current_funds_in_cents += transaction_value_in_cents

        self._touch()
