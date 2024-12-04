import random
from enum import Enum
from stats import *  # Imports the Stats class


class RandomEvent(Enum):
    FOOD_POISONING = 1
    THEFT = 2
    BITE = 3
    WAGON_DMG = 4
    LOOT = 5


# Event classes
class FoodPoisoning:
    def __init__(self, stats):
        self.stats = stats

    def execute(self):
        damage = random.randint(-5, -1)
        self.stats.party_health = max(0, self.stats.party_health + damage)
        return f"You got food poisoning, you took {-1*damage} damage. Your health is now: {self.stats.party_health}"


class Theft:
    def __init__(self, stats):
        self.stats = stats

    def execute(self):
        loss = random.randint(-9, -3)
        self.stats.money += loss
        return f"You got robbed, you lost {-1*loss} money. your money is now: {self.stats.money}"


class Bite:
    def __init__(self, stats):
        self.stats = stats

    def execute(self):
        damage = random.randint(-10, -5)
        self.stats.party_health = max(0, self.stats.party_health + damage)
        return f"One of your animals bit you! You took {-1*damage} damage. Your health is now: {self.stats.party_health}"


class WagonDmg:
    def __init__(self, stats):
        self.stats = stats

    def execute(self):
        damage = random.randint(-7, -2)
        self.stats.wagon_health += damage
        return f"Your wagon took {-1*damage} damage from poor road conditions. Your wagon's health is now: {self.stats.wagon_health}"


class Loot:
    def __init__(self, stats):
        self.stats = stats

    def execute(self):
        gold_found = random.randint(1, 10)
        self.stats.money += gold_found
        return f"You found a pouch, you found {gold_found} money. Your money is now: {self.stats.money}"

class OxenDied:
    def __init__(self, stats):
        self.stats = stats

    def execute(self):
        self.stats.oxen -= 1
        return f"One of your oxen got sick and died. You have {self.stats.oxen} oxen left."
class Clothing:
    def __init__(self, stats):
        self.stats = stats

    def execute(self):
        if self.stats.clothing > 0:
            self.stats.clothing -= 1
            return f"One of your clothes got ripped. You have {self.stats.clothing} clothes left."
        else:
            event_number = random.randint(1, 6)
            if event_number == 1:
                return FoodPoisoning(self.stats).execute()
            elif event_number == 2:
                return Theft(self.stats).execute()
            elif event_number == 3:
                return Bite(self.stats).execute()
            elif event_number == 4:
                return WagonDmg(self.stats).execute()
            elif event_number == 5:
                return Loot(self.stats).execute()
            elif event_number == 6:
                return OxenDied(self.stats).execute()
        
# Function to handle events
def events_occurred(stats):
    # pygame.mixer.music.unload()
    # pygame.mixer.music.load(os.path.join("songs", "The Long Road [ ezmp3.cc ].mp3"))
    # pygame.mixer.music.play(-1)
    event_number = random.randint(1, 7)
    if event_number == 1:
        return FoodPoisoning(stats).execute()
    elif event_number == 2:
        return Theft(stats).execute()
    elif event_number == 3:
        return Bite(stats).execute()
    elif event_number == 4:
        return WagonDmg(stats).execute()
    elif event_number == 5:
        return Loot(stats).execute()
    elif event_number == 6:
        return OxenDied(stats).execute()
    elif event_number == 7:
        return Clothing(stats).execute()


# code to test events
# if __name__ == "__main__":
    # stats_instance = Stats()  # Create an instance of Stats -- probs not a thing for final result
    # print(events_occurred(stats_instance))  # Print the result of a random event

