from Engine import Engine


class CombustionEngine(Engine):
    def __init__(self, engine_type):
        super().__init__(engine_type)

    def setTankCapacity(self, tankCapacity):
        self.tankCapacity = tankCapacity
