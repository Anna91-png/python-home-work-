import openpyxl
import os


def read_transactions_from_excel(file_path):
    """Считывает финансовые операции из Excel-файла.

    Args:
        file_path (str): Путь к Excel-файлу (xlsx).

    Returns:
        list[dict]: Список операций, каждая операция — это словарь с данными из файла.
    """
    transactions = []
    wb = openpyxl.load_workbook(file_path)
    ws = wb.active
    headers = [cell.value for cell in next(ws.iter_rows(min_row=1, max_row=1))]
    for row in ws.iter_rows(min_row=2, values_only=True):
        transaction = dict(zip(headers, row))
        transactions.append(transaction)
    return transactions


if __name__ == "__main__":
    print("Текущая рабочая директория:", os.getcwd())
    file_path = "../data/transactions_excel (1).xlsx"
    if not os.path.isfile(file_path):
        print(f"Файл не найден: {file_path}")
    else:
        transactions = read_transactions_from_excel(file_path)
        print(transactions)
