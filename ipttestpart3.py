# shows different values
PENNY_VALUE = 1
NICKEL_VALUE = 5
DIME_VALUE = 10
QUARTER_VALUE = 25
PENNIES_IN_DOLLAR = 100

# take input from user
num_pennies = int(input("Enter the number of pennies: "))
num_nickels = int(input("Enter the number of nickels: "))
num_dimes = int(input("Enter the number of dimes: "))
num_quarters = int(input("Enter the number of quarters: "))

# calculate total number of cents
total_cents = (num_pennies * PENNY_VALUE) + (num_nickels * NICKEL_VALUE) + \
    (num_dimes * DIME_VALUE) + (num_quarters * QUARTER_VALUE)

# calculate total number of dollars
total_dollars = total_cents / PENNIES_IN_DOLLAR

# final statement
if total_dollars == 1.0:
    print("Congratulations!")
    print("The amount you entered was exactly one dollar!")
    print("You win the game!!")
elif total_dollars > 1.0:
    print("Sorry, the amount you entered was more than one dollar.")
else:
    print("Sorry, the amount you entered was less than one dollar.")
