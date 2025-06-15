import re
from typing import List, Dict


def process_bank_search(data: List[Dict], search: str) -> List[Dict]:
    """
    Фильтрует список банковских операций по наличию строки поиска в описании операции.
    Поиск осуществляется с помощью регулярных выражений (без учета регистра).

    :param data: Список словарей, каждый из которых представляет банковскую операцию.
    :param search: Строка для поиска в описании.
    :return: Список словарей, удовлетворяющих условию поиска.
    """
    pattern = re.compile(re.escape(search), re.IGNORECASE)
    return [operation for operation in data if pattern.search(operation.get("description", ""))]
if __name__ == "__main__":
    # Тестовые данные
    data = [
        {"id": 1, "description": "Оплата в магазине"},
        {"id": 2, "description": "Перевод на карту"},
        {"id": 3, "description": "Оплата мобильной связи"},
    ]
    result = process_bank_search(data, "оплата")
    print(result)