from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from web3 import Web3

from dotenv import load_dotenv
import uvicorn
import requests
import os

load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

API = os.environ.get("ETHERSCAN")

@app.get("/transactions/{address}&{index}")
def transactions(address: str, index: int):
    API = os.environ.get("ETHERSCAN")
    url = f"https://api.etherscan.io/api?module=account&action=txlist&address={address}&sort=desc&apikey={API}"

    response = requests.get(url).json()
    result = response['result']

    transactions = [
        {
            "hash" : i["hash"],
            "from" : i["from"],
            "to" : i["to"],
            "value" : f"{round(Web3.from_wei(int(i["value"]), "ether"), 5)} ETH",
            "gas" : f"{i["gas"]} wei",
            "total" : len(result),
        }
        for i in result[index:index+3]
    ]
    print(transactions)
    return transactions


if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port="8001" , reload=True)