#program reads from a file contracts of imaginary electric companies
#determines the energy consumption of the user based on the size of their apartment and the number of residents
#asks the user for an estimate of their energy consumption
#The program determines:
# the cheapest and the most eco-friendly electricity contracts for the calculated energy consumption
#Nested dictionary
#Function

import math
def calculate_consumption(size, residents):
    BASE_CONSUMPTION = 2206  # kwh
    if size <= 30:
        area_increase = 0.0
    elif 30 < size <= 110:
        difference= size - 30
        area_increase = math.ceil(difference/10)*0.16
    elif size > 110:
        difference = size - 110
        area_increase = 8*0.16 + math.ceil(difference/10)*0.05
    if residents ==1:
        resident_increase = 0.0
    elif 1 < residents <= 3:
        resident_increase = (residents-1)*0.12
    elif residents >3:
        resident_increase = 2*0.12 + (residents-3) * 0.07
    consumption = (((area_increase+resident_increase)*BASE_CONSUMPTION)+BASE_CONSUMPTION)

    return consumption

def find_cheapest_contract(contracts, consumption):
    cheapest_cost=float('inf')
    name=""

    for contract_name in contracts:
        kWh_price = contracts[contract_name]['kWh_price']
        monthly_price= contracts[contract_name]['month_price']
        cost=(kWh_price*consumption)*0.01 + (12 * monthly_price)
        if cost < cheapest_cost:
            cheapest_cost = cost
            name=contract_name

    return name,cheapest_cost

def find_ecofriendly_contract(contracts, consumption):
    affordable_cost= float('inf')
    most_renewable = float('-inf')
    name=""

    for contract_name in contracts:
        renewable_rate = float(contracts[contract_name]['renewable'])
        if renewable_rate > most_renewable:
            most_renewable = renewable_rate


    for contract_name in contracts:
        if contracts[contract_name]['renewable'] == most_renewable:
            kWh_price = contracts[contract_name]['kWh_price']
            monthly_price= contracts[contract_name]['month_price']
            cost=(kWh_price*consumption)*0.01 + (12 * monthly_price)
            if cost < affordable_cost:
                affordable_cost=cost
                name=contract_name

    return name,affordable_cost

def print_all_contracts(contracts):
    for contract_name in contracts:
        print(contract_name)
        kWh_price = contracts[contract_name]['kWh_price']
        print(f"   kWh_price: {kWh_price:.2f}")
        monthly_price = contracts[contract_name]['month_price']
        print(f"   month_price: {monthly_price:.2f}")
        renewable_rate = float(contracts[contract_name]['renewable'])
        print(f"   renewable: {renewable_rate:.2f}")

def main():
    file=input("Enter the file name.\n")
    contract_details={}
    contracts={}

    try:
        tempfile = open(file, "r")
        first_line = tempfile.readline()
        for line in tempfile:
            if line != first_line and line != "\n":
                line = line.rstrip()
                parts = line.split(",")
                if len(parts) != 4:
                    print(f"Invalid line: {line:s}")
                else:
                    try:
                        contract_details={'kWh_price': float(parts[1]),'month_price' : float(parts[2]),'renewable' : float(parts[3])/100.0}
                        contracts[parts[0]]=contract_details
                    except ValueError:
                        print(f"Invalid value: {line:s}")
        tempfile.close()

        print("")
        size = int(input("Enter the size of your apartment (m2).\n"))
        residents = int(input("Enter the number of residents.\n"))
        user_consumption = int(input("Enter an estimate of your annual electricity consumption (kWh).\n"))

        print_all_contracts(contracts)
        consumption = calculate_consumption(size, residents)

        cheapest = find_cheapest_contract(contracts, consumption)
        eco = find_ecofriendly_contract(contracts, consumption)
        user_cheapest = find_cheapest_contract(contracts, user_consumption)
        user_eco = find_ecofriendly_contract(contracts, user_consumption)

        print("")
        print(f"The best deals according to the calculated consumption ({consumption:.0f} kwh):")
        if cheapest == eco:
            print(f"The cheapest contract is also the most eco-friendly and it is\n{cheapest[0]:s} and costs {cheapest[1]:.2f} eur/year.\n")
        else:
            print(f"The cheapest contract is {cheapest[0]:s} and costs {cheapest[1]:.2f} eur/year.")
            print(f"The most eco-friendly contract is {eco[0]:s} and costs {eco[1]:.2f} eur/year.\n")

        print(f"The best deals according to the user estimated consumption ({user_consumption:d} kwh):")
        if user_cheapest == user_eco:
            print(f"The cheapest contract is also the most eco-friendly and it is\n{user_cheapest[0]:s} and costs {user_cheapest[1]:.2f} eur/year.")
        else:
            print(f"The cheapest contract is {user_cheapest[0]:s} and costs {user_cheapest[1]:.2f} eur/year.")
            print(f"The most eco-friendly contract is {user_eco[0]:s} and costs {user_eco[1]:.2f} eur/year.")

    except OSError:
        print("Error while reading the file. Program ends.")
main()
