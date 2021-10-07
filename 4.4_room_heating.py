AIR_DENSITY = 1.225 # kg/m3
SPECIFIC_HEAT_CAPACITY_AIR = 1012 # J/(kg*celcius)
COMPUTER_HEATING_RATIO = 0.92
LIGHTS_HEATING_RATIO = 0.90
OVEN_HEATING_RATIO = 0.95
WASHING_MACHINE_HEATING_RATIO = 0.8
ERROR_WITH_WARMING = -99
KWH_PRICE = 9.89 # cents/kWh

def calculate_warming(power, time, device_type, room_size):
    if (power<0 or time<0 or device_type not in ("computer", "lights", "oven", "washing machine")):
        return ERROR_WITH_WARMING
    elif device_type == "computer":
        return (COMPUTER_HEATING_RATIO * power * (time*60)/(SPECIFIC_HEAT_CAPACITY_AIR * AIR_DENSITY * room_size))
    elif device_type == "lights":
        return (LIGHTS_HEATING_RATIO * power * (time * 60) / (SPECIFIC_HEAT_CAPACITY_AIR * AIR_DENSITY * room_size))
    elif device_type == "oven":
        return (OVEN_HEATING_RATIO * power * (time * 60) / (SPECIFIC_HEAT_CAPACITY_AIR * AIR_DENSITY * room_size))
    elif device_type == "washing machine":
        return (WASHING_MACHINE_HEATING_RATIO * power * (time * 60) / (SPECIFIC_HEAT_CAPACITY_AIR * AIR_DENSITY * room_size))

def calculate_costs(power, time):
    return KWH_PRICE * (power*0.001) * (time/60)

def main():
    size=float(input("Enter the size of the room (m3).\n"))
    device=str(input("Enter the device type (computer, lights, oven or washing machine).\n"))
    power=float(input("Enter the power of the device (W).\n"))
    time=int(input("Enter time of use (min).\n"))
    heat = 0
    cost = 0

    if (power<0 or time<0 or device not in ("computer", "lights", "oven", "washing machine")):
        print("Invalid input.")

    else:
        heat= calculate_warming(power, time, device,size)
        cost= calculate_costs(power, time)

    next_device=str(input("Do you want to enter another device (yes or no)?\n"))

    while next_device == "yes":
        device = str(input("Enter the device type (computer, lights, oven or washing machine).\n"))
        power = float(input("Enter the power of the device (W).\n"))
        time = int(input("Enter time of use (min).\n"))
        if (power<0 or time<0 or device not in ("computer", "lights", "oven", "washing machine")):
            print("Invalid input.")

        else:
            new_heat = calculate_warming(power, time, device,size)
            new_cost = calculate_costs(power, time)
            heat= heat + new_heat
            cost= cost + new_cost

        next_device = str(input("Do you want to enter another device (yes or no)?\n"))

    print(f"The electric devices heat the room by {heat:.2f} degrees and it costs {cost:.2f} cents.")





main()