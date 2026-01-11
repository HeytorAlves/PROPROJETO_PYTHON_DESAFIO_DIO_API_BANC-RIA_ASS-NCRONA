from fastapi import FastAPI

from app.auth.router import router as auth_router
from app.bank.router import router as bank_router

app = FastAPI(title="API Bancária Assíncrona", version="1.0.0")

app.include_router(auth_router)
app.include_router(bank_router)


@app.get("/health", tags=["Health"])
async def health_check():
    return {"status": "ok"}
