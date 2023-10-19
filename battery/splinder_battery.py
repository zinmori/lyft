from datetime import datetime
from battery.battery import Battery

class SplinderBattery(Battery):
    def __init__(self, last_service_date: datetime, current_date: datetime):
        self.last_service_date = last_service_date
        self.current_date = current_date
    def needs_service(self):
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + 3)
        return service_threshold_date < self.current_date
            