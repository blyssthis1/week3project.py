
#classIncome:
class income:
    incomes = {}
    def income(self, name, amount):
        if name in self:
            self[name]['amount']+=amount
        else:
            self[name] = {
                'amount': amount

            }


        show_income_list(self)

    def del_item(cart, item, amount):
        self[name]['amount']-=amount
        if cart[name]['quantity'] < 1:
            del self[name]
        show_income_list(self)

    def show_income_list(self):
        print('\n','='*10)
        print(self)
    
#classExpenses:


def driver():
    incomes={}
    shopping = True
    while income and expense:
        user_choice = input('Choices: add/remove/show/quit: ' ).lower()
        if user_choice == 'add':
            income = input('Are you adding income(i) or expense(e): ').lower()
            

            while True:
                try:
                    amount = int(input('Enter amount: '))
                    break
                except:
                    print("Please enter quantity in digits")
            while True:
                price = input('What\'s the cost?: ')
                if price.isdigit():
                    price=int(price)
                    break
                print("Please enter price in digits")
            add_item(shopping_cart, item, quantity, price)
        elif user_choice == 'remove':
            item_to_del = input('What item will you remove?: ')
            while True:
                try:
                    quantity = int(input('How many of said item to remove?: '))
                    break
                except:
                    print("Please enter quantity in digits")
            del_item(income, item_to_del, quantity)
        elif user_choice == 'show':
            show_shopping_list(shopping_cart)
        elif user_choice == 'quit':
            shopping = False
        else:
            print('Please Enter Valid Choice')
    show_shopping_list(shopping_cart)
    return shopping_cart

my_cart = driver()

print('\n','='*20,'\n', my_cart)





# class expense:
#     expenses ={}
#     def expenses(self, name, amountE):
#         if name in self:
#             self[name]['amountE']+=amountE
#         else:
#             self[name] = {
#                 'amountE': amountE
#             }
#         show_expense_list(self)

#     def show_expense_list(self):
#         print('\n','='*10)
#         print(self)
