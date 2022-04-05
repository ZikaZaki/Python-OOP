from Vehicle import Vehicle


class Truck(Vehicle):
    def printDetails(self):
        print("This is a truck.")


volvo = Truck()  # creating an object of the Truck class
volvo.printDetails()  # accessing method from its own class
volvo.setTopSpeed(180)  # accessing methods from the parent class
