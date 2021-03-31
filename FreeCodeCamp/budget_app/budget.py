class Category:

    def __init__(self, name = ''):
        self.name = name
        self.ledger = []
        self.balance = 0

    def get_balance(self):
        self.balance = sum(dictionaries['amount'] for dictionaries in self.ledger)
        return self.balance

    def check_funds(self, amount):
        if float(amount) > self.get_balance():
            return False
        else:
            return True

    def deposit(self, amount, description = ''):
        self.ledger.append(dict(amount = float(amount), description = description))

    def withdraw(self, amount, description = ''):
        if self.check_funds(float(amount)):
            self.ledger.append(dict(amount = -float(amount), description = description))
            return True
        else:
            self.ledger = self.ledger
            return False

    def transfer(self, amount, budget_categ):
        if self.get_balance() < float(amount):
            return False
        else:
            self.withdraw(amount, 'Transfer to ' + budget_categ.name)
            budget_categ.deposit(amount, 'Transfer from ' + self.name)
            return True

    def __str__(self):
        nr_stars = (30 - len(self.name))/2
        title = '*'*int(nr_stars) + self.name + '*'*int(nr_stars)

        ledger_lines = ''
        for dictionary in self.ledger:
            if len(dictionary['description']) > 23:
                descr_bit = dictionary['description'][:23]
            else:
                descr_bit = dictionary['description'] + ' '*(23 - len(dictionary['description']))
            
            if len(str(dictionary['amount'])) > 7:
                amount_bit = '{:.2f}'.format(dictionary['amount'][:7]) + '\n'
            else:
                amount_bit = (7 - len('{:.2f}'.format(dictionary['amount'])))*' ' + '{:.2f}'.format(dictionary['amount']) + '\n'

            ledger_lines = ledger_lines + descr_bit + amount_bit

        total_line = 'Total:' + ' ' + '{:.2f}'.format(self.get_balance())
        return title + '\n' + ledger_lines + total_line


def create_spend_chart(categories):

    total_withdraw = sum(sum(dic['amount'] for dic in category.ledger if dic['amount']<0) for category in categories)

    percent = []
    for category in categories:
        percent.append((sum(dic['amount'] for dic in category.ledger if dic['amount'] < 0)/total_withdraw))
    
    percent_list = [int(((num*100)//10)*10) for num in percent]
    
    line1 = 'Percentage spent by category' #+ '\n'

    # line100 = '100|' 
    # line90 = ' 90|' 
    # line80 = ' 80|' 
    # line70 = ' 70|' 
    # line60 = ' 60|' 
    # line50 = ' 50|' 
    # line40 = ' 40|' 
    # line30 = ' 30|' 
    # line20 = ' 20|'
    # line10 = ' 10|' 
    # line0 = '  0|' 
    
    # for index, category in enumerate(categories):
    
    #     line100 = line100 + (' o ' if percent_list[index] >= 100 else 3*' ') 
    #     line90 = line90 + (' o ' if percent_list[index] >= 90 else 3*' ')
    #     line80 = line80 + (' o ' if percent_list[index] >= 80 else 3*' ')
    #     line70 = line70 + (' o ' if percent_list[index] >= 70 else 3*' ')
    #     line60 = line60 + (' o ' if percent_list[index] >= 60 else 3*' ')
    #     line50 = line50 + (' o ' if percent_list[index] >= 50 else 3*' ')
    #     line40 = line40 + (' o ' if percent_list[index] >= 40 else 3*' ')
    #     line30 = line30 + (' o ' if percent_list[index] >= 30 else 3*' ')
    #     line20 = line20 + (' o ' if percent_list[index] >= 20 else 3*' ')
    #     line10 = line10 + (' o ' if percent_list[index] >= 10 else 3*' ')
    #     line0 = line0 + (' o ' if percent_list[index] >= 0 else 3*' ')

    # lines100_0 = line100 + ' \n' + line90 + ' \n' + line80 + ' \n' + line70 + ' \n' + line60 + ' \n' + line50 + ' \n' + line40 + ' \n' + line30 + ' \n' + line20 + ' \n' + line10 + ' \n' + line0 + ' \n'
    
    line = ''
    for i in range(100, -1, -10):
        line = line + '\n' + (3-len(str(i)))*' ' + str(i) + '|'
        for index, category in enumerate(categories):
            line = line + (' o ' if percent_list[index] >= i else 3*' ')
        line = line + ' '

    line_horiz = '\n' + 4*' ' + (3*len(categories)+1)*'-' 

    longest_name = max(len(cat.name) for cat in categories)
    last_line = ''

    for i in range(0, longest_name):
        last_line =  last_line + '\n' + 5*' '
        for category in categories:
            if i >= len(category.name):
                letter = ' '
            else:
                letter = category.name[i]
            last_line = last_line + letter + 2*' '

    return line1 + line + line_horiz + last_line

# categ = Category('Food')
# categ2 = Category('Clothes')

# print(categ.deposit('1000', 'food'))
# print(categ.ledger)
# print(categ.get_balance())

# print(categ2.deposit('100', 'water'))
# print(categ2.ledger)
# print(categ2.get_balance())

# print(categ.transfer('1150', categ2))
# print(categ.ledger)
# print(categ2.ledger)
# print(categ.get_balance())
# print(categ2.get_balance())

# print(categ.transfer('200', categ2))
# print(categ.ledger)
# print(categ2.ledger)
# print(categ.get_balance())
# print(categ2.get_balance())
# categ2.withdraw('100')

# print(categ.withdraw('100', 'bla'))

# print(categ) 
# print(sum(di['amount'] for di in categ.ledger if di['amount']<0))

# food = Category("Food")
# food.deposit(1000, "initial deposit")
# food.withdraw(10.15, "groceries")
# food.withdraw(15.89, "restaurant and more food for dessert")
# print(food.get_balance())
# clothing = Category("Clothing")
# food.transfer(50, clothing)
# clothing.withdraw(25.55)
# clothing.withdraw(100)
# auto = Category("Auto")
# auto.deposit(1000, "initial deposit")
# auto.withdraw(15)

# print(food)
# print(clothing)

# print(create_spend_chart([food, clothing, auto]))


# print(categ.ledger)
# print(categ2.ledger)


# print(categ.withdrawl('100', 'beer'))
# print(categ.get_balance())
# print(categ.check_funds('950'))

# print(categ.withdrawl('950'))
# print(categ.deposit('100'))
# print(categ.withdrawl('600'))
# print(categ.ledger)
# print(categ.get_balance())


