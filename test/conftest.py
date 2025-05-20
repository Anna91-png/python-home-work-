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


@pytest.fixture
def full_transactions_list():
    return [
        {'amount': 100, 'currency': 'USD', 'description': 'Оплата заказа'},
        {'amount': 200, 'currency': 'EUR', 'description': 'Покупка'},
        {'amount': 50, 'currency': 'USD', 'description': 'Перевод'},
        {'amount': 300, 'currency': 'RUB', 'description': 'Снятие'},
    ]

@pytest.fixture
def usd_expected_list():
    return [
        {'amount': 100, 'currency': 'USD', 'description': 'Оплата заказа'},
        {'amount': 50, 'currency': 'USD', 'description': 'Перевод'},
    ]

@pytest.fixture
def rub_expected_list():
    return [
        {'amount': 300, 'currency': 'RUB', 'description': 'Снятие'},
    ]
@pytest.fixture
def transactions_sample():
    return [
        {
            "id": 1,
            "operationAmount": {
                "amount": "100",
                "currency": {"name": "USD", "code": "USD"}
            },
            "description": "USD transaction"
        },
        {
            "id": 2,
            "operationAmount": {
                "amount": "200",
                "currency": {"name": "RUB", "code": "RUB"}
            },
            "description": "RUB transaction"
        },
        {
            "id": 3,
            "operationAmount": {
                "amount": "300",
                "currency": {"name": "EUR", "code": "EUR"}
            },
            "description": "EUR transaction"
        },
    ]
