def main():
    print("Enter the values of the trades in separated lines. Stop with a negative value.")
    line = input("Enter next value of the trade.\n")
    value = float(line)
    sum=0.0
    while value >= 0:
        if value >= 800:
            fee=(value*0.002)
            if fee < 8:
                fee=8
        elif value <800:
            fee =(value * 0.01)
        line = input("Enter next value of the trade.\n")
        value = float(line)
        sum = sum + fee
    print("The brokerage fees are",sum,"eur.")

main()

