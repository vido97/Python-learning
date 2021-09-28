def main():
    line1=input("How many days a week do you use contact lenses?\n")
    days=int(line1)
    line2=input("How much do the daily lenses cost per pair?\n")
    D=float(line2)
    line3=input("How much do the monthly lenses cost per pair?\n")
    M=float(line3)
    line4=input("How much does the contact lens solution cost? (euros per 100 ml)\n")
    S=float(line4)

    #5ml per day
    #28 days per monnth

    dailycost=4*days*D
    monthlycost= M+4*days*((5*S)/100)


    if (dailycost <= monthlycost) :
        print("You should buy daily lenses.\nThey cost",dailycost,"euros per month, which is", monthlycost-dailycost,"euros less than monthly lenses.")

    if (dailycost > monthlycost) and (dailycost-monthlycost<=5):
        print("Daily lenses cost ", dailycost, "euros per month, which is", dailycost - monthlycost,"euros more than monthly lenses.\nIf you prefer convenience and health, daily lenses might still be a better option.")

    if (dailycost > monthlycost) and (dailycost-monthlycost>5):
        print("You should buy monthly lenses.\nThey cost",monthlycost,"euros per month, which is", dailycost-monthlycost,"euros less than daily lenses.")

main()