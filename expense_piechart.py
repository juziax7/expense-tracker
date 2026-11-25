"""Expense visualization module (Member B).

Reads expenses.csv (written by expense_input.py), sums the amounts by
category, and draws a pie chart. The chart is shown on screen and also
saved as pie_chart.png.
"""

import csv
import os
import sys
from collections import defaultdict

import matplotlib.pyplot as plt

DATA_FILE = "expenses.csv"
OUTPUT_FILE = "pie_chart.png"


def load_totals(path=DATA_FILE):
    """Return a dict of {category: total amount}."""
    totals = defaultdict(float)
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f):
            try:
                amount = float(row["amount"])
            except (KeyError, ValueError):
                continue  # skip broken rows
            category = (row.get("category") or "Other").strip() or "Other"
            totals[category] += amount
    return dict(totals)


def draw_pie(totals, output=OUTPUT_FILE):
    """Draw and save a pie chart of spending by category."""
    # Largest category first so the chart reads clockwise from biggest
    items = sorted(totals.items(), key=lambda kv: kv[1], reverse=True)
    labels = [k for k, _ in items]
    values = [v for _, v in items]
    grand_total = sum(values)

    def label_pct(pct):
        amount = pct * grand_total / 100
        return f"{pct:.1f}%\n(${amount:,.0f})"

    fig, ax = plt.subplots(figsize=(7, 7))
    ax.pie(
        values,
        labels=labels,
        autopct=label_pct,
        startangle=90,
        counterclock=False,
        wedgeprops={"edgecolor": "white", "linewidth": 2},
    )
    ax.set_title(f"Expenses by Category (Total: ${grand_total:,.0f})", fontsize=14)
    ax.axis("equal")
    fig.tight_layout()
    fig.savefig(output, dpi=150)
    print(f"Pie chart saved to {output}")
    plt.show()


def main():
    if not os.path.exists(DATA_FILE):
        print(f"{DATA_FILE} not found. Run expense_input.py first.")
        sys.exit(1)

    totals = load_totals()
    if not totals:
        print(f"No expenses in {DATA_FILE}. Add some with expense_input.py.")
        sys.exit(1)

    print("Totals by category:")
    for category, amount in sorted(totals.items(), key=lambda kv: -kv[1]):
        print(f"  {category:<15} {amount:>10,.2f}")
    draw_pie(totals)


if __name__ == "__main__":
    main()
