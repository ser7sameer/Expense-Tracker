from storage import save_data, load_data
import random

def add_expense(amount, category, desc):
    data = load_data()
    exp_id = str(random.randint(1000, 9999))
    data[exp_id] = {"amount": amount, "category": category, "desc": desc}
    save_data(data)
    print("✅ Expense added successfully!")

def view_expenses():
    data = load_data()
    for exp_id, details in data.items():
        print(f"ID: {exp_id} | ${details['amount']} | {details['category']} | {details['desc']}")

def show_total_spending():
    data = load_data()
    total = sum(expense["amount"] for expense in data.values())
    print(f"Total spending: ${total:.2f}")