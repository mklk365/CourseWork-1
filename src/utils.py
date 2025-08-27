import pandas as pd
import os
import logging


PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
xlsx_file_path = os.path.join(PROJECT_ROOT, "data", "operations.xlsx")

# Путь к папке logs
LOG_DIR = os.path.join(PROJECT_ROOT, "logs")  # Путь к корневой папке logs
LOG_FILE = os.path.join(LOG_DIR, "utils_logger.log")  # Полный путь к файлу лога
os.makedirs(LOG_DIR, exist_ok=True)  # Создаем папку logs, если её нет

# Настройка логгера (перед использованием в функциях)
utils_logger = logging.getLogger(__name__)  # Создание и получение именованного логера
utils_logger.setLevel(logging.DEBUG)  # Настройка уровня логгирования
utils_logger.handlers = []  # Очистка старых обработчиков
# Создаем хендлер для вывода в файл
file_handler = logging.FileHandler(LOG_FILE, mode="w", encoding="utf-8")  # Новый лог при каждом запуске
file_formatter = logging.Formatter("%(asctime)s %(filename)s %(levelname)s: %(message)s")
file_handler.setFormatter(file_formatter)
utils_logger.addHandler(file_handler)

# Принудительно пишем тестовое сообщение
utils_logger.info("Логгер инициализирован!")


def read_excel_data(file_path: str = None) -> pd.DataFrame:
    """Функция принимает XLSX-файл и возвращает датафрейм
    с данными о финансовых транзакциях"""
    # Используем переданный путь или путь по умолчанию
    target_path = file_path if file_path is not None else xlsx_file_path
    try:
        # Читаем файл напрямую через pandas
        df = pd.read_excel(target_path)
        # Проверка на пустой DataFrame
        if df.empty:
            utils_logger.warning("Пустые данные!")
            return pd.DataFrame()  # Возвращаем пустой DataFrame
        return df  # Возвращаем DataFrame напрямую
    except FileNotFoundError:
        utils_logger.error(f"Файл '{target_path}' не найден!")
        return pd.DataFrame()  # Возвращаем пустой DataFrame
    except Exception as e:
        utils_logger.error(f"Ошибка при чтении XLSX файла: {e}")
        return pd.DataFrame()  # Возвращаем пустой DataFrame
