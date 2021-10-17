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
        heating_ratio = COMPUTER_HEATING_RATIO
    elif device_type == "lights":
        heating_ratio = LIGHTS_HEATING_RATIOR
    elif device_type == "oven":
        heating_ratio = OVEN_HEATING_RATIO
    elif device_type == "washing machine":
        heating_ratio = WASHING_MACHINE_HEATING_RATIO
    
    tempurature = heating_ratio * power * (time * 60) / (SPECIFIC_HEAT_CAPACITY_AIR * AIR_DENSITY * room_size)
    return tempurature
    
def calculate_costs(power, time):
    return KWH_PRICE * (power*0.001) * (time/60)

def main():
    size=float(input("Enter the size of the room (m3).\n"))
    new_input= 'yes'
    heat_sum = 0
    cost_sum = 0

    while new_input = 'yes':
        device = str(input("Enter the device type (computer, lights, oven or washing machine).\n"))
        power = float(input("Enter the power of the device (W).\n"))
        time = int(input("Enter time of use (min).\n"))
        heat = calculate_warming(power, time, device,size)
        cost = calculate_costs(power, time)
        
        if heat == ERROR_WITH_WARMING:
            print("Invalid input.")
        else:
            heat_sum += heat
            cost_sum += cost
  
        new_input=str(input("Do you want to enter another device (yes or no)?\n"))

    print(f"The electric devices heat the room by {heat:.2f} degrees and it costs {cost:.2f} cents.")
main()
