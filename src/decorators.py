from datetime import datetime
from functools import wraps
import pandas as pd
import os


def create_report(filename: str = "report"):
    """Декоратор для функций-отчетов, который записывает в файл результат,
    который возвращает функция, формирующая отчет.
    Без параметра - имя файла генерируется автоматически.
    С параметром - используется переданное имя файла"""

    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)

            # Определяем путь к папке data
            PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
            DATA_DIR = os.path.join(PROJECT_ROOT, "data")
            os.makedirs(DATA_DIR, exist_ok=True)  # Создаем папку если нет

            # Определяем имя файла
            if filename is None:
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                report_filename = f"{func.__name__}_{timestamp}.txt"
            else:
                report_filename = f"{filename}.txt"

            # Полный путь к файлу в папке data
            report_filepath = os.path.join(DATA_DIR, report_filename)

            # Записываем результат в файл
            try:
                with open(report_filepath, 'w', encoding='utf-8') as f:
                    f.write(f"Отчет сгенерирован: {datetime.now()}\n")
                    f.write(f"Функция: {func.__name__}\n")
                    f.write("=" * 50 + "\n")

                    if isinstance(result, pd.DataFrame):
                        if result.empty:
                            f.write("Нет данных для отчета\n")
                        else:
                            f.write(f"Количество записей: {len(result)}\n")
                            f.write("=" * 50 + "\n")
                            f.write(result.to_string())
                    else:
                        f.write(str(result))

                    f.write("\n" + "=" * 50)

                print(f"Отчет сохранен в файл: {report_filepath}")

            except Exception as e:
                print(f"Ошибка при записи отчета: {e}")

            return result

        return wrapper

    return decorator