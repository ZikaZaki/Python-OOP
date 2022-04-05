from Engine import Engine


class ElectricEngine(Engine):
    def __init__(self, engine_type):
        super().__init__(engine_type)

    def setChargeCapacity(self, chargeCapacity):
        self.chargeCapacity = chargeCapacity
