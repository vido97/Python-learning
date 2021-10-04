def main():
    print("This program calculates and summarizes the estimated profits from an investment.")

    initial_investment    = float(input("Initial investment sum (eur):\n"))
    annual_profit_percent = float(input("Expected annual growth / return rate (including expenses) (%):\n"))
    per_month_investment  = float(input("Monthly investment (+) or withdrawal (-) (eur):\n"))
    years                 = float(input("For how many years are you planning to hold the investment?\n"))

    e = "eur"
    print('{:>5s} | {:>5s} | {:^10s} | {:^10s} | {:^10s} | {:^10s}'.format('Year','Month','Start','Monthly', 'End', 'Cumulative'))
    print('{:>5s} | {:>5s} | {:^10s} | {:^10s} | {:^10s} | {:^10s}'.format('','','balance','Profit', 'balance','Profit'))
    print('{:>5s} | {:>5s} | {:>10s} | {:>10s} | {:>10s} | {:>10s}'.format('','',e,e,e,e))
    print('-' * 65)

    annual_profit_multiplier = 0.01 * annual_profit_percent
    # There are 12 months in a year; let's divide the exponential growth to them expecting it to be constant:
    monthly_profit_multiplier = (1 + annual_profit_multiplier) ** (1 / 12) - 1

    # Write your code here
    month= int (years*12)
    year_nr = 1
    final_end_balance =0
    total_profit =0


    for month in range (1,month+1):

        if month > 12 and month%12 ==0:
            month = int (month / year_nr)

        if month % 12 !=0:
            year_nr = (month // 12) +1
            month = month % 12

        if month==1 and year_nr==1:
            start_balance = initial_investment
            monthly_profit = start_balance * monthly_profit_multiplier
            end_balance = start_balance + monthly_profit + per_month_investment
            cumulative_profit = monthly_profit
            final_end_balance = end_balance
            total_profit = cumulative_profit
            total_net_deposit = start_balance + per_month_investment


        else:
            start_balance = end_balance
            monthly_profit = start_balance * monthly_profit_multiplier
            end_balance = start_balance + monthly_profit + per_month_investment
            cumulative_profit = cumulative_profit + monthly_profit
            if (start_balance + per_month_investment) < 0:
                break
            final_end_balance = end_balance
            total_profit = cumulative_profit
            total_net_deposit= final_end_balance - total_profit

        print(f"{year_nr:>5d} | {month:>5d} | {start_balance:10.2f} | {monthly_profit:10.2f} | {end_balance:10.2f} | {cumulative_profit:10.2f}")
        if month % 12 == 0:
            print('-' * 65)
    print('')
    if total_net_deposit<0:
        print('Stopped printing as balance cannot go negative.')
    print(f"End balance:        {final_end_balance:10.2f} eur")
    print(f"Total profit:       {total_profit:10.2f} eur")
    print(f"Total net deposit:  {total_net_deposit:10.2f} eur")
main()