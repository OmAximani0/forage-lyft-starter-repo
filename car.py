from serviceable import Serviceable
from engine.engine import Engine
from battery.battery import Battery


class Car(Serviceable):

    def __init__(self, engine: Engine, battery: Battery) -> None:
        self.engine = engine
        self.battery = battery

    def needs_service(self) -> bool:
        return self.battery.needs_service() or self.engine.needs_service()
