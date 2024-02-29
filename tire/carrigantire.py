from typing import List
from tire.tire import Tire


class CarriganTire(Tire):

    def __init__(self, tire_wear: List[float]) -> None:
        assert len(tire_wear) == 4
        assert all(0 <= num <= 1 for num in tire_wear)
        self.tire_wear = tire_wear

    def needs_service(self):
        tire_worn_threshold = 0.9
        for tire_worn_ratio in self.tire_wear:
            if tire_worn_ratio > tire_worn_threshold:
                return True
        return False
