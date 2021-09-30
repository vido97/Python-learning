def main():
# 1. The program asks the user for the value of the device in euros until the value is greater than zero.
    deductable = 150
    price = float(input("Enter the purchase price of your computer, smart watch or phone.\n"))
    while price <= 0:
        price = float(input("Incorrect value. Enter again the value of your device.\n"))

# 2. If the the value of the device is smaller than deductible:
    if price <= deductable:
        print("The value of your device is less than or equal to the deductible.")
        compensation = 0.0

# 3. If the value of the device is larger than deductible, ask for year:
    if price > deductable:
        year= int (input("Enter the year of the purchase.\n"))
        while year >2021:
            year= int (input("The year is not valid. Enter again the year of the purchase.\n"))

#4. Calculate compensation
        age_reduction = (2021-year)*0.25
        if age_reduction > 0.7:
            age_reduction = 0.7
        compensation = price - (deductable + (age_reduction*price))

        if compensation >2500:
            compensation = 2500
        if compensation < 0:
            compensation = 0.0
    print("The compensation is",compensation, "eur.")

main()
