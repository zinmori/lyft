import unittest

from tire.carrigan_tire import CarriganTire
from tire.octoprime_tire import OctoprimeTire

class TestCarrigan(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        wornArray = [0.5, 0.6, 0.8, 0.9]
        carrigan = CarriganTire(wornArray)

        self.assertTrue(carrigan.needs_service())
    def test_tire_should_not_be_serviced(self):
        wornArray = [0.5, 0.6, 0.8, 0.8]
        carrigan = CarriganTire(wornArray)

        self.assertFalse(carrigan.needs_service())

class TestOctoprime(unittest.TestCase):
    def test_tire_should_be_serviced(self):
        wornArray = [0.8, 0.7, 0.8, 0.9]
        octoprime = OctoprimeTire(wornArray)

        self.assertTrue(octoprime.needs_service())
    def test_tire_should_not_be_serviced(self):
        wornArray = [0.5, 0.6, 0.8, 0.7]
        octoprime = OctoprimeTire(wornArray)

        self.assertFalse(octoprime.needs_service())