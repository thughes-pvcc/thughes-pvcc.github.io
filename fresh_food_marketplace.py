#Name: Trevor Hughes
#   Prog Purpose: This Fresh Food Marketplace Store Employee program writes code to find the gross pay, deductions, and net pay for an employee based on number of hours worked and job category.
#   Category Codes and hourly pay rates:
#       C   (Cashier)     $16.50
#       S   (Stocker)     $15.75
#       J   (Janitor)     $15.75
#       M   (Maintenance) $19.50
#   Deduction rates:
#       Federal income tax rate:    12%
#       State income tax rate:      3%
#       Social Security tax rate:   6.2%
#       Medicare taz rate:          1.45%

import datetime

#pay rates
PAY_RATE = (16.50, 15.75, 15.75, 19.50)

#deduction rates
DEDUCTION_RATE = (0.12, 0.03, 0.062, 0.0145)

#define global functions
gross_pay = 0
hours_worked = 0
job_category = 0
pay_rate = 0
federal_decuction = 0
state_deduction = 0
social_security_deduction = 0
medicare_deduction = 0
total_deduction = 0
net_pay = 0

def main():
    another_employee = True
    while another_employee:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("n\Would you like to input data for another employee? (Y/N) ")
        if yesno.upper() != "Y":
            another_employee = False
            print("\nOkay, See you soon!")

def get_user_data():
    global job_category, hours_worked
    job_category = str(input("Input Job Category Code: Cashier(C), Stocker(S), Janitor(J), Maintenance(M): "))
    hours_worked = int(input("Number of hours worked: "))

def perform_calculations():
    global gross_pay, federal_deduction, state_deduction, social_security_deduction, medicare_deduction, total_decuction, net_pay
    if job_category.upper() == "C":
        pay_rate = PAY_RATE[0]
    elif job_category.upper() == "S":
        pay_rate = PAY_RATE[1]
    elif job_category.upper() == "J":
        pay_rate = PAY_RATE[2]
    elif job_category.upper() == "M":
        pay_rate = PAY_RATE[3]
    else:
        pay_rate = 0
        print("\nEnter correct Input Job Category Code.")
    gross_pay = hours_worked * pay_rate
    federal_deduction = gross_pay * DEDUCTION_RATE[0]
    state_deduction = gross_pay * DEDUCTION_RATE[1]
    social_security_deduction = gross_pay * DEDUCTION_RATE[2]
    medicare_deduction = gross_pay * DEDUCTION_RATE[3]
    total_deduction = federal_deduction + state_deduction + social_security_deduction + medicare_deduction
    net_pay = gross_pay - total_deduction

def display_results():
    print('--------------------------------')
    print('     Fresh Food Marketplace     ')
    print('           Weekly Pay           ')
    print('                                ')
    print('Number of Hours worked : ' + format (hours_worked, '10'))
    print('Gross Pay              $ ' + format (gross_pay, '10,.2f'))
    print('Federal Income Tax     $ ' + format (federal_deduction, '10,.2f'))
    print('State Income Tax       $ ' + format (state_deduction, '10,.2f'))
    print('Social Security Tax    $ ' + format (social_security_deduction, '10,.2f'))
    print('Medicare Tax           $ ' + format (medicare_deduction, '10,.2f'))
    print('Total Amount Deducted  $ ' + format (total_deduction, '10,.2f'))
    print('Net Pay                $ ' + format (net_pay, '10,.2f'))
    print('                               ')
    print('                               ')
    print(str(datetime.datetime.now()))
    print('---------------------------------')

########## call on main program to execute ############
main()
