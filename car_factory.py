from battery.nubbin_battery import NubbinBattery
from battery.splinder_battery import SplinderBattery
from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine
from car import Car
from tire.octoprime_tire import OctoprimeTire
from tire.carrigan_tire import CarriganTire

class CarFactory():
    @staticmethod
    def create_calliope(current_date, last_service_date, current_mileage, last_service_mileage, wornArray):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SplinderBattery(last_service_date, current_date)
        tire = OctoprimeTire(wornArray)
        car = Car(engine, battery, tire)
        return car
    @staticmethod
    def  create_glissade(current_date, last_service_date, current_mileage, last_service_mileage, wornArray):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SplinderBattery(last_service_date, current_date)
        tire = OctoprimeTire(wornArray)
        car = Car(engine, battery, tire)
        return car
    @staticmethod
    def create_palindrome(current_date, last_service_date, warning_light_on, wornArray):
        engine = SternmanEngine(warning_light_on)
        battery = SplinderBattery(last_service_date, current_date)
        tire = CarriganTire(wornArray)
        car = Car(engine, battery)
        return car
    @staticmethod
    def create_rorschach(current_date, last_service_date, current_mileage, last_service_mileage, wornArray):
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = CarriganTire(wornArray)
        car = Car(engine, battery, tire)
        return car
    @staticmethod
    def create_thovex(current_date, last_service_date, current_mileage, last_service_mileage, wornArray):
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(last_service_date, current_date)
        tire = OctoprimeTire(wornArray)
        car = Car(engine, battery, tire)
        return car





