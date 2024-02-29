from engine.engine import Engine


class CapuletEngine(Engine):

    def __init__(self, current_mileage: int, last_service_mileage: int) -> None:
        self.current_mileage = current_mileage
        self.last_service_mileage = last_service_mileage
        self._need_service_after_mileage = 30_000

    def needs_service(self) -> bool:
        return (
            self.current_mileage - self.last_service_mileage
        ) > self._need_service_after_mileage
