import math

# Given a list of numbers, use the map() function to double each number in the list.
l = [1, 2, 3, 4, 5, 6, 7, 8]
print(list(map(lambda x: x + x, l)))

# Given a list of temperatures in Celsius, use the map() function to convert each temperature to Fahrenheit using the formula:

l = [23, 24, 53, 34, 2, 33, 456, 76, 66, 412, 31, 4, 3, 65, 7, -40]
print(list(map(lambda x: ((9 / 5) * x) + 32, l)))

# Given a list of strings, use the map() function to calculate the length of each string in the list.
l = ["hello", "how", "you", "nice", "to", "meet", "you"]
print(list(map(lambda x: len(x), l)))

# Given a list of strings representing numbers, use the map() function to convert each string to an integer.
l = ["2", "3", "4", "5", "6", "6", "8", "90"]
print(list(map(lambda x: int(x), l)))

# Given a list of words, use the map() function to capitalize each word in the list.

l = ["hello", "how", "you", "nice", "to", "meet", "you"]
print(list(map(lambda x: x.capitalize(), l)))

# Given a list of strings, use the map() function to reverse each string in the list.

l = ["hello", "how", "you", "nice", "to", "meet", "you"]
print(list(map(lambda x: x[::-1], l)))

# Given a list of floating-point numbers, use the map() function to round each number to the nearest integer.
l = [22.21, 23.3123, 435.43, 45.13, 45.678, 789.1]
print(list(map(lambda x: round(x), l)))

# Given a list of numbers, use the map() function to find the square of each number.

l = [1, 2, 3, 4, 5, 6, 7, 8]
print(list(map(lambda x: x ** 2, l)))

# Given a list of strings representing floating-point numbers, use the map() function to convert each string to a float.

l = ["2.2", "22.32", "4.56", "44.34", "56.32", "66.78"]
print(list(map(lambda x: float(x), l)))

# Given a list of numbers, use the map() function to calculate the exponential value (e^x) for each number.

l = [
    1,
    2,
    3,
    4,
    5,
    112,
    34,
    23,
    25,
    5,
    65,
    86,
    78,
    5,
    6,
    52,
    1,
    3,
    72,
    4,
    12,
    2,
    32,
    6,
    7,
    455,
    1,
    2,
]
print(list(map(lambda x: x ** 3, l)))

# Given a list of integers, use the map() function to convert each integer to its binary representation as a string.

l = [1, 2, 3, 4, 5, 112, 1, 2]
print(list(map(lambda x: bin(x)[2:], l)))

# Given a list of numbers, use the map() function to calculate the natural logarithm (base e) of each number.
l = [1, 2, 3, 4, 5, 112, 1, 2]
print(list(map(math.log, l)))
