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
