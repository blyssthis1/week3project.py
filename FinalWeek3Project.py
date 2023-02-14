class rent:
    def __init__(self, income, expense):
        self.income = income
        self.expense = expense
        self.cashflow = 0



    def add_income(self):
        
        incomename = input("What is the income name?: ")
        incomeamount= int(input("What is the income amount?: "))
        self.income[incomename] = incomeamount
        incomecontd = input("Do you want to enter another income?(type: y or n): ")
        if incomecontd == "y":
            self.add_income()

        else:
            print(self.income)
            print(f' Total income is:', sum(self.income.values()))
        
    

    def add_expense(self):
        expensename = input("What is the expense name?: ")
        expenseamount= int(input("What is the expense amount?: "))
        self.expense[expensename] = expenseamount
        expensecontd = input("Do you want to enter another expense?(type: y or n): ")
        if expensecontd == "y":
            self.add_expense()

        else:
            print(self.expense)
            print(f'Total expense is:', sum(self.expense.values()))



    def totalcashflow(self):
        
        print(f'Total cashflow is:', sum(self.income.values()) - sum(self.expense.values()))

    
    
    def show_expense(self):
        print(self.expense)
    
    def show_income(self):
        print(self.income)




rentG = rent({"rent":10}, {"tax":9})

rentG.add_income()
rentG.add_expense()
rentG.totalcashflow()



















# def calculator():
    
#     try:
#         option = input("Would you like to add, divide, multiply, or subtract?: ")
#         if option != "add" and option != "divide" and option != "multiply" and option != "subtract":
#             raise Exception("Please type one of the above options.")
            
#         if option == "add":
#             add1 = int(input("What is the first number you want to add?: "))
#             add2 = int(input("What is the second number you want to add?: "))
#             print(int(add1) + int(add2))

#         elif option == "divide":
#             div1 = int(input("What is the first number you want to divide?: "))
#             if div1 == 0:
#                 raise Exception("You can't divide by zero!")
#             div2 = int(input("What is the second number you want to divide it by?: "))
#             if div2 == 0:
#                 raise Exception("You can't divide by zero!")
#             print(int(div1) / int(div2))

#         elif option == "multiply":
#             mult1 = int(input("What is the first number you want to multiply?: "))
#             mult2 = int(input("What is the second number you want to multiply?: "))
#             print(int(mult1) * int(mult2))

#         elif option == "subtract":
#             sub1 = int(input("What is the first number you want to subtract from?: "))
#             sub2 = int(input("What is the second number you want to subtract?: "))
#             print(int(sub1) - int(sub2))
            
#     except ValueError as err:
#         print("That wasn't an integer!")
            
#     except Exception as err:
#         print(err)
        
    