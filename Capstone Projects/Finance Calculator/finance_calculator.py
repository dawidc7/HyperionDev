# Finance Calculator code

import math #importing math module as it will be used lower down

print("investment - to calculate the amount of interest you'll earn on your investment \n\
bond       - to calculate the amount you'll have to pay on a home loan \n")

#user choice is changed to lower case so the code is not case sensitive
user_choice = input("Enter either 'investment' or 'bond' from the menu above to proceed. ").lower()

#code to calculate the investment part of the code
if user_choice == "investment":
    #variables to store user inputted data to be used in the interest calculator
    user_deposit = int(input("How much money do you want to deposit?: "))
    interest_rate = int(input("What is your interest rate?: ")) / 100   #interest rate is divided by 100 now for cleaner code in the calculation later
    num_years = int(input("What is the amount of years?: "))
    interest = input("What type of interest would you like?: ").lower()

    if interest == "simple":
        #formula for calculating simple interest using a provided formula and using the above variables
        #print statement displays the final value
        final_amount = user_deposit * (1 + (interest_rate * num_years))
        print(f"Your final amount is £{final_amount}")
    else:
        #formula for calculating compound interest using a provided formula and using the above variables
        #print statement displays the final value
        final_amount = user_deposit * math.pow((1 + interest_rate), num_years)
        print(f"Your final amount is £{round(final_amount,2)}")

#code to calculate the bond repayment
else:
    #code to take user input and store in different variables
    house_value = int(input("What is the value of the house?: "))
    interest_rate = (int(input("What is the interest rate?: ")) / 100) / 12     #interest rate is divided by 100 and then by 12 now for cleaner code in the calculation later
    months_num = int(input("What is the number of months?: "))

    #bond repayment calculation that uses the above variables and a provided formula
    #print statement below also displays the final amount
    repayment = (house_value * interest_rate) / (1 - (1 + interest_rate) ** -months_num)

    print(f"The amount you will have to repay each month is £{round(repayment, 2)}")

