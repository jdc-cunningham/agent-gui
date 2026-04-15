from pydantic_ai import Agent, RunContext
import requests

def get_weather(ctx: RunContext[None], city: str):
    response = requests.get(f"https://wttr.in/{city}?format=j1")
    return response.json()

# needs full name eg. bitcoin
def get_crypto_price(ctx: RunContext[None], crypto: str):
    response = requests.get(f"https://api.coingecko.com/api/v3/simple/price?ids={crypto}&vs_currencies=usd")
    return response.json()
