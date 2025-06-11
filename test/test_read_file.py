import unittest
from unittest.mock import patch, mock_open

from src.read_files import read_transactions_from_csv
from src.read_files import read_transactions_from_excel

class Cell:
    def __init__(self, value):
        self.value = value

class TestReadTransactions(unittest.TestCase):
    @patch("csv.DictReader")
    @patch("builtins.open", new_callable=mock_open)
    def test_read_transactions_from_csv(self, mock_file, mock_dictreader):
        mock_dictreader.return_value = [
            {"date": "2024-01-01", "amount": "100", "category": "Food"}
        ]
        result = read_transactions_from_csv("test.csv")
        self.assertEqual(result, [{"date": "2024-01-01", "amount": "100", "category": "Food"}])

    @patch("openpyxl.load_workbook")
    def test_read_transactions_from_excel(self, mock_load_wb):
        mock_ws = unittest.mock.MagicMock()
        # Для заголовков
        header_row = [Cell("date"), Cell("amount"), Cell("category")]
        # Для данных
        data_row = [Cell("2024-01-01"), Cell(100), Cell("Food")]

        def iter_rows_side_effect(*args, **kwargs):
            if kwargs.get("min_row") == 1 and kwargs.get("max_row") == 1:
                return iter([header_row])
            elif kwargs.get("min_row") == 2:
                return iter([data_row])
            else:
                return iter([])

        mock_ws.iter_rows.side_effect = iter_rows_side_effect
        mock_wb = unittest.mock.MagicMock()
        mock_wb.active = mock_ws
        mock_load_wb.return_value = mock_wb

        result = read_transactions_from_excel("test.xlsx")
        # Приводим все значения к .value (как делает реальная функция)
        cleaned_result = [
            {k: v.value if hasattr(v, "value") else v for k, v in item.items()}
            for item in result
        ]
        expected = [{"date": "2024-01-01", "amount": 100, "category": "Food"}]
        self.assertEqual(cleaned_result, expected)

if __name__ == "__main__":
    unittest.main()