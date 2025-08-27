from utils import read_excel_data
from reports import spending_by_category
from decorators import create_report


# Декорируем функцию
@create_report("category_report")
def analyze_category(category: str, date: str = None):
    data = read_excel_data() # Вызов utils.py
    print(f"Прочитано записей: {len(data)}")
    print(f"Колонки: {data.columns.tolist()}")
    print(f"Первые 5 записей:\n{data.head()}")
    return spending_by_category(data, category, date)


# Использование
if __name__ == "__main__":
    result = analyze_category("Бонусы", "2020-12-05")
