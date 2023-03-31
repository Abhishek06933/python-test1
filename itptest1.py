# list of rates
cleaning_rate = 60
cavity_filling_rate = 200
x_ray_rate = 100
tax_rate = 0.15

# calculating criteria
def calculate_bill(name, cleaning, cavity_filling, x_ray):
    subtotal = 0
    if cleaning == 'y':
        subtotal += cleaning_rate
    if cavity_filling == 'y':
        subtotal += cavity_filling_rate
    if x_ray == 'y':
        subtotal += x_ray_rate
    
    tax = subtotal * tax_rate
    total = subtotal + tax
    
    # discounts available 
    if total > 300:
        total *= 0.9
    elif total > 200:
        total *= 0.95
    
    # print the receipt
    print("Melanie Dental Clinic")
    print(".........................")
    print(f"reciept for pateint: {name}")
    print(".........................")
    print(f"subtotal: {subtotal}")
    print("tax 15%")
    print(f"total: {total}")

# get input from the user
name = input("Enter patient's name: ")
cleaning = input("Was cleaning performed? (y/n): ")
cavity_filling = input("Was cavity-filling performed? (y/n): ")
x_ray = input("Was X-Ray performed? (y/n): ")

# call the function to calculate the bill
calculate_bill(name, cleaning, cavity_filling, x_ray)
