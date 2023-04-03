#Name: Trevor Hughes
#Prog Purpose: This program finds the cost of Palermo Pizzas
#   Price for one pizza: Small- $9.99, Medium- $12.99, Large- $14.99, Extra Large- $17.99
#   Sales tax rate: 5.5%

import datetime

############## define global variables ############
# define tax rate and prices
SALES_TAX_RATE = .055
PR_Small= 9.99
PR_Medium= 12.99
PR_Large= 14.99
PR_ExtraLarge= 17.99

# define global variables
pizza_size = 0
num_pizzas = 0
pizza_cosy = 0
sales_tax = 0
total = 0

############## define program functions ###############
def main():
    another_order = True
    while another_order:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nWould you like to place another order? (Y/N): ")
        if yesno.upper() != "Y":
            another_order = False

def get_user_data():
    global pizza_size, num_pizzas
    pizza_size = str(input("Pizza size (S,M,L,X): "))
    num_pizzas = int(input("Number of Pizzas: "))

def perform_calculations():
    global pizza_cost, sales_tax, total
    if pizza_size.upper() == 'S':
        pizza_cost = num_pizzas * PR_Small
    elif pizza_size.lower() == 's':
        pizza_cost = num_pizzas * PR_Small
    elif pizza_size.upper() == 'M':
        pizza_cost = num_pizzas * PR_Medium
    elif pizza_size.lower() == 'm':
        pizza_cost = num_pizzas * PR_Medium
    elif pizza_size.upper() == 'L':
        pizza_cost = num_pizzas * PR_Large
    elif pizza_size.lower() == 'l':
        pizza_cost = num_pizzas * PR_Large
    elif pizza_size.upper() == 'X':
        pizza_cost = num_pizzas * PR_ExtraLarge
    elif pizza_size.lower() == 'x':
        pizza_cost = num_pizzas * PR_ExtraLarge
    else:
        pizza_cost = 0
    sales_tax = pizza_cost * SALES_TAX_RATE
    total = pizza_cost + sales_tax

def display_results():
    print('------------------------------')
    print('**** Palermo Pizza ****')
    print('------------------------------')
    print('Number of Pizzas Ordered :' + format(num_pizzas, '10'))
    print('Pizza Cost               $' + format(pizza_cost,'10,.2f'))
    print('Sales Tax                $' + format(sales_tax,'10,.2f'))
    print('Total                    $' + format(total,'10.2f'))
    print('------------------------------')
    print(str(datetime.datetime.now()))

########## call on main program to execute ############
main()
