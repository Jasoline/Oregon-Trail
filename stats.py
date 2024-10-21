class Stats:
    def __init__(self):
        self.__distance_travelled = 0
        self.__days_passed = 0
        self.__day = 31
        self.__month = 1
        self.__party_health = 100
        self.__events_occurred = 0
        self.__deaths = 0
        self.__money = 0
        self.__supplies = []
        self.__wagon_health = 100
           
    def get_days_passed(self):
        return self.__days_passed
    
    def set_days_passed(self, days):
        self.__days_passed += days

    def update_death(self):
        self.__deaths += 1
    
    def update_supplies(self, supply):
        if supply in self.__supplies:
            if self.__supplies[supply] > 0:
                self.__supplies[supply] -= 1
    
    def get_distance_travelled(self):
        return self.__distance_travelled

    def set_distance_travelled(self, distance):
        self.__distance_travelled = distance

    def get_day(self):
        return self.__day

    def set_day(self, day):
        self.__day = day

    def increase_day(self):
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
    
    def get_month(self):
        return self.__month
    
    def set_month(self, month):
        self.__month = month

    def get_party_health(self):
        return self.__party_health

    def set_party_health(self, health):
        if health > 0:
            self.__party_health += health
        else:
            self.__party_health -= health

    def get_events_occurred(self):
        return self.__events_occurred

    def set_events_occurred(self, events):
        self.__events_occurred = events

    def get_deaths(self):
        return self.__deaths

    def set_deaths(self, deaths):
        self.__deaths -= deaths

    def get_money(self):
        return self.__money

    def set_money(self, money):
        if money > 0:
            self.__money += money
        else:
            self.__money -= money
    def get_supplies(self):
        return self.__supplies

    def get_wagon_health(self):
        return self.__wagon_health

    def set_wagon_health(self, health):
        if health > 0:
            self.__wagon_health += health
        else:
            self.__wagon_health -= health
