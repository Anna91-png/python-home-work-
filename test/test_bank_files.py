import unittest
from unittest.mock import patch, mock_open, MagicMock
from src.bank_search import process_bank_search
from src.bank_operation import process_bank_operations
from src.main import (
    load_json_transactions,
    load_csv_transactions,
    load_xlsx_transactions,
    filter_by_status,
    sort_by_date,
    filter_by_rub,
    pretty_print_transactions
)

class TestBankUtils(unittest.TestCase):

    def test_process_bank_search(self):
        data = [
            {"id": 1, "description": "Оплата в магазине"},
            {"id": 2, "description": "Перевод на карту"},
            {"id": 3, "description": "Оплата мобильной связи"},
        ]
        result = process_bank_search(data, "оплата")
        self.assertEqual(len(result), 2)
        self.assertTrue(all("Оплата" in op["description"] for op in result))

    def test_process_bank_operations(self):
        data = [
            {"description": "Оплата"},
            {"description": "Перевод"},
            {"description": "Оплата"},
            {"description": "Снятие"},
        ]
        categories = ["Оплата", "Перевод", "Снятие"]
        result = process_bank_operations(data, categories)
        self.assertEqual(result, {"Оплата": 2, "Перевод": 1, "Снятие": 1})

    @patch("builtins.open", new_callable=mock_open, read_data='[{"status": "EXECUTED", "description": "Оплата", "date": "2022-01-01"}]')
    def test_load_json_transactions(self, mock_file):
        result = load_json_transactions("fake.json")
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]["status"], "EXECUTED")

    @patch("builtins.open", new_callable=mock_open, read_data='status,description,date\nEXECUTED,Оплата,2022-01-01\n')
    def test_load_csv_transactions(self, mock_file):
        result = load_csv_transactions("fake.csv")
        self.assertIsInstance(result, list)
        self.assertEqual(result[0]["status"], "EXECUTED")

    @patch("src.main.openpyxl")
    def test_load_xlsx_transactions(self, mock_openpyxl):
        # Мокаем workbook и worksheet
        mock_ws = MagicMock()
        # Для заголовков (первая строка)
        header_row = [MagicMock(value='status'), MagicMock(value='description'), MagicMock(value='date')]
        # Для данных (вторая строка) — возвращаем кортеж значений, а не MagicMock!
        data_row = ('EXECUTED', 'Оплата', '2022-01-01')
        # iter_rows должен вернуть итератор: сначала строка-заголовок, потом строка-данные
        mock_ws.iter_rows.side_effect = [
            iter([header_row]),   # для next(ws.iter_rows(...)) (заголовки)
            iter([data_row])      # для for row in ws.iter_rows(...): (данные)
        ]
        mock_wb = MagicMock()
        mock_wb.active = mock_ws
        mock_openpyxl.load_workbook.return_value = mock_wb

        result = load_xlsx_transactions("fake.xlsx")
        assert isinstance(result, list)
        assert result[0]["status"] == "EXECUTED"

    def test_filter_by_status(self):
        data = [
            {"status": "EXECUTED"},
            {"status": "executed"},
            {"status": "CANCELED"},
        ]
        filtered = filter_by_status(data, "EXECUTED")
        self.assertEqual(len(filtered), 2)
        self.assertTrue(all(op["status"].lower() == "executed" for op in filtered))

    def test_sort_by_date(self):
        data = [
            {"date": "2022-01-02"},
            {"date": "2022-01-01"},
        ]
        sorted_data = sort_by_date(data, reverse=False)
        self.assertEqual(sorted_data[0]["date"], "2022-01-01")

    def test_filter_by_rub(self):
        data = [
            {"sum": "1000 руб."},
            {"sum": "2000 USD"},
            {"currency": "RUB"},
        ]
        filtered = filter_by_rub(data)
        self.assertEqual(len(filtered), 2)

    @patch("builtins.print")
    def test_pretty_print_transactions(self, mock_print):
        data = [
            {"date": "2022-01-01", "description": "Оплата", "sum": "1000 руб."},
        ]
        pretty_print_transactions(data)
        mock_print.assert_any_call("\nВсего банковских операций в выборке: 1\n")
        mock_print.assert_any_call("01.01.2022 Оплата")
        mock_print.assert_any_call("Сумма: 1000 руб.\n")

    @patch("builtins.input", side_effect=["1", "fake.json", "EXECUTED", "нет", "нет", "нет"])
    @patch("builtins.print")
    @patch("src.main.load_json_transactions", return_value=[
        {"status": "EXECUTED", "description": "Оплата", "date": "2022-01-01", "sum": "1000 руб."}
    ])
    def test_main_json_flow(self, mock_load, mock_print, mock_input):
        # Импортируем main внутри теста, чтобы patch сработал
        from src.main import main
        main()
        mock_print.assert_any_call('Операции отфильтрованы по статусу "EXECUTED"')
        mock_print.assert_any_call("Распечатываю итоговый список транзакций...")

if __name__ == "__main__":
    unittest.main()