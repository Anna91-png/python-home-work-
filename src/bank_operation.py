from typing import List, Dict

def process_bank_operations(data: List[Dict], categories: List[str]) -> Dict[str, int]:
    """
    Подсчитывает количество банковских операций по заданным категориям.
    Категории ищутся по точному совпадению в поле 'description'.

    :param data: Список словарей с банковскими операциями.
    :param categories: Список категорий для подсчёта.
    :return: Словарь, где ключ — категория, а значение — количество операций в этой категории.
    """
    result = {category: 0 for category in categories}
    for operation in data:
        operation_desc = operation.get("description", "")
        for category in categories:
            if operation_desc == category:
                result[category] += 1
    return result

if __name__ == "__main__":
    # Пример данных для проверки
    data = [
        {"id": 1, "description": "Оплата товаров"},
        {"id": 2, "description": "Снятие наличных"},
        {"id": 3, "description": "Оплата товаров"},
        {"id": 4, "description": "Перевод"},
        {"id": 5, "description": "Снятие наличных"},
        {"id": 6, "description": "Пополнение"},
    ]
    categories = ["Оплата товаров", "Снятие наличных", "Перевод"]
    result = process_bank_operations(data, categories)
    print(result)
    # Ожидаемый вывод: {'Оплата товаров': 2, 'Снятие наличных': 2, 'Перевод': 1}