import logging

# Настройка логгера для модуля masks
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

file_handler = logging.FileHandler('masks.log', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)

file_formatter = logging.Formatter('%(asctime)s %(module)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
file_handler.setFormatter(file_formatter)

if not any(isinstance(h, logging.FileHandler) for h in logger.handlers):
    logger.addHandler(file_handler)


def get_mask_card_number(number_card: str) -> str:
    """
    Функция get_mask_card_number принимает на вход номер
    карты в виде числа и возвращает маску номера по правилу
    XXXX XX** **** XXXX
    """
    try:
        if len(number_card) < 16:
            logger.error(f"Передано менее 16 символов для маскировки карты: {number_card}")
            raise ValueError("количество переданного меньше 16")
        masked = f"{number_card[0:4]} {number_card[4:6]}** **** {number_card[-4:]}"
        logger.info(f"Маска карты успешно создана: {masked}")
        return masked
    except Exception as e:
        logger.error(f"Ошибка при маскировке карты: {e}")
        raise


def get_mask_account(account_number: str) -> str:
    """
    Маскирует номер банковского счета, оставляя видимыми последние 4 цифры.

    :param account_number: Номер счета в виде строки.
    :return: Замаскированный номер счета в формате **XXXX или сообщение об ошибке.
    """
    try:
        account_number_str = str(account_number).replace(" ", "")

        if len(account_number_str) < 4 or not account_number_str.isdigit():
            logger.error(f"Неверный формат номера счёта: {account_number}")
            return "Неверный формат номера счёта"

        masked = "**" + account_number_str[-4:]
        logger.info(f"Маска счёта успешно создана: {masked}")
        return masked
    except Exception as e:
        logger.error(f"Ошибка при маскировке счёта: {e}")
        return "Ошибка при обработке номера счёта"
