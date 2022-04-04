class Employee:
    # defining the properties and initializing them using the initializing method __init__
    def __init__(self, ID=None, salary=0, department=None):
        self.ID = ID
        self.__salary = salary  # salary is a private property
        self.department = department

    # method overloading
    def demo(self, a, b, c, d=5, e=None):
        print("a =", a)
        print("b =", b)
        print("c =", c)
        print("d =", d)
        print("e =", e)

    def displaySalary(self):
        print("Salary: ", self.__salary)

    # creating a private method
    def __displayID(self):
        print("ID: ", self.ID)

    def tax(self):
        return (self.__salary * 0.2)

    def salaryPerDay(self):
        return (self.__salary / 30)


# Initianlizing an object of the Employee class
Steve = Employee(3789, 2500, "Human Resources")
print("Demo 1:")
Steve.demo(1, 2, 3)
print("Demo 2:")
Steve.demo(1, 2, 3, 4)
print("Demo 3:")
Steve.demo(1, 2, 3, 4, 5)

# printing properties of Steve
print("Steve:")
print("ID: ", Steve.ID)
# print("Salary: ", Steve.__salary) # __salary is a private property and cannot be accessed directly
print("Department: ", Steve.department)
print("Tax paid by Steve: ", Steve.tax())
print("Salary per day of Steve: ", Steve.salaryPerDay())

# in Python there's no private attributes,
# but there's a way to hide the properties of an object
# and those objects can be accessed by _<ClassName> prefix when is necessary
print(Steve._Employee__salary)
