Виджет «Банкинг»
## Описание проекта
IT-отдел крупного банка делает новую фичу для личного кабинета клиента. Это виджет, который показывает несколько последних успешных банковских операций клиента. 
Применяемые функции:
## Установка:

1. Клонируйте репозиторий:

git clone https://github.com/Anna91-png/python-home-work-

2. Установите зависимости:

pip install -r requirements.txt
##  Использованные модули 
## модуль masks.py
Модуль предоставляет функции для работы с банковскими картами 
- 'get_mask_card_number' : принимает на вход номер карты в виде числа и возвращает маску номера по правилу 
XXXX XX** **** XXXX
- 'get_mask_account' - принимает на вход номер счета в виде числа и возвращает маску номера по правилу 
**XXXX

## Модуль widjet.py
Этот модуль  содержит функции для работы с новыми возможностями приложения.
- 'get_date' , которая принимает на вход строку с датой в формате"2024-03-11T02:26:18.671407" и возвращает строку с датой в формате"ДД.ММ.ГГГГ" (11.03.2024").
 - 'mask_account_card' , которая умеет обрабатывать информацию как о картах, так и о счетах.

## Модуль processing.py
Модуль предоставляет функции для работы с банковскими операциями:

- `filter_by_state` Функция принимает список словарей и значение для ключа и возвращает новый
    список содержащий только те словари у которых ключ содержит переданное значение.
- 
- `sort_by_date`Функция принимает список и сортирует его по убыванию.

##  Модульное тестирование:

Тесты подготовлены отдельными файлами под каждый модуль функционала:
test_masks.py
test_widget.py
test_processing.py

что входит в тесты:

# Модуль masks

- get_mask_card_number

Тестирование правильности маскирования номера карты.
Проверка работы функции на различных входных форматах номеров карт, включая граничные случаи и нестандартные длины номеров.
Проверка, что функция корректно обрабатывает входные строки, где отсутствует номер карты.

- get_mask_account

Тестирование правильности маскирования номера счета.
Проверка работы функции с различными форматами и длинами номеров счетов.
Проверка, что функция корректно обрабатывает входные данные, где номер счета меньше ожидаемой длины.
Модуль widget

- mask_account_card

Тесты для проверки, что функция корректно распознает и применяет нужный тип маскировки в зависимости от типа входных данных (карта или счет).
Параметризованные тесты с разными типами карт и счетов для проверки универсальности функции.
Тестирование функции на обработку некорректных входных данных и проверка ее устойчивости к ошибкам.

 
- get_date
:
Тестирование правильности преобразования даты.
Проверка работы функции на различных входных форматах даты, включая граничные случаи и нестандартные строки с датами.
Проверка, что функция корректно обрабатывает входные строки, где отсутствует дата.

# Модуль processing

- filter_by_state
:
Тестирование фильтрации списка словарей по заданному статусу 
state
.
Проверка работы функции при отсутствии словарей с указанным статусом 
state
 в списке.
Параметризация тестов для различных возможных значений статуса
state

- sort_by_date
:
Тестирование сортировки списка словарей по датам в порядке убывания и возрастания.
Проверка корректности сортировки при одинаковых датах.
Тесты на работу функции с некорректными или нестандартными форматами дат.

## Проделанная работа

# Реализованы функции-генераторы:
    - `filter_by_currency` — фильтрует список транзакций по заданной валюте и возвращает подходящие элементы.
    - `transaction_descriptions` — формирует строковые описания транзакций.
    - `card_number_generator` — генерирует номера банковских карт в заданном диапазоне в формате `XXXX XXXX XXXX XXXX`.
- Написаны и оформлены автотесты на каждую функцию с использованием фикстур и параметризации (`pytest`).
- Все функции и тесты снабжены подробными комментариями и докстрингами.
- Проведена ручная и автоматическая проверка корректности работы генераторов.
decorators.py - в модуле реализован декоратор, который позволяет:

 - логировать работу функции и ее результат как в файл, так и в консоль;
декоратор может принимать необязательный аргумент filename, который определяет имя файла, в который будут записываться логи. Если filename не задан, то логи выводятся в консоль;
