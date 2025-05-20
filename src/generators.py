from typing import List, Dict, Any, Iterator

def filter_by_currency(
    transactions_list: List[Dict[str, Any]],
    money: str
) -> Iterator[Dict[str, Any]]:
    return (
        entry for entry in transactions_list
        if (
            "operationAmount" in entry and
            "currency" in entry["operationAmount"] and
            entry["operationAmount"]["currency"].get("code") == money
        )
    )

# Пример данных:
transactions = [
    {
        "id": 939719570,
        "state": "EXECUTED",
        "date": "2018-06-30T02:08:58.425572",
        "operationAmount": {
            "amount": "9824.07",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод организации",
        "from": "Счет 75106830613657916952",
        "to": "Счет 11776614605963066702"
    },
    {
        "id": 142264268,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "79114.93",
            "currency": {
                "name": "USD",
                "code": "USD"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    },
    {
        "id": 1,
        "state": "EXECUTED",
        "date": "2019-04-04T23:20:05.206878",
        "operationAmount": {
            "amount": "100",
            "currency": {
                "name": "RUB",
                "code": "RUB"
            }
        },
        "description": "Перевод со счета на счет",
        "from": "Счет 19708645243227258542",
        "to": "Счет 75651667383060284188"
    }
]

usd_transactions = filter_by_currency(transactions, "USD")
for _ in range(2):
    print(next(usd_transactions))


    def transaction_descriptions(
            transactions_list: List[Dict[str, Any]]
    ) -> Iterator[str]:
        """
        Генератор возвращает описание каждой операции по очереди (ключ 'description').
        """
        for entry in transactions_list:
            yield entry.get("description", "")


    transactions = [
        {"description": "Перевод организации"},
        {"description": "Перевод со счета на счет"},
        {"description": "Перевод со счета на счет"},
        {"description": "Перевод с карты на карту"},
        {"description": "Перевод организации"},
    ]

    descriptions = transaction_descriptions(transactions)
    for _ in range(5):
        print(next(descriptions))


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


        for card_number in card_number_generator(1, 5):
            print(card_number)
