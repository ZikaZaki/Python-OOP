# import modules sys to get the type of exception
import sys

from numpy import reciprocal

randomList = ['a', 0, 2]

for entry in randomList:
    try:
        print("The entry is: ", entry)
        r = 1/int(entry)
        break
    except:
        print("Oops!", sys.exc_info()[0], "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of ", entry, "is ", r)

for entry in randomList:
    try:
        print("The entry is: ", entry)
        r = 1/int(entry)
        break
    except Exception as e:
        print("Oops!", e.__class__, "occurred.")
        print("Next entry.")
        print()
print("The reciprocal of ", entry, "is ", r)


try:
    a = int(input("Enter a positive number: "))
    if a <= 0:
        raise ValueError("That is not a positive number!")
except ValueError as ve:
    print(ve)

try:
    num = int(input("Enter a number: "))
    assert num % 2 == 0
except:
    print("Not an even number!")
else:
    reciprocal = 1/num
    print(reciprocal)
