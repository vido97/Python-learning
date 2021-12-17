class RestaurantBill:
    FOOD_VAT = 14.0
    DRINK_VAT = 24.0

    def __init__(self, table_number, waitress_name):
        self.__table = table_number
        self.__waitress = waitress_name
        self.__food = []
        self.__drinks=[]

    def get_table(self):
        return self.__table

    def get_waitress(self):
        return self.__waitress

    def get_food_prices(self):
        return self.__food

    def get_drink_prices(self):
        return self.__drinks

    def add_to_bill(self, price, is_drink):
        if is_drink == True:
            self.__drinks.append(price)
        else:
            self.__food.append(price)

    def fix_price(self, line, is_drink, new_price):
        if is_drink == True:
            if line < 1 or line > len(self.__drinks):
                return False
            else:
                if new_price < 0:
                    return False
                elif new_price == 0.0:
                    del self.__drinks[line - 1]
                    return True
                else:
                    self.__drinks[line - 1] = new_price
                    return True

        else:
            if line < 1 or line > len(self.__food):
                return False
            else:
                if new_price < 0:
                    return False
                elif new_price == 0.0:
                    del self.__food[line - 1]
                    return True
                else:
                    self.__food[line - 1] = new_price
                    return True

    def calculate_drink_prices(self):
        total_price= 0.0
        total_VAT= 0.0
        total_price_notax=0.0


        for price in self.__drinks:
            total_price += price

        total_price_notax = total_price /(1+(RestaurantBill.DRINK_VAT/100))
        total_VAT = total_price - total_price_notax

        return total_price_notax, total_VAT, total_price

    def calculate_food_prices(self):
        total_price= 0.0
        total_VAT= 0.0
        total_price_notax = 0.0

        for price in self.__food:
            total_price += price

        total_price_notax = total_price /(1+(RestaurantBill.FOOD_VAT/100))
        total_VAT = total_price - total_price_notax


        return total_price_notax, total_VAT, total_price

    def calculate_total(self):
        total_bill= self.calculate_drink_prices()[2] + self.calculate_food_prices()[2]
        return total_bill

    def make_bill(self):
        bill = "Table: " + str(self.__table) + "\n" + \
            "Waitress: " +self.__waitress + "\n" + \
            "FOOD:\n"

        for food_price in self.__food:
            bill += f"{food_price:16.2f}\n"

        bill += "DRINKS:\n"

        for drink_price in self.__drinks:
            bill += f"{drink_price:16.2f}\n"

        bill += "------------------------------" + "\n" + \
            "Total " + f"{self.calculate_total():7.2f}\n"  + \
            "\n" + \
            "           sales     VAT     total\n" +\
            f"VAT 24 %: {self.calculate_drink_prices()[0]:7.2f} {self.calculate_drink_prices()[1]:7.2f} {self.calculate_drink_prices()[2]:7.2f}\n" + \
            f"VAT 14 %: {self.calculate_food_prices()[0]:7.2f} {self.calculate_food_prices()[1]:7.2f} {self.calculate_food_prices()[2]:7.2f}"

        return bill

    def __str__(self):
        info= "Table: " + str(self.__table) + "\n" + \
            "Waitress: " +self.__waitress + "\n" + \
            f"Total sum so far: {self.calculate_total():.2f} eur."

        return info





