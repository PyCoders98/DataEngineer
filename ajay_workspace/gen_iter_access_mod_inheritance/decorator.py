import time

# Write a Python program to create a decorator that logs the arguments and
# return value of a function.


def function1(fun):
    def mul(*args):
        return fun(*args)

    return mul


@function1
def func(*args):
    m = 1
    print("args", args)
    for i in args:
        m *= i
    return m


print(func(1, 2, 3, 4, 5))


# program to create a decorator function to measure the execution time of a function.
def measure_time(fun):
    def mul(*args):
        start_time = time.time()
        x = fun(*args)
        end_time = time.time()
        print("Time taken for execution : ", round((end_time - start_time), 3))
        return x

    return mul


@measure_time
def func(*args, **kwargs):
    m = 1
    print("args", args)
    for i in args:
        m *= i
        for i in range(10000000):
            pass
    return m


print(func(1, 2, 3, 4, 5))


# program to create a decorator to convert the return value of a function to a specified data type.
def convert_type(fun):
    def inner(*n, **kwargs):
        print("Current type : ", type(n))
        s = str(fun(n))
        return s

    return inner


@convert_type
def fun(n):
    return n


print(type(fun(123)))


# program that implements a decorator to validate function arguments based on a given condition.
def validate_condition(condition):
    def wrapper(func):
        def inner(*a, **k):
            if condition(*a, **k):
                return func(*a, **k)
            else:
                try:
                    raise ValueError("Invalid arguments passed to the function")
                except ValueError as e:
                    print(e)

        return inner

    return wrapper


@validate_condition(lambda x: x > 0)
def calculate(n):
    return n**n


x = calculate(0)
if x is not None:
    print(calculate(0))
print(calculate(5))
