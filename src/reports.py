from datetime import datetime
import pandas as pd
from typing import Optional


def date_three_months() -> datetime:
    """Вычисляем дату три месяца назад"""
    current_date = datetime.now()
    year = current_date.year
    month = current_date.month - 3
    if month <= 0:
        year -= 1
        month += 12
    return datetime(year, month, 1)  # Искомая дата (используем первое число месяца)


def spending_by_category(transactions: pd.DataFrame, category: str, date: Optional[str] = None) -> pd.DataFrame:
    """Функция "Траты по категории"
    принимает на вход: датафрейм с транзакциями, название категории,
    опциональную дату (если дата не передана, то берется текущая дата),
    а возвращает траты по заданной категории за последние три месяца (от переданной даты)"""
    if transactions.empty:
        return pd.DataFrame()
    if category is None:
        print("Не указана категория")
        return pd.DataFrame()

    # Преобразуем даты в данных
    transactions = transactions.copy()  # Создаем копию чтобы не менять оригинал
    transactions['Дата операции'] = pd.to_datetime(
        transactions['Дата операции'],
        format="%d.%m.%Y %H:%M:%S",
        dayfirst=True,
        errors='coerce'
    )

    # Удаляем строки с некорректными датами
    transactions = transactions.dropna(subset=['Дата операции'])

    if date is None:
        end_date = datetime.now()
    else:
        end_date = datetime.strptime(date, "%Y-%m-%d")

    start_date = date_three_months()

    # Теперь фильтруем по уже преобразованным датам
    filtered_transactions = transactions[
        (transactions["Категория"] == category)
        & (transactions["Дата операции"] >= start_date)
        & (transactions["Дата операции"] <= end_date)
        ]

    return filtered_transactions


def spending_by_weekday(transactions: pd.DataFrame, date: Optional[str] = None) -> pd.DataFrame:
    """Функция "Траты по дням недели"
    принимает на вход: датафрейм с транзакциями, опциональную дату.
    Если дата не передана, то берется текущая дата.
    Возвращает средние траты в каждый из дней недели за последние три месяца (от переданной даты)"""
    pass


def spending_by_workday(transactions: pd.DataFrame, date: Optional[str] = None) -> pd.DataFrame:
    """Функция "Траты в рабочий/выходной день"
    принимает на вход: датафрейм с транзакциями, опциональную дату.
    Если дата не передана, то берется текущая дата.
    Ыыводит средние траты в рабочий и в выходной день за последние три месяца (от переданной даты)."""
    pass
