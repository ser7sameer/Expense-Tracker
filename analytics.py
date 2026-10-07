from storage import load_data
from expense_manager import add_expense as _add_expense, view_expenses as _view_expenses


def add_expense(amount, category, desc):
    return _add_expense(amount, category, desc)


def view_expenses():
    return _view_expenses()


def show_total_spending():
    data = load_data()
    total = sum(float(details['amount']) for details in data.values())
    print(f"📊 Total Spending: ${total:.2f}")