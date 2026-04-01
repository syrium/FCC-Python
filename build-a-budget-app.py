class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description = ''):
        if not self.check_funds(amount):
            return False
        self.ledger.append({'amount': -amount, 'description': description})
        return True   

    def get_balance(self):
        return sum(entry['amount'] for entry in self.ledger)

    def transfer(self, amount, category):
        if not self.check_funds(amount):
            return False
        self.withdraw(amount, f'Transfer to {category.name}')
        category.deposit(amount, f'Transfer from {self.name}')
        return True
    
    def check_funds(self, amount):
        return amount <= self.get_balance()
        

    def __str__(self):
        # Title
        lines = [display_title_line(self.name)]

        # Ledger
        for entry in self.ledger:
            amount = f"{entry['amount']:.2f}"
            desc = entry['description'][:23]
            lines.append(f"{desc.ljust(23)}{amount.rjust(7)}")

        # Total
        lines.append(f"Total: {self.get_balance():.2f}")
        return "\n".join(lines)

def display_title_line(title):
    width = 30
    pad = (width - len(title))//2
    return f"{'*' * pad}{title}{'*' * (width - len(title) - pad)}"

def create_spend_chart(categories):
    # Calculate spending per category
    spent = {
        cat.name: sum(-entry['amount'] for entry in cat.ledger if entry['amount'] < 0)
        for cat in categories
    }
    total = sum(spent.values())

    # Percentages rounded down to nearest 10
    perc = {name: int((amount / total) * 100) // 10 * 10 for name, amount in spent.items()}
    
    # Header
    lines = ['Percentage spent by category']

    # Chart rows
    for level in range(100, -1, -10):
        row = f'{level:>3}| '
        for name in spent:
            row += 'o  ' if perc[name] >= level else '   '
        lines.append(row)

    # print x axis line
    lines.append('    ' + '-' * (len(categories) * 3 + 1))

    # print category names
    names = list(spent.keys())
    max_len = max(len(name) for name in names)
    #name_padded = [name.ljust(max_len) for name in names] 
    for i in range(max_len):
        row = '     '
        for name in names:
            row += (name[i] + ' ' if i < len(name) else '  ') + ' '
        lines.append(row)
            
    return '\n'.join(lines)

food = Category('Food')
food.deposit(1000, 'initial deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')

clothing = Category('Clothing')
clothing.deposit(500, 'initial deposit')
clothing.withdraw(10.15, 'groceries')
clothing.withdraw(5.15, 'borrow')

auto = Category('Auto')
auto.deposit(400, 'initial deposit')
auto.withdraw(20.05, 'tires')
auto.withdraw(10.05, 'stickers')
food.transfer(50, clothing)
print(food)
print(clothing)
print(auto)

print(create_spend_chart([food, clothing, auto]))