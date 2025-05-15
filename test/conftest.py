import pytest

@pytest.fixture
def card_number():
    return "1234567812345678"

@pytest.fixture
def account_number():
    return "987654321"

@pytest.fixture
def account_card_number():
    # Тестовые данные для функции mask_account_card
    return "1234567812345678"

@pytest.fixture
def get_date():
    # Фикстура для фиксации текущей даты
    return (2025, 5, 14)
 