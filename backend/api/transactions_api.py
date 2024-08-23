from fastapi import APIRouter
from backend.scripts.eth_client import EthClient 

transactions_router = APIRouter()


@transactions_router.get("/transactions/{address}&{index}")
async def get_transactions(address: str, index: int):
    
    client = EthClient(address=address, rpc_url="https://cloudflare-eth.com", net_url="https://sepolia.infura.io/v3/843f611c200e4fb9ac1ba55a6978074e")
    transactions = client.get_transactions(start_index=index)
    print(transactions)

    return transactions 
