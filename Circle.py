from Shape import Shape


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
        self.sides = 0

    def getArea(self):
        return (self.radius * self.radius * 3.142)


circ = Circle(7)
print("Area of circle is:", str(circ.getArea()))
