"""A budget app that allows users to create different budget categories,
track their expenses, and visualize spending habits."""


class Category:
    """Class representing a budget category."""

    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description=""):
        """Method to deposit money into the category."""
        self.ledger.append({
            'amount': amount,
            'description': description
        })

    def withdraw(self, amount, description=""):
        """Method to withdraw money from the category."""
        if self.check_funds(amount):
            self.ledger.append({
                'amount': -amount,
                'description': description
            })
            return True
        else:
            return False

    def get_balance(self):
        """Method to get the current balance of the category."""
        balance = 0
        for item in self.ledger:
            balance += item['amount']
        return balance

    def transfer(self, amount, destination):
        """Method to transfer money to another category."""
        if self.check_funds(amount):
            self.withdraw(amount, f"Transfer to {destination.name}")
            destination.deposit(amount, f"Transfer from {self.name}")
            return True
        else:
            return False

    def check_funds(self, amount):
        """Method to check if there are enough funds for a withdrawal."""
        if amount > self.get_balance():
            return False
        else:
            return True

    def __str__(self):
        string = ""
        max_length = 30
        name_length = len(self.name)
        star_left = (max_length - name_length) // 2
        star_right = max_length - name_length - star_left
        string += '*' * star_left + self.name + '*' * star_right + '\n'

        for entry in self.ledger:
            fixed_desc = entry['description'][:23]
            fixed_amount = "%.2f" % entry['amount']
            remained_space = 30 - len(fixed_desc) - len(fixed_amount)
            string += fixed_desc + ' ' * remained_space + fixed_amount + '\n'

        string += f"Total: {self.get_balance()}"

        return string


def create_spend_chart(categories):
    """Function to create a spending chart for the given categories."""
    title = "Percentage spent by category\n"
    # 1. Calculate total spent per category (withdrawals only)
    spends = []
    for category in categories:
        total_spent = 0
        for item in category.ledger:
            amount = item["amount"]
            if amount < 0:  # withdrawal
                total_spent += -amount
        spends.append(total_spent)

    total_all = sum(spends)

    # 2. Calculate percentages rounded down to nearest 10
    percentages = [(spend / total_all) * 100 for spend in spends]
    rounded = [int(p // 10 * 10) for p in percentages]

    # 3. Build Y-axis (100 to 0)
    chart = ""
    for i in range(100, -1, -10):
        chart += f"{i:3}| "
        for pct in rounded:
            chart += "o  " if pct >= i else "   "
        chart += "\n"

    # 4. Divider line
    chart += "    " + "-" * (len(categories) * 3 + 1) + "\n"

    # 5. Vertical category labels
    names = [cat.name for cat in categories]
    max_len = max(len(name) for name in names)

    for i in range(max_len):
        chart += "     "
        for name in names:
            chart += (name[i] if i < len(name) else " ") + "  "
        if i < max_len - 1:
            chart += "\n"

    return title + chart

# Example usage
food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
car = Category('Car')
car.deposit(500, 'deposit')
car.withdraw(20, 'gas')
food.transfer(50, clothing)
print(food)

categories = [food, clothing, car]
spend_chart = create_spend_chart(categories)
print(spend_chart)
