from analytics import add_expense, show_total_spending, view_expenses

def main():
    while True:
        print("\n--- 💰 SpendSmart ---")
        print("1. Add Expense\n2. View Expenses\n3. Total Spending\n4. Exit")
        choice = input("Select an option: ")
        
        try:
            if choice == '1':
                amt = float(input("Amount: "))
                cat = input("Category (Food/Travel/etc): ")
                desc = input("Description: ")
                add_expense(amt, cat, desc)
            elif choice == '2':
                view_expenses()
            elif choice == '3':
                show_total_spending()
            elif choice == '4':
                break
            else:
                print("❌ Invalid input.")
        except ValueError:
            print("❌ Error: Please enter a valid number for amount.")

if __name__ == "__main__":
    main()