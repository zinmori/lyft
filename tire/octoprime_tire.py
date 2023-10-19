from tire.tire import Tire

class OctoprimeTire(Tire):
    def __init__(self, wornArray):
        self.wornArray = wornArray
    def needs_service(self):
        return sum(self.wornArray) >= 3