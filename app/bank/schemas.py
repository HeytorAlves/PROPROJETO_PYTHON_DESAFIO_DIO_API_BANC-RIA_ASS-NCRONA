from datetime import datetime
from typing import Literal, Optional

from pydantic import BaseModel, Field


class AccountOut(BaseModel):
    id: int
    owner_username: str
    balance: float


class AccountCreateOut(BaseModel):
    id: int
    owner_username: str


class DepositIn(BaseModel):
    amount: float = Field(gt=0, description="Valor do depósito (maior que 0)")


class WithdrawIn(BaseModel):
    amount: float = Field(gt=0, description="Valor do saque (maior que 0)")


TransactionType = Literal["deposit", "withdraw"]


class TransactionOut(BaseModel):
    id: int
    account_id: int
    type: TransactionType
    amount: float
    created_at: datetime


class StatementOut(BaseModel):
    account_id: int
    balance: float
    transactions: list[TransactionOut]
