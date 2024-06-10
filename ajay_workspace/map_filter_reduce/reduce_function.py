from functools import reduce

# 1. **Calculate sum of numbers**: Write a function that takes a list of numbers and returns the sum of all the numbers.
l = [1, 2, 13, 34, 2, 34, 2, 2, 54, 23, 2, 34]
print(reduce(lambda x, y: x + y, l))

# 2. **Calculate product of numbers**: Write a function that takes a list of numbers and returns the product of all the numbers.
l = [1, 2, 13, 34, 2, 34, 2, 2, 5, 23, 2, 34]
print(reduce(lambda x, y: x * y, l))

# 3. **Calculate factorial of a number**: Write a function that takes a number and returns its factorial.
num = 6
print(reduce(lambda a, b: a * b, [i for i in range(1, num + 1)]))

# 4. **Find maximum number in a list**: Write a function that takes a list of numbers and returns the maximum number.
l = [1, 2, 13, 34, 2, 34, 2, 2, 54, 23, 2, 34]
print(reduce(lambda a, b: max(a, b), l))

# 5. **Find minimum number in a list**: Write a function that takes a list of numbers and returns the minimum number.
l = [1, 2, 13, 34, 2, 34, 2, 2, 54, 23, -2, 34]
print(reduce(lambda a, b: min(a, b), l))


# 6. **Calculate cumulative sum**: Write a function that takes a list of numbers and returns a new list where each
# element is the cumulative sum up to that point.
l = [10, 20, 30, 40, 50]
print(reduce(lambda acc, x: acc + [acc[-1] + x] if acc else [x], l, []))

# 7. **Calculate cumulative product**: Write a function that takes a list of numbers and returns a new list where each
# element is the cumulative product up to that point.
l = [10, 20, 30, 40, 50]
print(reduce(lambda acc, x: acc + [acc[-1] * x] if acc else [x], l, []))

# 8. **Concatenate strings in a list**: Write a function that takes a list of strings and returns a single string by
# concatenating all the strings together.
l = [
    "hello",
    "how",
    "are",
    "i",
    "am",
    "fine",
    "what",
    "about",
    "you",
    "nice",
    "to",
    "meet",
    "you",
]
print(reduce(lambda a, b: a + b, l))

# 9. **Count occurrences of a specific element in a list**: Write a function that takes a list
# of elements and a specific element, and returns the count of occurrences of that element in the list.
l = [
    "h",
    "e",
    "l",
    "l",
    "o",
    " ",
    "h",
    "o",
    "w",
    " ",
    "a",
    "r",
    "e",
    ",",
    " ",
    "i",
    " ",
    "a",
    "m",
    " ",
    "f",
    "i",
    "n",
    "e",
    ",",
    " ",
    "w",
    "h",
    "a",
    "t",
    " ",
    "a",
    "b",
    "o",
    "u",
    "t",
    " ",
    "y",
    "o",
    "u",
    ",",
    " ",
    "n",
    "i",
    "c",
    "e",
    " ",
    "t",
    "o",
    " ",
    "m",
    "e",
    "e",
    "t",
    " ",
    "y",
    "o",
    "u",
]
ch = "i"
print(reduce(lambda acc, x: acc + (1 if x == ch else 0), l, 0))

# 10. **Flatten a list of lists**: Write a function that takes a
# list of lists and returns a single list by flattening all the sublists.
l = [[1, 2, 3, 4], [5, 6, 7, 8], [11, 22, 33, 4], [23, 5, 667, 8]]
print(reduce(lambda acc, l: acc + l, l, []))

# 11. **Calculate average of numbers**: Write a function that takes a list of numbers
# and returns the average of those numbers.
l = [11, 221, 23, 1, 657, 978, 45]
sum = reduce(lambda a, b: a + b, l)
length = len(l)
print(round((sum / length), 2))

# 12. **Check if all elements in a list are True**: Write a function that takes a list of
# boolean values and returns True if all the elements are True, otherwise False.
l = [True, True, True, True, True, False]
print(reduce(lambda x, y: True if x == True and y == True else False, l))

# 13. **Check if any element in a list is True**: Write a function that takes a list of boolean
# values and returns True if any of the elements are True, otherwise False.
l = [False, False, False, False, False, True]
print(reduce(lambda x, y: True if x == False and y == False else False, l))

# 14. **Merge dictionaries**: Write a function that takes a list of dictionaries and merges them
# into a single dictionary.
l = [{"a": 56, "b": 2}, {"c": 3}, {"c": 9}, {"d": 4, "e": 5}]
print(reduce(lambda acc, d: {**acc, **d}, l, {}))

# 15. **Reverse a string**: Write a function that takes a string and returns its reverse.
string = "hello how are, i am fine, what about you, nice to meet you"
print(reduce(lambda x, y: y + x, string, ""))
