from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timezone
from typing import Optional

from app.bank.schemas import TransactionType


@dataclass
class Account:
    id: int
    owner_username: str
    balance: float = 0.0


@dataclass
class Transaction:
    id: int
    account_id: int
    type: TransactionType
    amount: float
    created_at: datetime


_accounts_by_id: dict[int, Account] = {}
_transactions_by_account: dict[int, list[Transaction]] = {}

_next_account_id = 1
_next_tx_id = 1


def create_account(owner_username: str) -> Account:
    global _next_account_id
    account = Account(id=_next_account_id, owner_username=owner_username, balance=0.0)
    _accounts_by_id[account.id] = account
    _transactions_by_account[account.id] = []
    _next_account_id += 1
    return account


def get_account(account_id: int) -> Optional[Account]:
    return _accounts_by_id.get(account_id)


def deposit(account_id: int, amount: float) -> Account:
    global _next_tx_id
    acc = _accounts_by_id[account_id]
    acc.balance += amount

    tx = Transaction(
        id=_next_tx_id,
        account_id=account_id,
        type="deposit",
        amount=amount,
        created_at=datetime.now(timezone.utc),
    )
    _transactions_by_account[account_id].append(tx)
    _next_tx_id += 1
    return acc


def withdraw(account_id: int, amount: float) -> Account:
    global _next_tx_id
    acc = _accounts_by_id[account_id]
    acc.balance -= amount

    tx = Transaction(
        id=_next_tx_id,
        account_id=account_id,
        type="withdraw",
        amount=amount,
        created_at=datetime.now(timezone.utc),
    )
    _transactions_by_account[account_id].append(tx)
    _next_tx_id += 1
    return acc


def list_transactions(account_id: int) -> list[Transaction]:
    return list(_transactions_by_account.get(account_id, []))
