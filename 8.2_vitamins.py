def main():
    VITAMIN_DICTIONARY = {'A': 800, 'B1': 1200, 'B2': 1300, 'B3': 15000, 'B5': 5000, 'B6': 1500, 'B12': 2.0,
                          'C': 75000, 'D': 10, 'E': 9000}
    name = input("Enter the name of the food file.\n")
    food_name= name.split(".txt")

    try:
        filedic={}
        file=open(name,"r")
        for line in file:
            line = line.rstrip()
            parts = line.split(" ")
            if len(parts) == 2:
                try:
                    vitamin=parts[0]
                    amount=float(parts[1])
                    filedic[vitamin]=amount
                except ValueError:
                    print(f"Invalid amount of vitamin {vitamin:s}.")

        chosen_vitamin = input("Enter the vitamin.\n")

        if chosen_vitamin not in filedic:
            print(f"{food_name[0]:s} does not contain any vitamin {chosen_vitamin:s}.")

        elif chosen_vitamin not in VITAMIN_DICTIONARY:
            print(chosen_vitamin, "is an unknown vitamin.")

        else:
            need_amount = VITAMIN_DICTIONARY[chosen_vitamin] / (filedic[chosen_vitamin] / 100)
            if need_amount <= 1000:
                print(
                    f"You have to eat {food_name[0]:s} {need_amount:.1f} grams to reach the daily recommendation of the vitamin {chosen_vitamin:s}.")
            else:
                print(
                    f"You have to eat {food_name[0]:s} {(need_amount * 0.001):.1f} kilos to reach the daily recommendation of the vitamin {chosen_vitamin:s}.")

        file.close()

    except OSError:
        print(f"Error in reading {name:s} file.")
main()