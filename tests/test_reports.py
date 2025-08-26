from datetime import datetime
from unittest.mock import patch
from reports import date_three_months


"""Тестируем вычисление даты три месяца назад"""


def test_regular_case():
    with patch("reports.datetime") as mock_datetime:
        mock_datetime.now.return_value = datetime(2024, 5, 15)
        result = date_three_months()
        expected = datetime(2024, 2, 1)
        assert result == expected


def test_year_transition():
    with patch("reports.datetime") as mock_datetime:
        mock_datetime.now.return_value = datetime(2024, 2, 15)
        result = date_three_months()
        expected = datetime(2023, 11, 1)
        assert result == expected


def test_always_first_day():
    with patch("reports.datetime") as mock_datetime:
        mock_datetime.now.return_value = datetime(2024, 3, 31)
        result = date_three_months()
        assert result.day == 1
