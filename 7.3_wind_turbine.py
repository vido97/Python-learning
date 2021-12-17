#The program reads the wind speeds from the file, calculates
# maximum power of the wind turbine
#the amount of the generated electrical energy,
#and the capacity factor.

AIR_DENSITY = 1.225 #kg/m³
CUTIN_VELOCITY = 3 #m/s
CUTOUT_VELOCITY = 25 #m/s
TOTAL_AREA = 8659 #m²
MAX_POWER = 3450 #kW

def calculate_powers(velocities_list):
# Power = 8/27 * ρ * v³ * A
# p= air density, v= wind speed (m/s), A= total area of the blades (m²).
    power_list=[]
    for wind_speed in velocities_list:
        if CUTIN_VELOCITY <= wind_speed <= CUTOUT_VELOCITY:
            power = (8/27 * AIR_DENSITY * (wind_speed)**3 * TOTAL_AREA)/1000
        else:
            power= 0.0
        power_list.append(power)

    return power_list

def calculate_capacity_factor(power_list):
# capacity factor (CF) = generated electrical energy / maximum electrical energy
# generated electrical energy (GEE) = sum all powers
# maximum electrical energy (MEE) = max power of wind turbine (3450 kW) *  number of hours.
    GEE = sum(power_list)
    MEE = MAX_POWER * (len(power_list))
    CF = GEE / MEE
    return CF

def main():
    file=input("Enter the name of the file containing wind velocities.\n")
    velocities_list=[]
    try:
        tempfile=open(file,"r")
        first_line = tempfile.readline()
        for line in tempfile:
            if line != first_line:
                line = line.rstrip()
                parts = line.split(",")
                if len(parts) ==6:
                    wind_speed=float(parts[5])
                    velocities_list.append(wind_speed)
        tempfile.close()
        power_list = calculate_powers(velocities_list)
        max_power= max(power_list)
        GEE = sum(power_list)
        CF = calculate_capacity_factor(power_list)

        print("")
        print(f"The maximum power of the wind turbine was {max_power:.1f} kW.")
        print(f"The wind turbine generated {GEE:.1f} kWh of electricity.")
        print(f"The capacity factor of the wind turbine was {CF:.3f}.")

    except OSError:
        print(f"Error while reading the '{file:s}' file. Program ends.")


main()