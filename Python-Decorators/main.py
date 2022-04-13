def inc(x):
    return x + 1


def operate(func, x):
    result = func(x)
    return result


print(operate(inc, 3))


def print_msg(message):
    greeting = "Hello"

    def printer():
        print(greeting, message)

    return printer


func = print_msg("Python is awesome")
func()
print_msg("Python is awesome")()


def printer():
    print("Hello World!")


def display_info(func):

    def inner():
        print("Executing ", func.__name__, " Function")
        func()
        print("Finished Execution")

    return inner


decorated_func = display_info(printer)
decorated_func()


def smart_divide(func):
    def inner(a, b):
        print("Dividing: ", a, "by", b)
        if b == 0:
            print("Cannot divide by 0!")
            return
        return func(a, b)
    return inner


@smart_divide
def divide(a, b):
    return a / b


print(divide(15, 3))

print(divide(15, 0))


def star(func):
    def inner(*args, **kwargs):
        print("*" * 30)
        func(*args, **kwargs)
        print("*" * 30)
    return inner


def percent(func):
    def inner(*args, **kwargs):
        print("%" * 30)
        func(*args, **kwargs)
        print("%" * 30)
    return inner


@star
@percent
def printer(msg):
    print(msg)


printer("Decorators are cool!")


# The above example is equivalent to the following:
# printer = star(percent(printer))
star(percent(printer("Decorators are cool!")))
