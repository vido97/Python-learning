class RentApartment:

    RENTAL_SERVICE_FEE = 100  # eur per month
    STUDIO_SIZE_LIMIT = 32  # m2
    ONE_BEDROOOM_SIZE_LIMIT = 45  # m2
    STUDIO_PRICE_LEVEL = 25  # eur/m2
    ONE_BEDROOOM_PRICE_LEVEL = 20  # eur/m2
    LARGE_PRICE_LEVEL = 18  # eur/m2
    TRANSFER_TAX = 0.02

    def __init__(self, address, rent, maintenance_charge, size, free_of_debt_price):
        self.__address = address
        self.__rent = rent
        self.__maintenance_charge = maintenance_charge
        self.__size = size
        self.__free_of_debt_price = free_of_debt_price
        self.__rental_service = False
        self.__renovation_costs = 0

    def get_address(self):
        return self.__address

    def get_rent(self):
        return self.__rent

    def get_maintenance_charge(self):
        return self.__maintenance_charge

    def get_size(self):
        return self.__size

    def get_price(self):
        return self.__free_of_debt_price

    def get_renovation_costs(self):
        return self.__renovation_costs

    def update_rental_service(self):
        if self.__rental_service == True:
            self.__rental_service = False
            return False
        else:
            self.__rental_service = True
            return True

    def increase_rent(self, new_rent):
        if new_rent >  self.__rent:
            self.__rent = new_rent
            return True
        else:
            return False

    def add_renovation_costs(self, costs):
        self.__renovation_costs += costs

    def calculate_square_meter_rent(self):
        return (self.__rent / self.__size)

    def calculate_rental_income(self):
        if self.__rental_service == True:
            costs_of_month= self.__maintenance_charge + RentApartment.RENTAL_SERVICE_FEE
        else:
            costs_of_month = self.__maintenance_charge
        transfer_tax=self.__free_of_debt_price* RentApartment.TRANSFER_TAX
        rental_income = (self.__rent - costs_of_month) * 12 / (self.__free_of_debt_price + transfer_tax + self.__renovation_costs) * 100
        return rental_income

    def compare_rental_incomes(self, other):
        if self.calculate_rental_income() > other.calculate_rental_income():
            return 1
        elif self.calculate_rental_income() == other.calculate_rental_income():
            return 0
        else:
            return -1

    def calculate_return_on_equity(self, down_payment, loan_interest):
        if self.__rental_service == True:
            costs_of_month= self.__maintenance_charge + RentApartment.RENTAL_SERVICE_FEE
        else:
            costs_of_month = self.__maintenance_charge
        ROE= (self.__rent - costs_of_month - loan_interest) * 12 / down_payment * 100
        return ROE

    def check_price_level(self):
        if self.__size < RentApartment.STUDIO_SIZE_LIMIT:
            if self.calculate_square_meter_rent() >= 25:
                return True
            else:
                return False

        elif self.__size >= RentApartment.STUDIO_SIZE_LIMIT and self.__size < RentApartment.ONE_BEDROOOM_SIZE_LIMIT:
            if self.calculate_square_meter_rent() >= 20:
                return True
            else:
                return False

        else:
            if self.calculate_square_meter_rent() >= 18:
                return True
            else:
                return False

    def __str__(self):
        if self.__rental_service == False:
            usage="not in use"
        else:
            usage="in use"
        return_str="Address: " + self.__address + "\n" +\
            "Maintenance charge: "+ str(self.__maintenance_charge) + " eur" + " \n"+ \
            "Size: " + str(self.__size) + " m2" + " \n"+ \
            "Rent: " + str(self.__rent) + " eur" + "\n"+ \
            "Rental service: " + usage
        return return_str
