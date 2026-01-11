from fastapi import APIRouter, Depends, HTTPException

from app.auth.security import get_current_user
from app.auth.store import User
from app.bank.schemas import (
    AccountCreateOut,
    AccountOut,
    DepositIn,
    StatementOut,
    WithdrawIn,
)
from app.bank.store import (
    create_account,
    deposit,
    get_account,
    list_transactions,
    withdraw,
)

router = APIRouter(prefix="/bank", tags=["Bank"])


@router.post("/accounts", response_model=AccountCreateOut)
async def open_account(current_user: User = Depends(get_current_user)):
    acc = create_account(owner_username=current_user.username)
    return {"id": acc.id, "owner_username": acc.owner_username}


@router.get("/accounts/{account_id}", response_model=AccountOut)
async def get_account_details(account_id: int, current_user: User = Depends(get_current_user)):
    acc = get_account(account_id)
    if not acc:
        raise HTTPException(status_code=404, detail="Conta não encontrada")

    if acc.owner_username != current_user.username:
        raise HTTPException(status_code=403, detail="Você não tem acesso a esta conta")

    return {"id": acc.id, "owner_username": acc.owner_username, "balance": acc.balance}


@router.post("/accounts/{account_id}/deposit", response_model=AccountOut)
async def deposit_money(
    account_id: int,
    payload: DepositIn,
    current_user: User = Depends(get_current_user),
):
    acc = get_account(account_id)
    if not acc:
        raise HTTPException(status_code=404, detail="Conta não encontrada")

    if acc.owner_username != current_user.username:
        raise HTTPException(status_code=403, detail="Você não tem acesso a esta conta")

    acc = deposit(account_id, payload.amount)
    return {"id": acc.id, "owner_username": acc.owner_username, "balance": acc.balance}


@router.post("/accounts/{account_id}/withdraw", response_model=AccountOut)
async def withdraw_money(
    account_id: int,
    payload: WithdrawIn,
    current_user: User = Depends(get_current_user),
):
    acc = get_account(account_id)
    if not acc:
        raise HTTPException(status_code=404, detail="Conta não encontrada")

    if acc.owner_username != current_user.username:
        raise HTTPException(status_code=403, detail="Você não tem acesso a esta conta")

    if acc.balance < payload.amount:
        raise HTTPException(status_code=400, detail="Saldo insuficiente")

    acc = withdraw(account_id, payload.amount)
    return {"id": acc.id, "owner_username": acc.owner_username, "balance": acc.balance}


@router.get("/accounts/{account_id}/statement", response_model=StatementOut)
async def statement(account_id: int, current_user: User = Depends(get_current_user)):
    acc = get_account(account_id)
    if not acc:
        raise HTTPException(status_code=404, detail="Conta não encontrada")

    if acc.owner_username != current_user.username:
        raise HTTPException(status_code=403, detail="Você não tem acesso a esta conta")

    txs = list_transactions(account_id)
    return {
        "account_id": acc.id,
        "balance": acc.balance,
        "transactions": [
            {
                "id": t.id,
                "account_id": t.account_id,
                "type": t.type,
                "amount": t.amount,
                "created_at": t.created_at,
            }
            for t in txs
        ],
    }
