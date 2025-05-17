import pytest
from src.mask import get_mask_card_number,get_mask_account

# Тесты для проверки верных номеров карт
@pytest.mark.parametrize("card_number, expected", [
    ("8234567890123456", "8234 56** **** 3456"),
    ("7234-5678-9012-3456", '7234 -5** **** 3456'),
    ("6234 5678 9012 3456", "6234  5** **** 3456")
])
def test_valid_card_numbers(card_number, expected):
    assert get_mask_card_number(card_number) == expected

# Тесты для проверки некорректных номеров
@pytest.mark.parametrize("card_number", [
    "1234",
    "123456789012",
    "",

])
def test_invalid_card_numbers(card_number):
    with pytest.raises(ValueError):
        get_mask_card_number(card_number)

# Тесты для нестандартных форматов
@pytest.mark.parametrize("card_number, expected", [
    ("1234/5678/9012/3456", "1234 /5** **** 3456"),
    ("1234_5678_9012_3456", '1234 _5** **** 3456')
])
def test_special_formats(card_number, expected):
    assert get_mask_card_number(card_number) == expected

    @pytest.mark.parametrize("account_number, expected", [
        (1234123412341234, "**1234"),  # Обычная длина номера
        ("1234567812345678", "**5678"),  # Номер передан как строка
        (1234, "**1234"),  # Минимальная длина
        ("0000000000000000", "**0000"),  # Номер состоит из нулей
        ("abcd1234", ""),  # Номер содержит нецифровые символы
        ("", ""),  # Пустая строка
        (None, ""),  # None
        (123, ""),  # Слишком короткий номер
        ("123", ""),  # Слишком короткая строка
    ])
    def test_get_mask_account(account_number, expected):
        assert get_mask_account(account_number) == expected