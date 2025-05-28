import json
import os

def get_transactions(json_path: str) -> list:
    """
    Считывает JSON-файл и возвращает список словарей с транзакциями.
    Если файл отсутствует, пуст, или не содержит список — возвращает пустой список.
    """
    if not os.path.exists(json_path):
        return []
    try:
        with open(json_path, encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError:
                return []
            if isinstance(data, list):
                return data
            else:
                return []
    except (OSError, IOError):
        return []