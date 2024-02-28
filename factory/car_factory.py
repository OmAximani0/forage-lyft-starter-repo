from car import Car
from datetime import date
from engine.engine_types.capuletengine import CapuletEngine
from engine.engine_types.sternmanengine import SternmanEngine
from engine.engine_types.willoughbyengine import WilloughbyEngine
from battery.battery_types.nubbinbattery import NubbinBattery
from battery.battery_types.spindlerbattery import SpindlerBattery


class CarFactory:

    @staticmethod
    def create_calliope(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)

        return Car(engine, battery)

    @staticmethod
    def create_glissade(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = SpindlerBattery(current_date, last_service_date)

        return Car(engine, battery)

    @staticmethod
    def create_palindrome(
        current_date: date, last_service_date: date, warning_light_on: bool
    ) -> Car:
        engine = SternmanEngine(warning_light_on)
        battery = SpindlerBattery(current_date, last_service_date)

        return Car(engine, battery)

    @staticmethod
    def create_rorschach(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        engine = WilloughbyEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)

        return Car(engine, battery)

    @staticmethod
    def create_thovex(
        current_date: date,
        last_service_date: date,
        current_mileage: int,
        last_service_mileage: int,
    ) -> Car:
        engine = CapuletEngine(current_mileage, last_service_mileage)
        battery = NubbinBattery(current_date, last_service_date)

        return Car(engine, battery)
