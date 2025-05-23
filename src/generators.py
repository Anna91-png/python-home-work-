import pytest
from src.decorators import log


@pytest.fixture(params=[None, "file"])
def log_destination(request, tmp_path):
    """Фикстура возвращает либо None (консоль), либо путь к временному файлу"""
    if request.param == "file":
        return str(tmp_path / "test_log.txt")
    return None


@pytest.mark.parametrize(
    "x, y, expected, raises_error",
    [
        (10, 2, 5.0, False),
        (10, 0, None, True),
    ]
)
def test_log_decorator(log_destination, capsys, x, y, expected, raises_error):
    """
    Тестирует декоратор log:
    - лог выводится в консоль или в файл
    - результат и ошибки логируются корректно
    """

    @log(filename=log_destination)
    def div(a: float, b: float) -> float:
        return a / b

    if raises_error:
        with pytest.raises(ZeroDivisionError):
            div(x, y)
    else:
        result = div(x, y)
        assert result == expected

    # Проверяем лог либо в файле, либо в консоли
    if log_destination is None:
        out = capsys.readouterr().out
        assert "Начало выполнения функции 'div'" in out
        assert "Конец выполнения функции 'div'" in out
        if raises_error:
            assert "Ошибка в функции 'div': ZeroDivisionError" in out
            assert f"args=({x}, {y})" in out
        else:
            assert f"Функция 'div' успешно завершена. Результат: {expected!r}" in out
    else:
        with open(log_destination, encoding="utf-8") as f:
            log_text = f.read()
        assert "Начало выполнения функции 'div'" in log_text
        assert "Конец выполнения функции 'div'" in log_text
        if raises_error:
            assert "Ошибка в функции 'div': ZeroDivisionError" in log_text
            assert f"args=({x}, {y})" in log_text
        else:
            assert f"Функция 'div' успешно завершена. Результат: {expected!r}" in log_text
