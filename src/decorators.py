import functools
import traceback
from typing import Any, Callable, Optional, TypeVar, cast

F = TypeVar("F", bound=Callable[..., Any])

def log(filename: Optional[str] = None) -> Callable[[F], F]:
    """
    Декоратор для логирования вызова и завершения функции, а также обработки исключений.

    При применении к функции, логирует:
    - начало выполнения функции, ее имя и переданные аргументы;
    - результат выполнения функции (или исключение, если оно возникло);
    - окончание выполнения функции;
    - трассировку стека при возникновении исключения.

    Если указан путь к файлу (`filename`), логирование будет происходить в этот файл.
    Если путь к файлу не задан, логирование производится в стандартный вывод (`print`).

    Args:
        filename (Optional[str]): Имя файла для записи логов. Если не указано, используется стандартный вывод.

    Returns:
        Callable[[F], F]: Декоратор для оборачивания функции логированием.

    Пример:
        @log("log.txt")
        def foo(x, y):
            return x + y

        foo(1, 2)
    """
    def decorator(func: F) -> F:
        @functools.wraps(func)
        def wrapper(*args: Any, **kwargs: Any) -> Any:
            logger: Optional[Any] = None
            close_logger: bool

            def write(msg: str) -> None:
                if logger is not None:
                    logger.write(msg + '\n')
                else:
                    print(msg)

            if filename:
                logger = open(filename, 'a', encoding='utf-8')
                close_logger = True
            else:
                logger = None
                close_logger = False

            try:
                write(f"Начало выполнения функции '{func.__name__}' с args={args}, kwargs={kwargs}")
                result = func(*args, **kwargs)
                write(f"Функция '{func.__name__}' успешно завершена. Результат: {result!r}")
                return result
            except Exception as e:
                error_type = type(e).__name__
                write(
                    f"Ошибка в функции '{func.__name__}': {error_type}. "
                    f"Аргументы: args={args}, kwargs={kwargs}"
                )
                write("Traceback:\n" + ''.join(traceback.format_exc()))
                raise
            finally:
                write(f"Конец выполнения функции '{func.__name__}'")
                if logger is not None and close_logger:
                    logger.close()
        return cast(F, wrapper)
    return decorator