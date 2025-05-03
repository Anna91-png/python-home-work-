from typing import List

from src.mask import get_mask_account
from src.mask import get_mask_card_number


def mask_account_card(account_list: List[str]) -> None:
    """
    Функция, которая умеет обрабатывать информацию о картах и счетах
    """
    for i in account_list:
        i = i.split()
        if i[0] == "Visa":
            print(f"Visa Platinum {get_mask_card_number(i[-1])}")
        elif i[0] == "Maestro":
            print(f"Maestro {get_mask_card_number(i[-1])}")
        elif i[0] == "Счет":
            print(f"Счет {get_mask_account(i[-1])}")


def get_date(date: str) -> str:
    """
    Функция, которая возвращает строку с датой в формате "ДД.ММ.ГГГГ"
    """
    date = date[:10].split("-")[::-1]
    return ".".join(date)

a = ["Visa Platinum 7000792289606361"]
b = ["Maestro 7000792289606361"]
c = ["Счет 73654108430135874305"]

vh = [
    "Maestro 1596837868705199",
    "Счет 64686473678894779589",
    "MasterCard 7158300734726758",
    "Счет 35383033474447895560",
    "Visa Classic 6831982476737658",
    "Visa Platinum 8990922113665229",
    "Visa Gold 5999414228426353",
    "Счет 73654108430135874305",
]

my_date = "2024-03-11T02:26:18.671407"

mask_account_card(a)
mask_account_card(b)
mask_account_card(c)
mask_account_card(vh)
print(get_date(my_date))

my_date = "2024-03-11T02:26:18.671407"

mask_account_card(a)
mask_account_card(b)
mask_account_card(c)
mask_account_card(vh)
print(get_date(my_date))
print("hello")