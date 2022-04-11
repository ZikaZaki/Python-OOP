numbers = [1, 2, 9]
# print(dir(numbers)) # prints all the methods and properties in the numbers object
value = iter(numbers)

item1 = next(value)
print(item1)

item2 = next(value)
print(item2)

item3 = next(value)
print(item3)


num_list = [1, 4, 9]
iter_obj = iter(num_list)

while(True):
    try:
        element = next(iter_obj)
        print(element)
    except StopIteration:
        break
