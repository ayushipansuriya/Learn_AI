#Expence Tracker json file using cli

import argparse
import json





def load_expenses():
    try:
        with open("expenses.json", "r") as f:
            return json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        return []

def save_expenses(expenses):
    with open("expenses.json", "w") as f:
        json.dump(expenses, f, indent=4)

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--add', nargs=3, metavar=('CATEGORY', 'AMOUNT', 'DATE'), help="Add new expense...")
    parser.add_argument('--show', action='store_true', help="Show all expenses....")
    args = parser.parse_args()

    if args.add:
        expenses = load_expenses()
        new_exp = {
            "category": args.add[0],
            "amount": args.add[1],
            "date": args.add[2]
        }
        expenses.append(new_exp)
        save_expenses(expenses)
        print("Added:", new_exp)

    elif args.show:
        expenses = load_expenses()
        if not expenses:
            print("No expenses found.")
        else:
            print("\nYour Expenses:")
            for i, exp in enumerate(expenses, start=1):
                print(f"{i}. {exp['date']} | {exp['category']} | Rs.{exp['amount']}")


if __name__=="__main__":
    main()
