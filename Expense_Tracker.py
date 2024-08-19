from ex import Expense
import calendar
import datetime


def main():
    print("i love my india")
    expense_file_path = "expense.csv"
    budget = 20000

    expense = expense_spend()

    file_save(expense, expense_file_path)

    summarize_expenses(expense_file_path, budget)
    pass


def expense_spend():
    print("How much money did you spend?")
    expense_name = input("where did you spend the money:")
    expense_amount = float(input("How much money did you spend"))
    print(f"expense name is {expense_name}, {expense_amount}")

    expense_categories = [
        "🍕Food",
        "🏘️Home",
        "🎯Work",
        "🎉Fun",
        "✨Misc",
    ]

    while True:
        print("In which category did you spend the money:")
        for i,  category_name in enumerate(expense_categories):
            print(f"{i+1}.{category_name}")

        value_range = f"[1-{len(expense_categories)}]"
        selected_index = int(input(f"what is the category:: {value_range}"))-1

        if selected_index in range(len(expense_categories)):
            selected_category = expense_categories[selected_index]
            print(selected_category)

            new_expense = Expense(
                name=expense_name, category=selected_category, amount=expense_amount)

            return new_expense
        else:
            print("invalid category")
        break


def file_save(expense: Expense, expense_file_path):
    print(f"expense should be saved in file: {expense} to {expense_file_path}")
    with open(expense_file_path, "a", encoding="utf-8") as f:
        f.write(f"{expense.name},{expense.amount},{expense.category}\n")


def summarize_expenses(expense_file_path, budget):
    print("summary of user expenses:")
    expenses = []
    with open(expense_file_path, 'r', encoding="utf-8") as f:
        lines = f.readlines()
        for line in lines:
            # print(line)
            expense_name, expense_amount, expense_category = line.strip().split(",")
            print(f"{expense_name}{expense_amount}{expense_category}")
            line_expense = Expense(name=expense_name, amount=float(
                expense_amount), category=expense_category)
            # print(line_expense)
            expenses.append(line_expense)
            # print(expenses)

    amount_by_category = {}
    for expense in expenses:
        key = expense.category

        if key in amount_by_category:
            amount_by_category[key] += expense.amount
        else:
            amount_by_category[key] = expense.amount

    # print(amount_by_category)
    print("This is your category wise spending:")
    for key, amount in amount_by_category.items():
        print(f"{key}:{amount}")

    total_spent = sum([x.amount for x in expenses])
    print(f"This is the amount you spent: {total_spent:.2f}")

    remaining_budget = budget - (total_spent)
    print(f"remaining budget: {remaining_budget:2f}")

    now = datetime.datetime.now()
    days_in_month = calendar.monthrange(now.year, now.month)[1]
    remaining_days = days_in_month - now.day
    print("remaining days in the month:", remaining_days)

    daily_budget = remaining_budget/remaining_days
    print("daily budget:", daily_budget)


if __name__ == '__main__':
    main()
