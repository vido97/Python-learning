#The program asks for an integer corresponding to bottle type until the user gives a negative number. 
#After that, the program prints the money earned from bottles in euros and cents.

def main():
    CAN = 0
    GLASS_BOTTLE = 1
    PLASTIC_SMALL = 2
    PLASTIC_NORMAL = 3
    PLASTIC_BIG = 4
    NO_DEPOSIT_BOTTLE = 5
    CAN_DEPOSIT = 15            # cents
    GLASS_BOTTLE_DEPOSIT = 10   # cents
    PLASTIC_SMALL_DEPOSIT = 10  # cents
    PLASTIC_NORMAL_DEPOSIT = 20 # cents
    PLASTIC_BIG_DEPOSIT = 40    # cents

    print("Welcome to the bottle recycling.")
    print("Bottle types with the corresponding numbers:")
    print("Can: 0")
    print("Glass bottle: 1")
    print("Plastic bottle (0.33l): 2")
    print("Plastic bottle(0.5l): 3")
    print("Plastic bottle (1.5l): 4")
    print("No deposit bottle: 5")
    bottle = int(input("Enter the type of the first bottle. Stop with a negative number:\n"))

    total = 0
    while bottle >=0:
         if bottle == CAN:
           total += CAN_DEPOSIT
        elif bottle == GLASS_BOTTLE:
           total += GLASS_BOTTLE_DEPOSIT
        elif bottle == PLASTIC_SMALL:
           total += PLASTIC_SMALL_DEPOSIT
        elif bottle == PLASTIC_NORMAL:
           total += PLASTIC_NORMAL_DEPOSIT
        elif bottle == PLASTIC_BIG:
           total += PLASTIC_BIG_DEPOSIT
        elif bottle != NO_DEPOSIT_BOTTLE:
           print("Unknown bottle type.")
        bottle = int(input("Enter the type of the next bottle. Stop with a negative number:\n"))
        
    print(f"You got {(total//100):d} euros and {(total%100):d} cents from the bottles.")

main()
