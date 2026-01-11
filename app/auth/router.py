from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.auth.security import create_access_token, hash_password, verify_password
from app.auth.store import create_user, get_user_by_username

router = APIRouter(prefix="/auth", tags=["Auth"])


@router.post("/register")
async def register(data: dict):
    username = data.get("username")
    password = data.get("password")

    if not username or not password:
        raise HTTPException(status_code=422, detail="username e password são obrigatórios")

    if get_user_by_username(username):
        raise HTTPException(status_code=409, detail="Usuário já existe")

    user = create_user(username, hash_password(password))
    return {"id": user.id, "username": user.username}


@router.post("/login")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = get_user_by_username(form_data.username)
    if not user or not verify_password(form_data.password, user.password_hash):
        raise HTTPException(status_code=401, detail="Credenciais inválidas")

    token = create_access_token(subject=user.username)
    return {"access_token": token, "token_type": "bearer"}
