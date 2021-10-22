#The program determines the combination of two resistors,
# which provide the total resistance which is closest to the desired resistance when resistors are connected in series or parallel.

def resistors_in_parallel(resistor_list, target):
    max_difference = 0.02
    i=0
    good_combination = []
    for i in range (len(resistor_list)):
        first_resistor = resistor_list[i]
        for second_resistor in resistor_list :
            if resistor_list.index(second_resistor) != i:
                resistance = 1/ (1/first_resistor + 1/second_resistor)
                if (1-max_difference) <= resistance/target <=1:
                    good_combination.append(resistance)
                    good_combination.append(first_resistor)
                    good_combination.append(second_resistor)

    if len(good_combination) >0:
        if good_combination[1] > good_combination[2]:
            return good_combination[0],good_combination[1], good_combination[2]
        elif good_combination[2] > good_combination[1]:
            return good_combination[0], good_combination[2], good_combination[1]
        else:
            return good_combination[0], good_combination[1], good_combination[2]
    else:
        return 0.0,0.0,0.0

def resistors_in_series(resistor_list, target):
    max_difference = 0.02
    i = 0
    good_combination = []
    for i in range(len(resistor_list)):
        first_resistor = resistor_list[i]
        for second_resistor in resistor_list:
            if resistor_list.index(second_resistor) != i:
                resistance = first_resistor + second_resistor
                if (1 - max_difference) <= resistance / target <= 1:
                    good_combination.append(resistance)
                    good_combination.append(first_resistor)
                    good_combination.append(second_resistor)

    if len(good_combination) > 0:
        if good_combination[1] > good_combination[2]:
            return good_combination[0], good_combination[1], good_combination[2]
        elif good_combination[2] > good_combination[1]:
            return good_combination[0], good_combination[2], good_combination[1]
        else:
            return good_combination[0], good_combination[1], good_combination[2]
    else:
        return 0.0, 0.0, 0.0

def main():
    target_resistance=float(input("Enter the desired resistance in ohms.\n"))
    registor_list=[]
    registor = float(input("Enter the resistances of the resistors in ohms and stop with a negative value.\n"))
    if registor > 0:
        registor_list.append(registor)
    while registor > 0:
        registor = float(input())
        registor_list.append(registor)
    parallel=resistors_in_parallel(registor_list,target_resistance)
    series = resistors_in_series(registor_list,target_resistance)

    if parallel[0] == 0.0 and series[0] == 0.0:
        print ("No suitable resistors.")
    else:
        if (target_resistance - parallel[0]) < (target_resistance - series[0]):
            first_resistor = parallel[1]
            second_resistor = parallel[2]
            type = "parallel"
        elif (target_resistance - parallel[0]) > (target_resistance - series[0]):
            first_resistor = series[1]
            second_resistor = series[2]
            type = "series"
        elif parallel[0] == series[0]:
            first_resistor = series[1]
            second_resistor = series[2]
            type = "series"

        print(f"The best combination of resistors is {first_resistor:.1f} ohm and {second_resistor:.1f} ohm resistors connected in {type:s}.")

main()