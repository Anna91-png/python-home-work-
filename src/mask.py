def get_mask_card_number(number_card: str) -> str:
    """
    Функция get_mask_card_number принимает на вход номер
    карты в виде числа и возвращает маску номера по правилу
    XXXX XX** **** XXXX
    """
    if len(number_card)<16:
        raise ValueError("количество переданного меньше 16")
    return f"{number_card[0:4]} {number_card[4:6]}** **** {number_card[-4:]}"


def get_mask_account(number_card: str) -> str:
    """
    Функция get_mask_account принимает на вход номер
    счета в виде числа и возвращает маску номера по
    правилу **XXXX
    """
    return f"**{number_card[-4:]}"
