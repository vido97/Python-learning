#The user is thinking of getting contact lenses and wants to know whether it would be better to choose daily lenses or monthly lenses. 
#The program asks the user how many days per week they use contact lenses, price of the daily lenses (eur per pair), the price of the monthly lenses (eur per pair) and the price of the contact lense solution (eur per 100 ml). 
#Then, the program calculates how much the daily lenses would cost and how much the monthly lenses would cost per month. 


def main():
    days=int(input("How many days a week do you use contact lenses?\n"))
    daily_price=float(input("How much do the daily lenses cost per pair?\n"))
    monthly_price=float(input("How much do the monthly lenses cost per pair?\n"))
    solution_cost=float(input("How much does the contact lens solution cost? (euros per 100 ml)\n"))

    
    #28 days per monnth
    daily_cost=28/7*days*daily_price
    
    #only monthly lenses require solution
    #solution costs 5ml per day
    monthly_cost= 28/7*days*((5*solution_cost)/100) + monthly_price


    if (dailycost <= monthlycost) :
        print("You should buy daily lenses.\nThey cost",dailycost,"euros per month, which is", monthlycost-dailycost,"euros less than monthly lenses.")

    if (dailycost > monthlycost) and (dailycost-monthlycost<=5):
        print("Daily lenses cost ", dailycost, "euros per month, which is", dailycost - monthlycost,"euros more than monthly lenses.\nIf you prefer convenience and health, daily lenses might still be a better option.")

    if (dailycost > monthlycost) and (dailycost-monthlycost>5):
        print("You should buy monthly lenses.\nThey cost",monthlycost,"euros per month, which is", dailycost-monthlycost,"euros less than daily lenses.")

main()
