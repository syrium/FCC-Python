from itertools import zip_longest

class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def deposit(self, amount, description = ''):
        entry = {'amount': amount, 'description': description}
        self.ledger.append(entry)
        if entry in self.ledger:
            return True
        else:
            return False

    def withdraw(self, amount, description = ''):
        entry = {'amount': -amount, 'description': description}
        if self.check_funds(amount):
            self.ledger.append(entry)
        if entry in self.ledger:
            return True
        else:
            return False

    def get_balance(self):
        self.balance = 0.0
        for entry in self.ledger:
            self.balance += entry['amount']
        return self.balance

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        else:
            return False
    
    def check_funds(self, amount):
        #balance = self.get_balance()
        if amount > self.get_balance():
            return False
        else:
            return True

    def __str__(self):
        lines = []

        # Title
        title_line = display_title_line(self.name)
        lines.append(title_line)

        # Ledger
        for entry in self.ledger:
            amount = f"{entry['amount']:.2f}"
            description = entry['description'][:23]
            lines.append(f"{description.ljust(23)}{amount.rjust(7)}")

        # Total
        lines.append(f"Total: {self.get_balance():.2f}")

        return "\n".join(lines)

def display_title_line(title):
    total_width = 30
    pad = (total_width - len(title))//2
    left_pad = '*' * pad
    right_pad = '*' * (total_width - len(title) - pad) 
    return f'{left_pad}{title}{right_pad}'

def create_spend_chart(categories):
    
    category_dict = {}
    percent_by_category = {}
    line = 'Percentage spent by category\n'
    for category in categories:
        withdraw = round(sum((entry['amount'] * (-1) for entry in category.ledger if entry['amount'] < 0)),2)
        category_dict[(category.name)] = withdraw
    total_withdraw = round(sum(category_dict.values()),2)

    for category in category_dict:
        #percent_by_category = category
        percent_by_category[category] = round(((category_dict[category]/total_withdraw) * 100 ))
    
    #print graph
    for i in range(100, -1, -10):
        line += f'{i:>3}| '
        for per in percent_by_category:
            if percent_by_category[per] >= i:
                line += 'o  '
            else:
                line += '   '
        line += '\n'

    #print x axis line
    line += '    ' + '---' * len(percent_by_category) + '-\n'

    #print category names
    names = list(percent_by_category.keys())
    name_len = max(len(name) for name in names)
    name_padded = [name.ljust(name_len) for name in names] 
    xline = ''
    for row in range(name_len):
        line += '     '
        for name in name_padded:
            line += name[row] + '  '
        if row == name_len-1:
            line
        else:
            line += '\n'
            
    return line
"""
def create_spend_chart(categories):
    display = []
    total_withdraw, withdraw_count = 0.0, 0.0
    title = 'Percentage spent by category'
    display.append(title)

    for entry in categories.ledger:
        if entry['amount'] < 0:
            withdraw = -(entry['amount'])
            total_withdraw += withdraw
            withdraw_count += 1.0
    percentage =  round((total_withdraw/withdraw_count),-1)
    return(display, percentage)
"""
#food = Category('Food')
#cloth = Category('Clothes')
#food.deposit(1000, 'initial deposit')
#food.withdraw(10.15, 'groceries')
#print(food.get_balance())
#print(food.check_funds(9))
#food.transfer(10, cloth)
#print(food)

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
#print(food)
#print(clothing)
#print(auto)

print(create_spend_chart([food, clothing, auto]))