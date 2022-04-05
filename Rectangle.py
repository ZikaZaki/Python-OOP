from Shape import Shape


class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.sides = 4

    def getArea(self):
        return (self.width * self.height)


rec = Rectangle(6, 10)
print("Area of rectangle is:", str(rec.getArea()))
