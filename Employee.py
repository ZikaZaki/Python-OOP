class Employee:
    # defining the properties and assigning them none
    ID = None
    salary = None
    department = None


# creating an object of the Employee class
Steve = Employee()

# assigning values to properties of Steve - an object of the Employee class
Steve.ID = 3789
Steve.salary = 2500
Steve.department = "Human Resources"
# creating a new attribute for Steve
Steve.title = "Manager"

# printing properties of Steve
print("ID: ", Steve.ID)
print("Salary: ", Steve.salary)
print("Department: ", Steve.department)
print("Title: ", Steve.title)
