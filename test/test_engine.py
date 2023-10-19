import unittest

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine

class TestCapulet(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 30001
        last_service_mileage = 0

        capulet = CapuletEngine(current_mileage, last_service_mileage)
        self.assertTrue(capulet.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 30000
        last_service_mileage = 0

        capulet = CapuletEngine(current_mileage, last_service_mileage)
        self.assertFalse(capulet.needs_service())


class TestWilloughby(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        current_mileage = 60001
        last_service_mileage = 0

        willoughby = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertTrue(willoughby.needs_service())

    def test_engine_should_not_be_serviced(self):
        current_mileage = 60000
        last_service_mileage = 0

        willoughby = WilloughbyEngine(current_mileage, last_service_mileage)
        self.assertFalse(willoughby.needs_service())


class TestSternman(unittest.TestCase):
    def test_engine_should_be_serviced(self):
        warning_light_on = True

        sternman = SternmanEngine(warning_light_on)
        self.assertTrue(sternman.needs_service())

    def test_engine_should_not_be_serviced(self):
        warning_light_on = False

        sternman = SternmanEngine(warning_light_on)
        self.assertFalse(sternman.needs_service())


if __name__ == '__main__':
    unittest.main()
