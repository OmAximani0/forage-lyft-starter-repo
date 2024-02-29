import unittest

from engine.engine_types.capuletengine import CapuletEngine
from engine.engine_types.sternmanengine import SternmanEngine
from engine.engine_types.willoughbyengine import WilloughbyEngine


class TestCapuletEngine(unittest.TestCase):

    def test_needs_service_true(self):
        current_mileage = 40_000
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        current_mileage = 0
        last_service_mileage = 0
        engine = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())


class TestSternmanEngine(unittest.TestCase):

    def test_needs_service_true(self):
        warning_light_on = True
        engine = SternmanEngine(warning_light_on)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        warning_light_on = False
        engine = SternmanEngine(warning_light_on)
        self.assertFalse(engine.needs_service())


class TestWilloughbyEngine(unittest.TestCase):

    def test_needs_service_true(self):
        current_mileage = 70_000
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(engine.needs_service())

    def test_needs_service_false(self):
        current_mileage = 0
        last_service_mileage = 0
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(engine.needs_service())


if __name__ == "__main__":
    unittest.main()
