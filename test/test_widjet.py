import pytest
from src.widjet import mask_account_card
from datetime import datetime

@pytest.mark.parametrize("input_data, expected", [
    # Тесты для карт
    (1234123412341234, "**1234"),          # Обычная карта (16 цифр)
    ("1234567812345678", "**5678"),        # Карта как строка (16 цифр)
    (1234567812345, "**2345"),             # Карта с длиной 13 цифр
    ("123456781234", "**1234"),            # Карта с длиной 12 цифр (граничный случай)

    # Тесты для счетов
    (12345678, "**5678"),                  # Счет (8 цифр)
    ("0000000000000000", "**0000"),        # Счет с нулями
    (1234, "**1234"),                      # Минимальная длина счета
    ("9999", "**9999"),                    # Счет как строка (4 цифры)

    # Некорректные данные
    ("abcd1234", ""),                      # Номер содержит нецифровые символы
    ("", ""),                              # Пустая строка
    (None, ""),                            # None
    (123, ""),                             # Номер слишком короткий
    ("abc", ""),                           # Содержит только буквы
])
def test_mask_account_card(input_data, expected):
    assert mask_account_card(input_data) == expected

# Предполагаемая функция для преобразования дат

def get_date(date_string):
    """
    Преобразует строку с датой в объект datetime.
    Поддерживает несколько форматов дат.

    :param date_string: строка с датой
    :return: объект datetime
    :raises ValueError: если дата не может быть распознана
    """
    supported_formats = [
        '%Y-%m-%d',        # 2025-05-15
        '%d-%m-%Y',        # 15-05-2025
        '%m/%d/%Y',        # 05/15/2025
        '%d %b %Y',        # 15 May 2025
        '%d %B %Y',        # 15 May 2025
        '%Y.%m.%d',        # 2025.05.15
    ]
    for fmt in supported_formats:
        try:
            return datetime.strptime(date_string, fmt)
        except ValueError:
            continue
    raise ValueError(f"Некорректный формат даты: {date_string}")

# Тестовые данные для параметризации

@pytest.mark.parametrize("input_date, expected", [
    # Проверка стандартных форматов
    ('2025-05-15', datetime(2025, 5, 15)),
    ('15-05-2025', datetime(2025, 5, 15)),
    ('05/15/2025', datetime(2025, 5, 15)),
    ('15 May 2025', datetime(2025, 5, 15)),
    ('15 May 2025', datetime(2025, 5, 15)),
    ('2025.05.15', datetime(2025, 5, 15)),
    # Проверка граничных случаев
    ('0001-01-01', datetime(1, 1, 1)),  # Минимальная допустимая дата
    ('9999-12-31', datetime(9999, 12, 31)),  # Максимальная допустимая дата
    # Проверка нестандартных строк
    ('01 Jan 2025', datetime(2025, 1, 1)),
    ('31 December 2999', datetime(2999, 12, 31)),
])
def test_get_date_valid(input_date, expected):
    assert get_date(input_date) == expected

# Тесты на некорректные данные

@pytest.mark.parametrize("input_date", [
    '15/05/2025',         # Неподдерживаемый формат
    '2025-13-01',         # Неверный месяц
    '2025-00-10',         # Неверный месяц
    '2025-05-32',         # Неверный день
    'abcd-ef-gh',         # Полностью неверный формат
    '',                   # Пустая строка
    'No date here',       # Строка без даты
  ])
def test_get_date_invalid(input_date):
    with pytest.raises(ValueError):
        get_date(input_date)


