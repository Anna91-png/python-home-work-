from typing import List

from src.mask import get_mask_account
from src.mask import get_mask_card_number


def mask_account_card(input_data):
    """
    Определяет тип входных данных (карта или счет) и применяет соответствующую маскировку.
    Карты: Маскируются все символы, кроме последних 4.
    Счета: Маскируются все символы, кроме последних 4.
    Если данные некорректны, возвращается пустая строка.

    :param input_data: str или int, номер карты или счета
    :return: str, замаскированные данные
    """
    if not input_data:
        return ""

    # Преобразуем в строку, если это число
    input_data = str(input_data)

    # Карты обычно имеют длину 16 цифр
    if input_data.isdigit():
        if 13 <= len(input_data) <= 16:  # Типичная длина номера карты
            return "**" + input_data[-4:]
        elif len(input_data) >= 4:  # Для номеров счетов минимальная длина — 4 символа
            return "**" + input_data[-4:]

    # Если входные данные некорректны
    return ""

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
#print(get_date(my_date))
