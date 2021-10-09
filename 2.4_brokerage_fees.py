#Write a program that asks the user for the values of the stock trades. 
#The program calculates and prints the brokerage fees charged by the bank. 
    #if the value of the the stock trade is less than 800 euros, the brokerage fee is 1 % of the transaction.
    #if the value of the stock trade is at least 800 euros, the brokerage fee is 0.2 % of the transaction, or at least 8 euros.

def main():
    print("Enter the values of the trades in separated lines. Stop with a negative value.")
    trade = float(input("Enter next value of the trade.\n"))
    
    sum=0.0
    while trade >= 0:
        if trade >= 800:
            fee=(trade*0.002)
            if fee < 8:
                fee=8
        elif trade <800:
            fee =(trade * 0.01)
        trade = float(input(("Enter next value of the trade.\n"))
        sum = sum + fee
    print("The brokerage fees are",sum,"eur.")

main()

