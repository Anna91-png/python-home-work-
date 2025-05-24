
from typing import Any, List, Dict


def filter_by_state(
    items: List[Dict[str, Any]], state: str = "EXECUTED"
) -> List[Dict[str, Any]]:
    """
    Возвращает новый список словарей, у которых значение по ключу 'state' равно переданному значению.
    """
    return [item for item in items if item.get("state") == state]


def sort_by_date(
    items: List[Dict[str, Any]], reverse: bool = True
) -> List[Dict[str, Any]]:
    """
    Сортирует список словарей по ключу 'date' в порядке убывания (по умолчанию).
    """
    return sorted(items, key=lambda x: x["date"], reverse=reverse)


# Пример использования:
if __name__ == "__main__":
    list_of_dicts = [
        {"id": 41428829, "state": "EXECUTED", "date": "2019-07-03T18:35:29.512364"},
        {"id": 939719570, "state": "EXECUTED", "date": "2018-06-30T02:08:58.425572"},
        {"id": 594226727, "state": "CANCELED", "date": "2018-09-12T21:27:25.241689"},
        {"id": 615064591, "state": "CANCELED", "date": "2018-10-14T08:21:33.419441"},
    ]

    print(filter_by_state(list_of_dicts))
    print(sort_by_date(list_of_dicts))

    # Ссылки на функции
    list_first_func = filter_by_state
    list_second_func = sort_by_date