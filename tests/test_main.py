from unittest.mock import patch, MagicMock
import pandas as pd
from main import analyze_category


def test_analyze_category_with_date():
    """Тестирует analyze_category с указанной датой.
    Проверяет:
    - Корректный вызов read_excel_data
    - Корректная передача параметров в spending_by_category
    - Возврат правильного результата"""
    # Подготавливаем тестовые данные
    test_data = pd.DataFrame({
        'Категория': ['Бонусы', 'Продукты', 'Бонусы', 'Транспорт'],
        'Сумма': [1000, 500, 200, 300],
        'Дата': ['2020-12-05', '2020-12-04', '2020-12-05', '2020-12-03']
    })
    # Мокируем зависимости
    with patch('main.read_excel_data') as mock_read, \
            patch('main.spending_by_category') as mock_spending:
        mock_read.return_value = test_data
        mock_spending.return_value = 1200
        # Вызываем тестируемую функцию
        result = analyze_category("Бонусы", "2020-12-05")
        # Проверяем вызовы
        mock_read.assert_called_once()
        mock_spending.assert_called_once_with(test_data, "Бонусы", "2020-12-05")
        assert result == 1200, "Должна вернуться сумма 1200"


def test_analyze_category_without_date():
    """Тестирует analyze_category без указания даты.
    Проверяет:
    - Передача None в качестве даты
    - Корректная работа функции при отсутствии даты"""
    test_data = pd.DataFrame({
        'Категория': ['Бонусы', 'Продукты'],
        'Сумма': [1000, 500],
        'Дата': ['2020-12-05', '2020-12-04']
    })
    with patch('main.read_excel_data') as mock_read, \
            patch('main.spending_by_category') as mock_spending:
        mock_read.return_value = test_data
        mock_spending.return_value = 1500

        result = analyze_category("Бонусы")

        mock_read.assert_called_once()
        mock_spending.assert_called_once_with(test_data, "Бонусы", None)
        assert result == 1500, "Должна вернуться сумма 1500"


def test_analyze_category_nonexistent_category():
    """Тестирует analyze_category с несуществующей категорией.
    Проверяет:
    - Обработка категорий, которых нет в данных
    - Возврат 0 для несуществующих категорий"""
    test_data = pd.DataFrame({
        'Категория': ['Бонусы', 'Продукты'],
        'Сумма': [1000, 500],
        'Дата': ['2020-12-05', '2020-12-04']
    })
    with patch('main.read_excel_data') as mock_read, \
            patch('main.spending_by_category') as mock_spending:
        mock_read.return_value = test_data
        mock_spending.return_value = 0

        result = analyze_category("Несуществующая", "2020-12-05")

        assert result == 0, "Для несуществующей категории должен вернуться 0"


def test_analyze_category_empty_data():
    """Тестирует analyze_category с пустыми данными.
    Проверяет:
    - Обработка пустого DataFrame
    - Корректное поведение при отсутствии данных
    """
    with patch('main.read_excel_data') as mock_read, \
            patch('main.spending_by_category') as mock_spending:
        mock_read.return_value = pd.DataFrame()
        mock_spending.return_value = 0

        result = analyze_category("Бонусы", "2020-12-05")

        assert result == 0, "Для пустых данных должен вернуться 0"