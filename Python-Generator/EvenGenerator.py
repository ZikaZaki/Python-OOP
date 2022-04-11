def even_generator(max):
    n = 2

    while n <= max:
        yield n
        n += 2


numbers = even_generator(4)
print(next(numbers))
print(next(numbers))


print("**************Fibonacci Sequence**************")


def generate_fibonacci():
    n1 = 0
    n2 = 1
    while True:
        yield n1
        n1, n2 = n2, n1 + n2


seq = generate_fibonacci()
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
print(next(seq))
