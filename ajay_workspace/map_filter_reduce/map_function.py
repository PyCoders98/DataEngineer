import math

# Q Write a function that takes a list of integers and returns a list where each element is squared.
l = [1, 2, 3, 4, 5, 6, 7, 8]
print(list(map(lambda x: x ** 2, l)))

# Q Write a function that takes a list of strings and returns a list where each string is converted to upper case.
l = ["hello", "how", "are", "you"]
print(list(map(lambda x: x.upper(), l)))

# Q Write a function that takes a list of words and returns a list of their first letters.
l = ["hello", "how", "are", "you"]
print(list(map(lambda x: x.capitalize(), l)))

# 1. **Square each element**: Write a function that takes a list of numbers and returns a new list where each element
#  is the square of the corresponding element in the input list.
l = [1, 2, 3, 4, 5, 6, 7, 8]
print(list(map(lambda x: x ** 2, l)))

# 2. **Convert Fahrenheit to Celsius**: Write a function that takes a list of temperatures in Fahrenheit and returns a
# new list where each temperature is converted to Celsius.
l = [23, 24, 53, 34, 2, 33, 456, 76, 66, 412, 31, 4, 3, 65, 7, -40]
print(list(map(lambda x: ((9 / 5) * x) + 32, l)))

# 3. **Convert Strings to Uppercase**: Write a function that takes a list of strings and returns a new list where each
# string is converted to uppercase.
l = ["hello", "how", "are", "you"]
print(list(map(lambda x: x.upper(), l)))

# 4. **Calculate Length of Strings**: Write a function that takes a list of strings and returns a new list where each
# element is the length of the corresponding string in the input list.
l = ["hello", "how", "are", "you", "I", "am", "fine", "what", "about", "you"]
print(list(map(lambda x: len(x), l)))

# 5. **Remove Leading Zeros from Strings**: Write a function that takes a list of strings representing numbers and returns
# a new list where leading zeros are removed from each string.
l = ["221", "002", "0123", "89834", "099898", "00000", "000023213", "0721638"]
print(list(map(lambda x: x.lstrip("0"), l)))

# 6. **Check if Numbers are Even**: Write a function that takes a list of numbers and returns a new list where each element
# is True if the corresponding number in the input list is even, and False otherwise.
l = [123, 4, 3, 57, 657, 65, 6, 344, 12, 23, 2, 5, 7, 678, 67, 857, 45, 233]
print(list(map(lambda x: True if x % 2 == 0 else False, l)))

# 7. **Calculate Square Root of Numbers**: Write a function that takes a list of numbers and returns a new list
# where each element is the square root of the corresponding number in the input list.
l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list(map(lambda x: round(math.sqrt(x), 4), l)))

# 8. **Count Occurrences of Characters in Strings**: Write a function that takes a list of strings and a character, and
# returns a new list where each element is the count of the given character in the corresponding string.
def occurence(l):
    char = "a"
    return l.count(char)


l = ["hello", "how", "are", "you", "I", "am", "fine", "what", "about", "you"]
print(list(map(occurence, l)))

# 10. **Convert List of Lists to List of Sums**: Write a function that takes a list of lists of numbers and returns a new list
# where each element is the sum of the corresponding list in the input list.
l = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [11, 23, 2]]


def sum(l):
    sum = 0
    for i in l:
        sum += i
    return sum


print(list(map(sum, l)))

# 11. **Calculate Factorial of Numbers**: Write a function that takes a list of numbers and returns a new list where each
# element is the factorial of the corresponding number in the input list.
def fact(n):
    mul = 1
    for i in range(2, n + 1):
        mul *= i
    return mul


l = [3, 4, 5, 6, 7, 8]
print(list(map(fact, l)))

# 12. **Convert List of Tuples to List of Sums**: Write a function that takes a list of tuples of numbers and returns a new
# list where each element is the sum of the numbers in the corresponding tuple in the input list.

l = [(1, 2, 3), (4, 5, 6), (7, 8, 9), (12, 43, 56)]


def sum(l):
    sum = 0
    for i in l:
        sum += i
    return sum


print(list(map(sum, l)))

# 13. **Capitalize First Letter of Strings**: Write a function that takes a list of strings and returns a new list where the
# first letter of each string is capitalized.

l = ["hello", "how", "are", "you", "I", "am", "fine", "what", "about", "you"]
print(list(map(lambda x: x.capitalize(), l)))

# 14. **Calculate Exponential of Numbers**: Write a function that takes a list of numbers and returns a new list where each
# element is e raised to the power of the corresponding number in the input list.

l = [1, 2, 3, 4, 5, 6]
print(list(map(lambda x: x ** x, l)))
