import math
'''
# Pseudo Code
1 - Print the plan on screen investment - to calculate the amount of interest you'll earn on your investment
2 - bond - to calculate the amount you'll have to pay on a home loan
3 - Enter either 'investment' or 'bond' from the menu above to proceed
4 - Store the user selected_plan in selected_plan variable.
5 - Check if user select investment plan, then 
    1 - Take input amount of money user want to invest and store in money variable.
    2 - Take interest rate input from user and divide it by 100 and store in interest_rate variable.
    3 - Take number of year input from user want to invest and store in year variable.
    4 - Ask wether user want to invest in simple or compound interest.
    5 - If user select simple interest then
           1 - Use this formula money * (1 + interest_rate * year).
           2 - Calculate the amount by using formula and store in amount variable and print amount on screen.
    6 - If user select compound interest then,
           1 - Use this formula money * math.pow((1+interest_rate),year).
           2 - Calculate the amount by using formula and store in amount variable and print amount on screen.
    7 - else print "Invalid input, please select a valid interest"
6 - If user select bond plan, then
    1 - Take present value input from user and convert it into integer, store in present_value variable.
    2 - Take interest rate input from user and divide it by 100 and store in interest_rate variable.  
    3 - Take number of month want to take repay the bond input from user.
    4 - Divide interest rate by 12 and store in interest variable.
    5 - Use this formula (interest * present_value)/(1 - (1 + interest)**(-month)).
    6 - Calculate the repayment using formula and store in repayment variable and print on screen. 
7 - else print "Invalid plan selected, please select a valid plan to continue."
'''

selected_plan = input("""
investment - to calculate the amount of interest you'll earn on your investment
bond - to calculate the amount you'll have to pay on a home loan

Enter either 'investment' or 'bond' from the menu above to proceed : """)

if selected_plan == "investment" or selected_plan == "Investment" or selected_plan == "INVESTMENT":
    money = int(input("Amount of money you want to invest : ")) 
    interest_rate = (int(input("Please enter the interest rate : "))) / 100
    year = int(input("Please enter number of years you want to invest : "))
    interest = input("Do you want simple or compound interest : ")

    if interest == "simple":
        amount = money * (1 + interest_rate * year)
        print("Interest amount: " + str(amount))    
    
    elif interest == "compound":
        amount = money * math.pow((1+interest_rate),year)
        print("Interest amount: " + str(amount)) 
    
    else:
        print("Invalid input, please select a valid interest")

elif selected_plan == "bond" or selected_plan == "Bond" or selected_plan == "BOND":
    present_value = int(input("Please enter the present value of your house : ")) 
    interest_rate = (int(input("Please enter the interest rate : "))) / 100
    month = int(input("Please enter number of months you want to take to repay the bond : "))
    interest = interest_rate / 12
    repayment = (interest * present_value)/(1 - (1 + interest)**(-month))
    print("Repayment : " + str(repayment))

else:
    print("Invalid plan selected, please select a valid plan to continue.")

