from tire.tire import Tire

class CarriganTire(Tire):
    def __init__(self, wornArray):
        self.wornArray = wornArray
    def needs_service(self):
        return any(element >= 0.9 for element in self.wornArray)