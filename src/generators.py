from typing import List, Dict, Any, Iterator

def filter_by_currency(
    transactions_list: List[Dict[str, Any]],
    money: str
) -> Iterator[Dict[str, Any]]:
    """Генератор возвращает транзакции с нужной валютой (ключ 'currency')."""
    return (entry for entry in transactions_list if entry.get("currency") == money)

def transaction_descriptions(
    transactions_list: List[Dict[str, Any]]
) -> Iterator[str]:
    """
    Генератор принимает список словарей с транзакциями и возвращает описание каждой операции по очереди.
    Формат строки: "Операция: <amount> <currency>. <description>"
    """
    for entry in transactions_list:
        amount = entry.get("amount", "N/A")
        currency = entry.get("currency", "N/A")
        description = entry.get("description", "")
        yield f"Операция: {amount} {currency}. {description}".strip()

def card_number_generator(
    start: int | str,
    end: int | str
) -> Iterator[str]:
    """
    Генератор выдает номера банковских карт в формате XXXX XXXX XXXX XXXX,
    для диапазона от start до end (оба включительно, могут быть строка или int).
    """
    if isinstance(start, str):
        start_num = int(start.replace(" ", ""))
    else:
        start_num = int(start)
    if isinstance(end, str):
        end_num = int(end.replace(" ", ""))
    else:
        end_num = int(end)
    for num in range(start_num, end_num + 1):
        s = f"{num:016d}"
        yield f"{s[:4]} {s[4:8]} {s[8:12]} {s[12:]}"