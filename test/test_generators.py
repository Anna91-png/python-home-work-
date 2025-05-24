import pytest

from src.generators import card_number_generator, filter_by_currency, transaction_descriptions


@pytest.mark.parametrize(
    "transactions, money, expected",
    [
        (
            [
                {"operationAmount": {"currency": {"code": "USD"}}, "description": "usd"},
                {"operationAmount": {"currency": {"code": "RUB"}}, "description": "rub"},
            ],
            "USD",
            [{"operationAmount": {"currency": {"code": "USD"}}, "description": "usd"}],
        ),
        (
            [
                {"operationAmount": {"currency": {"code": "RUB"}}, "description": "rub"},
            ],
            "USD",
            [],
        ),
        (
            [],
            "USD",
            [],
        ),
        (
            [
                {"operationAmount": {}, "description": "no currency"},
            ],
            "USD",
            [],
        ),
    ],
)
def test_filter_by_currency_param(transactions, money, expected):
    result = list(filter_by_currency(transactions, money))
    assert result == expected


@pytest.mark.parametrize(
    "transactions, expected",
    [
        (
            [{"description": "first"}, {"description": "second"}],
            ["first", "second"],
        ),
        (
            [{"description": "only"}],
            ["only"],
        ),
        (
            [],
            [],
        ),
        (
            [{"id": 1}, {"description": "desc2"}],
            ["", "desc2"],
        ),
    ],
)
def test_transaction_descriptions_param(transactions, expected):
    result = list(transaction_descriptions(transactions))
    assert result == expected


@pytest.mark.parametrize(
    "start, end, expected",
    [
        (1, 3, [
            "0000 0000 0000 0001",
            "0000 0000 0000 0002",
            "0000 0000 0000 0003",
        ]),
        ("5", "7", [
            "0000 0000 0000 0005",
            "0000 0000 0000 0006",
            "0000 0000 0000 0007",
        ]),
        (1234567890123456, 1234567890123456, [
            "1234 5678 9012 3456",
        ]),
        (0, 0, [
            "0000 0000 0000 0000",
        ]),
    ],
)
def test_card_number_generator_param(start, end, expected):
    result = list(card_number_generator(start, end))
    assert result == expected
