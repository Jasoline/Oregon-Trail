import random
from enum import Enum
from stats import *  # Imports the Stats class


class RandomEvent(Enum):
    FOOD_POISONING = 1
    THEFT = 2
    DYSENTERY = 3
    WAGON_DMG = 4
    LOOT = 5


# Event classes
class FoodPoisoning:
    def __init__(self, stats):
        self.stats = stats

    def execute(self):
        damage = random.randint(-5, -1)
        self.stats.party_health += damage
        return f"You got food poisoning, you took {-1*damage} damage. Your health is now: {self.stats.party_health}"


class Theft:
    def __init__(self, stats):
        self.stats = stats

    def execute(self):
        loss = random.randint(-9, -3)
        self.stats.money += loss
        return f"You got robbed, you lost {-1*loss} money. your money is now: {self.stats.money}"


class Dysentery:
    def __init__(self, stats):
        self.stats = stats

    def execute(self):
        damage = random.randint(-10, -5)
        self.stats.party_health += damage
        return f"You got dysentery! You took {-1*damage} damage. Your health is now: {self.stats.party_health}"


class WagonDmg:
    def __init__(self, stats):
        self.stats = stats

    def execute(self):
        damage = random.randint(-7, -2)
        self.stats.wagon_health += damage
        return f"Your wagon took damage from poor road conditions, your wagon took {-1*damage} damage. Your wagon's health is now: {self.stats.wagon_health}"


class Loot:
    def __init__(self, stats):
        self.stats = stats

    def execute(self):
        gold_found = random.randint(1, 10)
        self.stats.money += gold_found
        return f"You found a pouch, you found {gold_found} money. Your money is now: {self.stats.money}"


# Function to handle events
def events_occurred(stats):
    # pygame.mixer.music.unload()
    # pygame.mixer.music.load(os.path.join("songs", "The Long Road [ ezmp3.cc ].mp3"))
    # pygame.mixer.music.play(-1)
    event_number = random.randint(1, 5)
    if event_number == 1:
        return FoodPoisoning(stats).execute()
    elif event_number == 2:
        return Theft(stats).execute()
    elif event_number == 3:
        return Dysentery(stats).execute()
    elif event_number == 4:
        return WagonDmg(stats).execute()
    elif event_number == 5:
        return Loot(stats).execute()


# code to test events
# if __name__ == "__main__":
    # stats_instance = Stats()  # Create an instance of Stats -- probs not a thing for final result
    # print(events_occurred(stats_instance))  # Print the result of a random event

