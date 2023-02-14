class run_me_my_money:

    def __init__(self, income, expenses):
        self.income = income
        self.expenses = expenses

    
class income():
    def __init__(self, income_name, income_amount, income_category):
        self.income_name = income_name
        self.income_amount = income_amount
        self.category = income_category
        income_name = input(f'Name your income: ')
        income_amount = int(input(f'Type in the income amount: '))
        income_category = input(f'Input income category: ')

        
# def income(self, income_name, income_amount, income_category):



    
class expenses():
    def __init__(self, expense_name, expense_amount):
        self.expense_name = expense_name
        self.expense_amount = expense_amount

    
class cashflow():
    def __init__(self, cashflow):
        self.cashflow = cashflow
        cashflow = expenses(self) - income(self)



