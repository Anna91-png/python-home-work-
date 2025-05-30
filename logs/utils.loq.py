import logging
import json
import os

# Настройка логгера для модуля utils
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)  # Уровень не ниже DEBUG

# Хендлер для записи логов в файл
file_handler = logging.FileHandler('utils.log', encoding='utf-8')
file_handler.setLevel(logging.DEBUG)  # Уровень не ниже DEBUG

# Форматтер для логов: время, модуль, уровень, сообщение
file_formatter = logging.Formatter('%(asctime)s %(module)s %(levelname)s: %(message)s', datefmt='%Y-%m-%d %H:%M:%S')
file_handler.setFormatter(file_formatter)

# Добавляем handler, если еще не добавлен (чтобы избежать дублирования при повторном импорте)
if not any(isinstance(h, logging.FileHandler) for h in logger.handlers):
    logger.addHandler(file_handler)

def get_transactions(json_path: str) -> list:
    """
    Считывает JSON-файл и возвращает список словарей с транзакциями.
    Если файл отсутствует, пуст, или не содержит список — возвращает пустой список.
    """
    if not os.path.exists(json_path):
        logger.error(f"Файл не найден: {json_path}")
        return []
    try:
        with open(json_path, encoding="utf-8") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError as e:
                logger.error(f"Ошибка декодирования JSON в файле {json_path}: {e}")
                return []
            if isinstance(data, list):
                logger.info(f"Успешно считано {len(data)} транзакций из {json_path}")
                return data
            else:
                logger.error(f"Данные в файле {json_path} не являются списком")
                return []
    except (OSError, IOError) as e:
        logger.error(f"Ошибка при работе с файлом {json_path}: {e}")
        return []