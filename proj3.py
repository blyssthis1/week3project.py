
#classIncome:
def add_income(self, name, amount):
    if name in self:
        self[name]['amount']+=amount
    else:
        self[name] = {
            'amount': amount
        
        }
    show_shopping_list(self)
#classExpenses:
def expenses(self, name, amountE):
    if name in self:
        self[name]['amountE']+=amountE
    else:
        self[name] = {
            'amountE': amountE
        }
    show_shopping_list(self)

def show_shopping_list(self):
    print('\n','='*10)
    print(self)

'''
cart= {
    item : {
        quantity: 2
        price: 4
    }
}
'''

def driver():
    shopping_cart={}
    shopping = True
    while shopping:
        user_choice = input('Choices: add/remove/show/quit: ' ).lower()
        if user_choice == 'add':
            item = input('Income(I) or Expense(E): ').upper()
            if
            while True:
                try:
                    quantity = int(input('How many of said item?: '))
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
            del_item(shopping_cart, item_to_del, quantity)
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