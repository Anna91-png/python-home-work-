import pytest
from src.mask import get_mask_card_number

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
