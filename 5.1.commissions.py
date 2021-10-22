#The user has a sales job, and they get commissions for each sale they make. 
#For each sale of 500 euros or more, they get a 13.5 % commission and for each sale smaller than that, they get a 6.5 % commission
#The program  go through the list of sales and calculate and print the commissions for each sale. 
#At the end, the total amount of commissions is printed.

def main():
    days = int(input("How many sales will you input?\n"))
    sales = [0.0] * days
    for i in range(days):
        sales_day = float(input("Enter the next amount.\n"))
        sales[i] = sales_day

    print("Commissions")

    LIMIT = 500             # euros
    NORMAL_COMMISSION = 6.5 # %
    BONUS_COMMISSION = 13.5   # %

    # sales and calculates and prints the commissions based on those sales.
    total_sum = 0
    for sales_day in sales:
        if sales_day < 500:
            commission = sales_day * (NORMAL_COMMISSION/100)
        else:
            commission = sales_day * (BONUS_COMMISSION/100)
        print(f"{commission:.2f} eur")
        total_sum = total_sum + commission

    # Write then a command here that prints the total of commissions.
    print(f"Total commissions {total_sum:.2f} eur.")
main()
