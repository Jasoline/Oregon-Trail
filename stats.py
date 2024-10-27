class Stats:
    def __init__(self):
        # Initialize instance variables
        self.__distance_travelled = 0  # Distance travelled by the party
        self.__days_passed = 0  # Number of days passed
        self.__day = 1,  # Current day of the month
        self.__month = 0  # Current month
        self.__month_names = ["January", "February", "March", "April", "May", "June", "July", "August", "September",
                              "October", "November", "December"]
        self.__party_health = 100  # Health of the party
        self.__events_occurred = 0  # Number of events occurred
        self.__deaths = 0  # Number of deaths
        self.__money = 0  # Amount of money
        self.__ammo = 0  # Amount of ammunition
        self.__food = 0  # Amount of food
        self.__oxen = 0  # Amount of oxen
        self.__clothing = 0  # Amount of clothing
        self.__wagon_health = 100  # Health of the wagon
    @property
    def month_name(self):
        # Return the list of month names
        return self.__month_names[self.__month - 1]
    @property
    def ammo(self):
        # Return the amount of ammunition
        return self.__ammo
    @ammo.setter
    def ammo(self, ammo):
        # Set the amount of ammunition
            self.__ammo += ammo
    @property
    def food(self):
        # Return the amount of food
        return self.__food
    @food.setter
    def food(self, food):
        # Set the amount of food
            self.__food += food
    @property
    def clothing(self):
        # Return the amount of clothing
        return self.__clothing
    @clothing.setter
    def clothing(self, clothing):
        # Set the amount of clothing
            self.__clothing += clothing
    @property
    def oxen(self):
        # Return the amount of oxen
        return self.__oxen
    @oxen.setter
    def oxen(self, oxen):
        # Set the amount of oxen
            self.__oxen += oxen
    @property
    def days_passed(self):
        # Return the number of days passed
        return self.__days_passed

    @days_passed.setter
    def days_passed(self, days):
        # Set the number of days passed
        self.__days_passed += days

    @property
    def distance_travelled(self):
        # Return the distance travelled by the party
        return self.__distance_travelled

    @distance_travelled.setter
    def distance_travelled(self, distance):
        # Set the distance travelled by the party
        self.__distance_travelled = distance

    @property
    def day(self):
        # Return the current day of the month
        return self.__day

    @day.setter
    def day(self, day):
        # Set the current day of the month
        self.__day = day

    @property
    def month(self):
        # Return the current month
        return self.__month

    @month.setter
    def month(self, month):
        # Set the current month
        self.__month = month

    @property
    def party_health(self):
        # Return the health of the party
        return self.__party_health

    @party_health.setter
    def party_health(self, health):
        # Set the health of the party
        self.__party_health += health

    @property
    def events_occurred(self):
        # Return the number of events occurred
        return self.__events_occurred

    @events_occurred.setter
    def events_occurred(self, events):
        # Set the number of events occurred
        self.__events_occurred = events

    @property
    def deaths(self):
        # Return the number of deaths
        return self.__deaths

    @deaths.setter
    def deaths(self, deaths):
        # Set the number of deaths
        self.__deaths -= deaths

    @property
    def money(self):
        # Return the amount of money
        return self.__money

    @money.setter
    def money(self, money):
        # Set the amount of money
            self.__money += money

    @property
    def supplies(self):
        # Return the list of supplies
        return self.__supplies

    @property
    def wagon_health(self):
        # Return the health of the wagon
        return self.__wagon_health

    @wagon_health.setter
    def wagon_health(self, health):
        # Set the health of the wagon
            self.__wagon_health += health
        

    def update_death(self):
        # Update the number of deaths
        self.__deaths += 1

    def increase_day(self):
        # Increase the current day of the month
        if self.__month == 1 or self.__month == 3 or self.__month == 5 or self.__month == 7 or self.__month == 8 or self.__month == 10 or self.__month == 12:
            if self.__day == 31:
                self.__day = 1
                self.__month += 1
        elif self.__month == 4 or self.__month == 6 or self.__month == 9 or self.__month == 11:
            if self.__day == 30:
                self.__day = 1
                self.__month += 1
        elif self.__month == 2:
            if self.__day == 28:
                self.__day = 1
                self.__month += 1
        else:
            self.__day += 1


