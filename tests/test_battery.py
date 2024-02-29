import unittest

from datetime import date
from battery.battery_types.nubbinbattery import NubbinBattery
from battery.battery_types.spindlerbattery import SpindlerBattery


class TestNubbinBattery(unittest.TestCase):

    def test_needs_service_true(self):
        current_date = date(year=2024, month=1, day=1)
        last_service_date = date(year=2015, month=1, day=1)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date(year=2024, month=1, day=1)
        last_service_date = date(year=2023, month=1, day=1)
        battery = NubbinBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())


class TestSpindlerBattery(unittest.TestCase):

    def test_needs_service_true(self):
        current_date = date(year=2024, month=1, day=1)
        last_service_date = date(year=2015, month=1, day=1)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertTrue(battery.needs_service())

    def test_needs_service_false(self):
        current_date = date(year=2024, month=1, day=1)
        last_service_date = date(year=2023, month=1, day=1)
        battery = SpindlerBattery(current_date, last_service_date)
        self.assertFalse(battery.needs_service())


if __name__ == "__main__":
    unittest.main()
