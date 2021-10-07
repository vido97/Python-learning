import math

def calculate_water_volume_and_price(diameter, height):
    #V=π * d * h
    liters = float((math.pi*(diameter/2)**2*height)*1000)
    cost =  float((math.pi*(diameter/2)**2*height)*5.0)
    print(f"You need {liters:.0f} liters of water to fill the pool.\nIt will cost you {cost:.2f} euros.")

def main():
    pool=int(input("Enter the number of pools:\n"))
    for i in range (1,pool+1):
        print(f"{i:d}. pool")
        diameter = float(input("Enter the diameter of the pool in meters:\n"))
        height = float(input("Enter the height of the pool in meters:\n"))
        calculate_water_volume_and_price(diameter, height)
main()

