from utils import read_excel_data
from reports import spending_by_category
from decorators import create_report

# Декорируем функцию
@create_report("category_report")
def analyze_category(category: str, date: str = None):
    data = read_excel_data()
    return spending_by_category(data, category, date)

# Использование
if __name__ == "__main__":
    result = analyze_category("Еда", "2024-01-15")