def get_mask_card_number(number_card: str) -> str:
    """
    Функция get_mask_card_number принимает на вход номер
    карты в виде числа и возвращает маску номера по правилу
    XXXX XX** **** XXXX
    """
    if len(number_card)<16:
        raise ValueError("количество переданного меньше 16")
    return f"{number_card[0:4]} {number_card[4:6]}** **** {number_card[-4:]}"


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счета, оставляя видимыми последние 4 цифры.

    :param account_number: Номер счета в виде строки.
    :return: Замаскированный номер счета в формате **XXXX или сообщение об ошибке.
    """
    # Убираем пробелы и преобразуем в строку
    account_number_str = str(account_number).replace(" ", "")

    # Проверка длины и формата
    if len(account_number_str) < 4 or not account_number_str.isdigit():
        return "Неверный формат номера счёта"

    # Маскировка: скрываем все, кроме последних 4 цифр
    masked = "**" + account_number_str[-4:]
    return masked