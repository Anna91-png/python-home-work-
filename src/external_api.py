import os
import requests
from dotenv import load_dotenv

load_dotenv()

EXCHANGE_API_KEY = os.getenv("EXCHANGE_RATES_API_KEY")
API_URL = "https://api.apilayer.com/exchangerates_data/convert"

def convert_to_rub(amount: float, from_currency: str) -> float:
    """
    Конвертирует сумму в валюте from_currency в рубли (RUB) через внешний API.
    """
    if from_currency == "RUB":
        return float(amount)
    if not EXCHANGE_API_KEY:
        raise RuntimeError("API ключ для обмена валют не найден в переменных окружения.")
    params = {
        "to": "RUB",
        "from": from_currency,
        "amount": amount
    }
    headers = {"apikey": EXCHANGE_API_KEY}
    response = requests.get(API_URL, params=params, headers=headers)
    response.raise_for_status()
    data = response.json()
    return float(data["result"])