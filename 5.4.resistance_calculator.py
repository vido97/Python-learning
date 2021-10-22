#The program determines the combination of two resistors,
# which provide the total resistance which is closest to the desired resistance when resistors are connected in series or parallel.

def resistors_in_parallel(resistor_list, target):
    max_difference = 0.02
    good_combination= 0.0
    R1 = 0.0
    R2 = 0.0

    for i in range (len(resistor_list)):
       for j in range(i + 1, len(resistor_list)):
           resistance = 1/ (1/resistor_list[i] + 1/resistor_list[j])
               if (1-max_difference) <= resistance/target <= (1+max_difference):
                   if abs(resistance - target) < abs(good_combination - target):
                    good_combination = resistance
                    R1 = resistor_list[i]
                    R2 = resistor_list[j]
    if R1 > R2:
        R_first = R1
        R_second = R2
    else:
        R_first = R2
        R_second = R1
    return good_combination, R_first, R_second

def resistors_in_series(resistor_list, target):
    max_difference = 0.02
    good_combination= 0.0
    R1 = 0.0
    R2 = 0.0
  
    for i in range (len(resistor_list)):
       for j in range(i + 1, len(resistor_list)):
           resistance = resistor_list[i] + resistor_list[j]
               if (1-max_difference) <= resistance/target <= (1+max_difference):
                   if abs(resistance - target) < abs(good_combination - target):
                    good_combination = resistance
                    R1 = resistor_list[i]
                    R2 = resistor_list[j]
    if R1 > R2:
        R_first = R1
        R_second = R2
    else:
        R_first = R2
        R_second = R1
    return good_combination, R_first, R_second

def main():
    target_resistance=float(input("Enter the desired resistance in ohms.\n"))
    registor_list=[]
    registor = float(input("Enter the resistances of the resistors in ohms and stop with a negative value.\n"))
    while registor > 0:
        registor = float(input())
        registor_list.append(registor)
    parallel=resistors_in_parallel(registor_list,target_resistance)
    series = resistors_in_series(registor_list,target_resistance)

    if parallel == 0.0 and series == 0.0:
        print ("No suitable resistors.")
    else:
        if (target_resistance - parallel[0]) < (target_resistance - series[0]):
            first_resistor = parallel[1]
            second_resistor = parallel[2]
            type = "parallel"
        elif (target_resistance - parallel[0]) >= (target_resistance - series[0]):
            first_resistor = series[1]
            second_resistor = series[2]
            type = "series"

        print(f"The best combination of resistors is {first_resistor:.1f} ohm and {second_resistor:.1f} ohm resistors connected in {type:s}.")

main()
