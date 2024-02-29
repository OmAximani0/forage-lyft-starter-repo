from typing import List
from tire.tire import Tire


class OctoprimeTire(Tire):

    def __init__(self, tire_wear: List[float]) -> None:
        assert len(tire_wear) == 4
        assert all(0 <= num <= 1 for num in tire_wear)
        self.tire_wear = tire_wear

    def needs_service(self):
        worn_threshold = 3.0
        return sum(self.tire_wear) > worn_threshold
