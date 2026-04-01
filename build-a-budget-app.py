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
        display = []
        amount = []
        description = []
        display = [display_title_line(self.name)]

        expected_title = '*************Food*************'
        actual_title = display_title_line(self.name)
        assert expected_title == actual_title, (
            f'Title Mismatch\n'
            f'Expected: {repr(expected_title)}\n'
            f'Actual  : {repr(actual_title)}'
        )

        for entry in self.ledger:
            amount = '{:.2f}'.format(entry['amount'])
            description = entry['description'][:23]
            line = (f'{description.ljust(23)} {amount.rjust(7)}')
            print("Debud Ledger: ",repr(line))
            display.append(line)
        total_line = (f'Total: {self.get_balance():.2f}')       
        print("Debug total: ",repr(total_line) )
        display.append(total_line)
        final = '\n'.join(display) + '\n'
        print("Debug final: \n", final)

        expected = """*************Food*************
initial deposit        1000.00
groceries               -10.15
restaurant and more foo -15.89
Transfer to Clothing    -50.00
Total: 923.96"""
        actual = final

        for i,(e,a) in enumerate(zip(expected.splitlines(),actual.splitlines())):
            if e != a:
                print(f'Mismatch in line: {i}\n')
                print('Expected: ', repr(e))
                print('Actual  : ',repr(a))

        return '\n'.join(display) + '\n'

def display_title_line(title):
    pad = round(((30 - len(title))/2))
    pad_str = str('*'*pad)
    return f'{pad_str}{title}{pad_str}'

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
                line += 'o '
            else:
                line += '  '
        line += '\n'

    #print x axis line
    line += '    ' + '---' * len(percent_by_category) + '\n'

    #print category names
    names = list(percent_by_category.keys())
    for name_row in zip_longest(*names,fillvalue=" "):
        line +='     ' + ' '.join(name_row) + '\n'

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
"""
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
"""
#print(repr(display_title_line('Food')))
#print(len(display_title_line('Food')))
print(food)

