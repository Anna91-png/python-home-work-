from typing import Optional, Union

def mask_account_card(account: Optional[Union[str, int]]) -> str:
    """
    Универсальная функция маскирует номер карты/счета (строку или число).
    Если входные данные некорректны — возвращает пустую строку.
    """
    if account is None:
        return ""
    account_str = str(account)
    # Маскируем только если все символы — цифры и длина не менее 4
    if account_str.isdigit() and len(account_str) >= 4:
        return "**" + account_str[-4:]
    # Если меньше 4 цифр, или не только цифры — возвращаем ""
    return ""

def get_mask_card_number(card_number: str) -> str:
    return mask_account_card(card_number)

def get_mask_account(account_number: str) -> str:
    return mask_account_card(account_number)

def get_date(date: str) -> str:
    """
    Функция, которая возвращает строку с датой в формате "ДД.ММ.ГГГГ"
    """
    date_parts = date[:10].split("-")[::-1]
    return ".".join(date_parts)