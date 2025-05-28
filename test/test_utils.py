import json
from unittest.mock import patch, mock_open
from src. utils import get_transactions

def test_get_transactions_list():
    expected = [
        {'amount': 100, 'currency': 'USD'},
        {'amount': 200, 'currency': 'EUR'}
    ]
    mock_data = json.dumps(expected)
    with patch("builtins.open", mock_open(read_data=mock_data)):
        with patch("os.path.exists", return_value=True):
            result = get_transactions("some_path.json")
            assert result == expected
def test_get_transactions_file_not_found(fixture_for_expected_path_file: str) -> None:
    """Тест на случай, если файл не найден"""

    with patch("builtins.open", mock_open()) as mocked_open:
        mocked_open.side_effect = FileNotFoundError  # Симулируем ошибку "файл не найден"
        transactions_list = get_transactions(fixture_for_expected_path_file)
        assert transactions_list == []  # Ожидаем пустой список

def test_get_transactions_invalid_json(fixture_for_expected_path_file: str) -> None:
    """Тест на случай, если файл содержит некорректный JSON"""

    with patch("builtins.open", mock_open(read_data="invalid json")):
        transactions_list = get_transactions(fixture_for_expected_path_file)
        assert transactions_list == []  # Ожидаем пустой список

def test_get_transactions_not_a_list(fixture_for_expected_path_file: str) -> None:
    """Тест на случай, если JSON содержит не список"""

    mock_data = json.dumps({"not": "a list"})
    with patch("builtins.open", mock_open(read_data=mock_data)):
        transactions_list = get_transactions(fixture_for_expected_path_file)
        assert transactions_list == []  # Ожидаем пустой список