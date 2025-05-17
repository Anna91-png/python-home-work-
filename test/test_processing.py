import pytest

from src.processing import filter_by_state
from src.processing import sort_by_date

# Предполагаемая функция для фильтрации
def filter_by_state(data, state):
    """
    Фильтрует список словарей по заданному статусу state.

    :param data: список словарей
    :param state: строка, статус для фильтрации
    :return: список словарей с указанным статусом
    """
    return [item for item in data if item.get('state') == state]

# Тестовые данные для параметризации
@pytest.mark.parametrize("input_data, state, expected", [
    # Список содержит элементы с указанным статусом
    ([{'id': 1, 'state': 'active'}, {'id': 2, 'state': 'inactive'}], 'active', [{'id': 1, 'state': 'active'}]),
    ([{'id': 1, 'state': 'active'}, {'id': 2, 'state': 'active'}], 'active', [{'id': 1, 'state': 'active'}, {'id': 2, 'state': 'active'}]),
    # Нет элементов с указанным статусом
    ([{'id': 1, 'state': 'active'}, {'id': 2, 'state': 'inactive'}], 'pending', []),
    # Пустой список
    ([], 'active', []),
    # Разные значения статуса
    ([{'id': 1, 'state': 'active'}, {'id': 2, 'state': 'inactive'}, {'id': 3, 'state': 'pending'}], 'inactive', [{'id': 2, 'state': 'inactive'}]),
    # Отсутствие ключа 'state' в одном из элементов
    ([{'id': 1, 'state': 'active'}, {'id': 2}, {'id': 3, 'state': 'pending'}], 'active', [{'id': 1, 'state': 'active'}]),
])
def test_filter_by_state(input_data, state, expected):
    assert filter_by_state(input_data, state) == expected

    # Предполагаемая функция для сортировки
    def sort_by_date(data, date_key, reverse=False):
        """
        Сортирует список словарей по дате.

        :param data: список словарей
        :param date_key: ключ, содержащий дату
        :param reverse: порядок сортировки (False для возрастания, True для убывания)
        :return: отсортированный список
        """
        try:
            return sorted(data, key=lambda x: datetime.strptime(x[date_key], '%Y-%m-%d'), reverse=reverse)
        except (ValueError, KeyError) as e:
            raise ValueError(f"Некорректный формат данных или отсутствует ключ '{date_key}'") from e

    # Тестовые данные для параметризации
    @pytest.mark.parametrize("input_data, date_key, reverse, expected", [
        # Сортировка по возрастанию
        ([{'id': 1, 'date': '2025-05-10'}, {'id': 2, 'date': '2025-05-15'}], 'date', False,
         [{'id': 1, 'date': '2025-05-10'}, {'id': 2, 'date': '2025-05-15'}]),
        # Сортировка по убыванию
        ([{'id': 1, 'date': '2025-05-10'}, {'id': 2, 'date': '2025-05-15'}], 'date', True,
         [{'id': 2, 'date': '2025-05-15'}, {'id': 1, 'date': '2025-05-10'}]),
        # Одинаковые даты
        ([{'id': 1, 'date': '2025-05-10'}, {'id': 2, 'date': '2025-05-10'}], 'date', False,
         [{'id': 1, 'date': '2025-05-10'}, {'id': 2, 'date': '2025-05-10'}]),
        # Смешанные даты
        ([{'id': 1, 'date': '2025-05-15'}, {'id': 2, 'date': '2025-05-10'}, {'id': 3, 'date': '2025-05-12'}], 'date',
         False,
         [{'id': 2, 'date': '2025-05-10'}, {'id': 3, 'date': '2025-05-12'}, {'id': 1, 'date': '2025-05-15'}]),
    ])
    def test_sort_by_date(input_data, date_key, reverse, expected):
        assert sort_by_date(input_data, date_key, reverse) == expected

    # Тесты на некорректные данные
    @pytest.mark.parametrize("input_data, date_key, reverse, expected_exception", [
        # Некорректный формат даты
        ([{'id': 1, 'date': '2025/05/10'}, {'id': 2, 'date': '2025-05-15'}], 'date', False, ValueError),
        # Отсутствие ключа даты
        ([{'id': 1, 'timestamp': '2025-05-10'}, {'id': 2, 'timestamp': '2025-05-15'}], 'date', False, ValueError),
        # Пустой список
        ([], 'date', False, None),  # Ожидается, что функция вернет пустой список
    ])
    def test_sort_by_date_exceptions(input_data, date_key, reverse, expected_exception):
        if expected_exception:
            with pytest.raises(expected_exception):
                sort_by_date(input_data, date_key, reverse)
        else:
            assert sort_by_date(input_data, date_key, reverse) == []

    # Дополнительный тест на нестандартный формат даты
    def test_sort_by_date_non_standard_format():
        input_data = [{'id': 1, 'date': '10-05-2025'}, {'id': 2, 'date': '15-05-2025'}]
        date_key = 'date'
        reverse = False
        with pytest.raises(ValueError):
            sort_by_date(input_data, date_key, reverse)