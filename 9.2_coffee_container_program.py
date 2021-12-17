# Y1 AUTUMN 2021
# Basic Course in Programming Y1
# Author: Joel Lahenius, modified by Veera Laine
# Template for Exercise 9.2 Coffee containers

import container

def main():
    # Ask the names and volumes of the containers according to the example runs and
    # create three containers: large coffee cup, small coffee cup, and coffee jug.
    input1 = input("Big coffee cup name and volume: ")
    input2 = input("Small coffee cup name and volume: ")
    input3 = input("Coffee jug name and volume: ")
    data1 = input1.split("/")
    bigcup = container.LiquidContainer(data1[0], float(data1[1]), False)
    data2 = input2.split("/")
    smallcup = container.LiquidContainer(data2[0], float(data2[1]), False)
    data3 = input3.split("/")
    jug = container.LiquidContainer(data3[0], float(data3[1]), True)

    print("Created the following containers:")
    # Print here the statuse of the three created coffee containers
    print(bigcup)
    print(smallcup)
    print(jug)

    # Fill the format with the jug name"
    print(f"\nFilling {jug.get_name():s}...")
    # Fill here the coffee jug
    jug.fill()

    print("Jug status after filling:")
    # Print here the status of the coffee jug
    print(jug)

    amount_to_be_served = float(input("\nHow many litres of coffee should be served?\n"))

    # Fill the format. Sould print "Trying to pour [amount to be served] litres from [jug name] into [big cup name] and [small cup name]"
    print(f"Trying to pour {amount_to_be_served:.2f} litres from {jug.get_name():s} into {bigcup.get_name():s} and {smallcup.get_name():s}")  # This should print

    # Pour here the coffee from the jug first to the big cup and then to small cup
    poured_bigcup = jug.pour_to_another(bigcup, amount_to_be_served)
    poured_smallcup = jug.pour_to_another(smallcup, amount_to_be_served)

    # Print the amounts of the coffee poured in each container, i.e., fill the format
    print(f"Managed to pour {poured_bigcup:.2f} litres to {bigcup.get_name():s}")
    print(f"Managed to pour {poured_smallcup:.2f} litres to {smallcup.get_name():s}")

    print("\nCup and jug statuses after pouring:")
    # Print here the statuses of the containers
    print(bigcup)
    print(smallcup)
    print(jug)

    # Check whether both cups got the same amount of coffee, i.e. fill the if clause
    if bigcup.get_liquid_volume() == smallcup.get_liquid_volume():
        print("\nBoth were happy for having the same amount of coffee and lived happily everafter.")
    else:
        # Fill the format with the name of the small cup.
        print(f"\nThe holder of {smallcup.get_name():s} became angry for having less coffee and flipped their coffee cup!")
        
        # Flip here the small cup
        smallcup.flip()

        print("\nThey also flipped the jug!")
        # Flip here the coffee jug
        jug.flip()

        print("However, it had a lid, so the liquid stayed inside:")
        # Print here the status of the coffee jug
        print(jug)


        print("\nSo they had to force flip to the jug!")
        # Force flip here the coffee jug
        jug.force_flip()
        
        print("Now it's empty and no longer has a lid:")
        # Print here the status of the coffee jug
        print(jug)

        # Fill the format with the name of the big cup
        print(f"\nNext they got mad and nicked all the coffee they could from {bigcup.get_name():s}")

        # Pour here as much coffee as possible from the large cup to the small cup
        stolen_amount= bigcup.pour_to_another(smallcup,bigcup.get_liquid_volume())

        # Fill the format with the stolen amount
        print(f"{stolen_amount:.2f} litres were stolen.")
       
        print("\nCup statuses after the theft:")
        # Print here the status of the big and small cup
        print(bigcup)
        print(smallcup)

        # Fill the format with the name of the small cup
        print(f"\nNow finally the holder of {smallcup.get_name():s} can drink their coffee:")
        # Empty here the small cup
        smallcup.pour_out(smallcup.get_liquid_volume())
        # Print here the status of the small cup
        print(smallcup)
    
main()
