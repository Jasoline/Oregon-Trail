import unittest
from stats import *
from randomizer import *


class OregonTest(unittest.TestCase):
    def setUp(self):
        self.stats = Stats()

    def test_year(self):
        self.assertEqual(self.stats.year, 1848)
        self.stats.year = 1850
        self.assertEqual(self.stats.year, 1850)

    def test_spare_parts(self):
        self.assertEqual(self.stats.spare_parts, 0)
        self.stats.spare_parts = 5
        self.assertEqual(self.stats.spare_parts, 5)

    def test_month_name(self):
        self.assertEqual(self.stats.month_name, "December")
        self.stats.month = 3
        self.assertEqual(self.stats.month_name, "March")

    def test_ammo(self):
        self.assertEqual(self.stats.ammo, 0)
        self.stats.ammo = 100
        self.assertEqual(self.stats.ammo, 100)

    def test_food(self):
        self.assertEqual(self.stats.food, 0)
        self.stats.food = 200
        self.assertEqual(self.stats.food, 200)

    def test_clothing(self):
        self.assertEqual(self.stats.clothing, 0)
        self.stats.clothing = 10
        self.assertEqual(self.stats.clothing, 10)

    def test_oxen(self):
        self.assertEqual(self.stats.oxen, 0)
        self.stats.oxen = 4
        self.assertEqual(self.stats.oxen, 4)

    def test_days_passed(self):
        self.assertEqual(self.stats.days_passed, 0)
        self.stats.days_passed = 10
        self.assertEqual(self.stats.days_passed, 10)

    def test_distance_travelled(self):
        self.assertEqual(self.stats.distance_travelled, 0)
        self.stats.distance_travelled = 100
        self.assertEqual(self.stats.distance_travelled, 100)

    def test_day(self):
        self.assertEqual(self.stats.day, 1)
        self.stats.day = 15
        self.assertEqual(self.stats.day, 15)

    def test_month(self):
        self.assertEqual(self.stats.month, 0)
        self.stats.month = 6
        self.assertEqual(self.stats.month, 6)

    def test_party_health(self):
        self.assertEqual(self.stats.party_health, 100)
        self.stats.party_health = 80
        self.assertEqual(self.stats.party_health, 80)

    def test_events_occurred(self):
        self.assertEqual(self.stats.events_occurred, 0)
        self.stats.events_occurred = 5
        self.assertEqual(self.stats.events_occurred, 5)

    def test_deaths(self):
        self.assertEqual(self.stats.deaths, 0)
        self.stats.deaths = 2
        self.assertEqual(self.stats.deaths, -2)

    def test_money(self):
        self.assertEqual(self.stats.money, 1600)
        self.stats.money = 2000
        self.assertEqual(self.stats.money, 2000)

    def test_wagon_health(self):
        self.assertEqual(self.stats.wagon_health, 100)
        self.stats.wagon_health = 80
        self.assertEqual(self.stats.wagon_health, 80)

    def test_update_death(self):
        self.stats.update_death()
        self.assertEqual(self.stats.deaths, 1)

    def test_events(self):
        stats = Stats()
        stats.party_health = 10
        health = stats.party_health
        event = FoodPoisoning(stats)
        event.execute()
        self.assertEqual(health > stats.party_health, True)
        event = Theft(stats)
        event.execute()
        money = stats.money
        self.assertEqual(money <= stats.money, True)
        event = Bite(stats)
        health = stats.party_health
        event.execute()
        self.assertEqual(health > stats.party_health, True)
        event = WagonDmg(stats)
        health = stats.wagon_health
        event.execute()
        self.assertEqual(health >= stats.wagon_health, True)
        event = Loot(stats)
        money = stats.money
        event.execute()
        self.assertEqual(money < stats.money, True)
        event = OxenDied(stats)
        stats.oxen = 1
        event.execute()
        self.assertEqual(stats.oxen < 1, True)
        event = Clothing(stats)
        stats.clothing = 1
        event.execute()
        self.assertEqual(stats.clothing < 1, True)


if __name__ == '__main__':
    unittest.main()
