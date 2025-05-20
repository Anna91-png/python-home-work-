from typing import Any

import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions

# === Фикстуры ===

@pytest.fixture
def full_transactions_list() -> list[dict[str, Any]]:
    return [
        {'amount': 100, 'currency': 'USD', 'description': 'Оплата заказа'},
        {'amount': 200, 'currency': 'EUR', 'description': 'Покупка'},
        {'amount': 50, 'currency': 'USD', 'description': 'Перевод'},
        {'amount': 300, 'currency': 'RUB', 'description': 'Снятие'},
        {'amount': 150, 'currency': 'USD'},  # без description
    ]

@pytest.fixture
def usd_expected_list() -> list[dict[str, Any]]:
    return [
        {'amount': 100, 'currency': 'USD', 'description': 'Оплата заказа'},
        {'amount': 50, 'currency': 'USD', 'description': 'Перевод'},
        {'amount': 150, 'currency': 'USD'},
    ]

@pytest.fixture
def rub_expected_list() -> list[dict[str, Any]]:
    return [
        {'amount': 300, 'currency': 'RUB', 'description': 'Снятие'},
    ]

# === Тесты filter_by_currency ===

@pytest.mark.parametrize(
    "money, expected_fixture",
    [
        ("USD", "usd_expected_list"),
        ("RUB", "rub_expected_list"),
    ],
)
def test_positive_filter_by_currency(full_transactions_list, money, expected_fixture, request):
    expected = request.getfixturevalue(expected_fixture)
    result = list(filter_by_currency(full_transactions_list, money))
    assert result == expected

@pytest.mark.parametrize(
    "money, expected",
    [
        ("EUR", [{'amount': 200, 'currency': 'EUR', 'description': 'Покупка'}]),
        ("GBP", []),
    ]
)
def test_negative_filter_by_currency(full_transactions_list, money, expected):
    result = list(filter_by_currency(full_transactions_list, money))
    assert result == expected

# === Тесты transaction_descriptions ===

@pytest.mark.parametrize(
    "transactions, expected",
    [
        (
            [
                {'amount': 100, 'currency': 'USD', 'description': 'Оплата заказа'},
                {'amount': 200, 'currency': 'EUR', 'description': 'Возврат'},
            ],
            [
                "Операция: 100 USD. Оплата заказа",
                "Операция: 200 EUR. Возврат",
            ]
        ),
        (
            [{'amount': 50, 'currency': 'USD'}],
            ["Операция: 50 USD."]
        ),
        (
            [{'description': 'Только описание'}],
            ["Операция: N/A N/A. Только описание"]
        ),
        (
            [],
            []
        ),
    ]
)
def test_transaction_descriptions(transactions, expected):
    result = list(transaction_descriptions(transactions))
    assert result == expected

# === Тесты card_number_generator ===

@pytest.mark.parametrize(
    "start, end, expected",
    [
        (
            "0000 0000 0000 0001", "0000 0000 0000 0003",
            ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]
        ),
        (
            1, 3,
            ["0000 0000 0000 0001", "0000 0000 0000 0002", "0000 0000 0000 0003"]
        ),
        (
            "9999 9999 9999 9999", "9999 9999 9999 9999",
            ["9999 9999 9999 9999"]
        ),
        (
            1234567890123456, 1234567890123457,
            ["1234 5678 9012 3456", "1234 5678 9012 3457"]
        ),
    ]
)
def test_card_number_generator(start, end, expected):
    result = list(card_number_generator(start, end))
    assert result == expected