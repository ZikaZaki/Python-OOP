from CombustionEngine import CombustionEngine
from ElectricEngine import ElectricEngine


class HybridEngine(CombustionEngine, ElectricEngine):
    def __init__(self, engine_type):
        super().__init__(engine_type)

    def printDetails(self):
        print("This is a %s engine." % self.engine_type)
        print("Power: ", self.power)
        print("Tank Capacity:", self.tankCapacity)
        print("Charge Capacity:", self.chargeCapacity)


car = HybridEngine("Hybrid")
car.setPower("2000 CC")
car.setChargeCapacity("250 W")
car.setTankCapacity("20 Litres")
car.printDetails()
