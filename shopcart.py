# 1) Build a Shopping Cart

# You can use either lists or dictionaries. The program should have the following capabilities:

# 1) Takes in input
# 2) Stores user input into a dictionary or list
# 3) The User can add or delete items
# 4) The User can see current shopping list
# 5) The program Loops until user 'quits'
# 6) Upon quiting the program, print out all items in the user's list 

def add_item(cart, item, quantity, cost):
    if item in cart:
        cart[item]['quantity']+=quantity
    else:
        cart[item] = {
            'quantity': quantity,
            'price': cost
        }
    show_shopping_list(cart)

def del_item(cart, item, quantity):
    cart[item]['quantity']-=quantity
    if cart[item]['quantity'] < 1:
        del cart[item]
    show_shopping_list(cart)

def show_shopping_list(cart):
    print('\n','='*10)
    print(cart)

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
            item = input('What item will you add?: ')
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