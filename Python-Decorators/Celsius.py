# using property class
class Celsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    # getter method
    def get_temperature(self):
        print("Getting value...")
        return self._temperature

    # setter method
    def set_temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible!")
        self._temperature = value

    # creating a property object
    temperature = property(get_temperature, set_temperature)
    # Teh above code above is equivalent to the following code:

    # make empty property
    temperature = property()
    # assign fget
    temperature = temperature.getter(get_temperature)
    # assign fset
    temperature = temperature.setter(set_temperature)


# Create a new object, set_temperature() internally called by __init__
human = Celsius(37)

# Get the temperature attribute via a getter
print(human.temperature)

# Get the to_fahrenheit() method, get_temperature() called by the method itself
print(human.to_fahrenheit())

# new constraint implementation
# human.temperature = -300

# using @property decorator


class DCelsius:
    def __init__(self, temperature=0):
        self.temperature = temperature

    def to_fahrenheit(self):
        return (self.temperature * 1.8) + 32

    @property
    def temperature(self):
        print("Getting value...")
        return self._temperature

    @temperature.setter
    def temperature(self, value):
        print("Setting value...")
        if value < -273.15:
            raise ValueError("Temperature below -273.15 is not possible!")
        self._temperature = value


# create an object
human = DCelsius(37)

print(human.temperature)

print(human.to_fahrenheit())

coldest_temp = DCelsius(-300)
