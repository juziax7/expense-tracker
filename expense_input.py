"""Expense input module (Member A).

Lets the user enter multiple expenses (date, amount, category, optional note)
and appends them to expenses.csv, which the visualization module reads.
"""

import csv
import os
from datetime import date, datetime

DATA_FILE = "expenses.csv"
FIELDS = ["date", "amount", "category", "note"]


def ask_date():
    """Ask for a date in YYYY-MM-DD; empty input means today."""
    while True:
        text = input(f"Date (YYYY-MM-DD, Enter = {date.today()}): ").strip()
        if not text:
            return date.today().isoformat()
        try:
            return datetime.strptime(text, "%Y-%m-%d").date().isoformat()
        except ValueError:
            print("  Invalid date format, please try again.")


def ask_amount():
    """Ask for a positive number."""
    while True:
        text = input("Amount: ").strip()
        try:
            value = float(text)
            if value <= 0:
                raise ValueError
            return round(value, 2)
        except ValueError:
            print("  Amount must be a positive number.")


def ask_category():
    """Ask for a non-empty category."""
    while True:
        text = input("Category (e.g. Food, Transport, Entertainment): ").strip()
        if text:
            return text.capitalize()
        print("  Category cannot be empty.")


def save_expense(expense, path=DATA_FILE):
    """Append one expense to the CSV file, writing the header if needed."""
    is_new = not os.path.exists(path)
    with open(path, "a", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDS)
        if is_new:
            writer.writeheader()
        writer.writerow(expense)


def main():
    print("=== Expense Tracker: Input ===")
    count = 0
    while True:
        expense = {
            "date": ask_date(),
            "amount": ask_amount(),
            "category": ask_category(),
            "note": input("Note (optional): ").strip(),
        }
        save_expense(expense)
        count += 1
        print(f"  Saved: {expense['date']} {expense['category']} {expense['amount']}")

        again = input("Add another? (y/n): ").strip().lower()
        if again != "y":
            break
    print(f"Done. {count} expense(s) saved to {DATA_FILE}.")


if __name__ == "__main__":
    main()
