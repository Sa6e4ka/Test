from backend import (
    create_router,
    import_router,
    token_router,
    transactions_router,
    balance_router
)

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
app = FastAPI()

origins = [
    "http://localhost:5173",  
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(create_router)
app.include_router(import_router)
app.include_router(token_router)
app.include_router(transactions_router)
app.include_router(balance_router)


@app.get("/")
async def start():
    return 'Alive!'