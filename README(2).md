# SpendSmart – Expense Tracker

## Overview
SpendSmart is a menu-driven, command-line expense tracker written in Python. It lets a user record an expense, view saved expenses, and calculate total spending. Expense records are stored locally in a JSON file (`expenses.json`), so they remain available between program runs.

## Features
- **Add Expense:** Enter an amount, category, and description.
- **View Expenses:** Display saved records with an expense ID, amount, category, and description.
- **Total Spending:** Calculate and display the sum of recorded expense amounts.
- **Persistent Storage:** Save and load expense records using JSON.
- **Input Handling:** Reject invalid menu choices and catch non-numeric amounts.

## Project Structure
```text
SpendSmart/
├── main.py              # Command-line menu and application entry point
├── analytics.py         # Public operations and total-spending calculation
├── expense_manager.py   # Adds and lists expense records
├── models.py            # Expense data model
├── storage.py            # JSON load/save helpers
└── expenses.json         # Local expense data (created when saved)
```

## Requirements
- Python 3.8 or later (the code uses standard-library modules only)
- No third-party packages are required.

## How to Run
1. Place all Python files and `expenses.json` (if already present) in the same folder.
2. Open a terminal in that folder.
3. Run:
   ```bash
   python main.py
   ```
4. Select an option from the menu:
   - `1` to add an expense
   - `2` to view expenses
   - `3` to show total spending
   - `4` to exit

## Data Format
Expenses are stored as a JSON object keyed by a randomly generated four-digit ID. Each record contains:
- `amount`: numeric expense amount
- `category`: category entered by the user
- `desc`: description entered by the user

Example:
```json
{
  "7942": {
    "amount": 10000.0,
    "category": "Food",
    "desc": "chat"
  }
}
```

## Module Responsibilities
- **`main.py`:** Repeats the menu, reads user input, dispatches actions, and handles `ValueError` for invalid numeric amounts.
- **`analytics.py`:** Exposes the add/view operations and calculates total spending by loading the saved records.
- **`expense_manager.py`:** Creates an expense ID, adds the record to the data dictionary, saves it, and prints saved expenses.
- **`storage.py`:** Loads JSON data from disk, returning an empty dictionary if the file does not exist, and writes updated data to the file.
- **`models.py`:** Defines an `Expense` class with ID, amount, category, and description attributes. The current menu workflow stores dictionaries in JSON rather than instantiating this class.

## Limitations and Possible Improvements
- IDs are random four-digit numbers, so a collision could overwrite an existing record.
- There are no options to edit or delete an expense.
- Amount validation currently checks that input can be converted to a number; it does not prevent negative values.
- Category names are free-form text rather than a controlled list.
- The application uses a local JSON file and has no user accounts, encryption, or backup feature.
- An empty expense list produces no explanatory message when viewing records.

## Troubleshooting
- If `python` is not recognized, try `python3 main.py` or check that Python is installed and on your PATH.
- Run the program from the project directory so `expenses.json` is read and written in the expected location.
- If the JSON file is manually edited, ensure it remains valid JSON.

## License
No license is specified in the supplied project files.
