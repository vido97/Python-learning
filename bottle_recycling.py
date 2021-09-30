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

    
    if bottle > 5:
        print("Unknown bottle type.")
    total = 0
    while bottle >=0:
        if bottle == 0:
            total = total + 15
        if bottle == 1:
            total = total + 10
        if bottle == 2:
            total = total + 10
        if bottle == 3:
            total = total + 20
        if bottle == 4:
            total = total + 40
        if bottle == 5:
            total = total + 0
        if bottle < 0:
                break
        bottle = int(input("Enter the type of the next bottle. Stop with a negative number:\n"))
        if bottle >5:
            print("Unknown bottle type.")
    print(f"You got {(total//100):d} euros and {(total%100):d} cents from the bottles.")

main()