# Programming Exercise 10-7

from  retailitem import *
from cashregister import *

# Constants to hold the options of purchase items
PANTS = 1
SHIRT = 2
DRESS = 3
SOCKS = 4
SWEATER = 5

# define get user choice
def get_user_choice():
    print('Menu')
    print('---------------------------------')
    print('1. Pants')
    print('2. Shirt')
    print('3. Dress')
    print('4. Socks')
    print('5. Sweater')
    print()

    choice = int(input('Enter the menu number of the item ' + \
                       'you would like to purchase: '))
    print()

    while choice > SWEATER or choice < PANTS:

        choice = int(input('Please enter a valid item number: '))
        print()

    return(choice)


# main method
def main():

    # Create sale items.
    pants = RetailItem('Pants', 10, 19.99)
    shirt = RetailItem('Shirt', 15, 12.50)
    dress = RetailItem('Dress', 3, 79.00)
    socks = RetailItem('Socks', 50, 1.00)
    sweater = RetailItem('Sweater', 5, 49.99)

    # Create dictionary of sale items.
    sale_items = {PANTS:pants, SHIRT:shirt,
                  DRESS:dress, SOCKS:socks,
                  SWEATER:sweater}

    # Create a cash register.
    register = CashRegister()

    # Initialize loop test.
    checkout = 'N'

    menuCount = 1
    # User wants to purchase more items:
    while checkout == 'N':
        if menuCount != 1:
           print()
        user_choice = get_user_choice()
        item = sale_items[user_choice]
        '''
        #If the item's iventory is 0 type 'The item is out of stock.'
        Otherwise,  1) add the item to the register  
                    2) change the inventory number of the item in the sale_items dictionary
                    3) ask the user if they're ready to checkout Y/N and save that in the checkout var
        '''
        #Your code here
        if item.get_inv() == 0:
           print("The item is out of stock.")
        else:
           register.purchase_item(item)
           print("The item was added to the cash register.")
           item.set_inv(item.get_inv() - 1)
        checkout = input("Are you ready to check out (Y/N)? ")
        menuCount += 1

    print()
    print('Your purchase total is: ', \
          format(register.get_total(), '.2f'))
    print()
    print("The items in the cash register are:")
    print()
    register.show_items()
    register.clear()


# Call the main function.
main()

