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
l = [1, 2, 13, 34, 2, 34, 2, 2, 54, 23, 2, 34]
    # return reduce(lambda acc, num: acc + [acc[-1] + num], numbers[1:], [numbers[0]])

print(reduce(lambda x,y: x + [x[-1] + y], l[1:], [l[0]]))

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

# 15. **Reverse a string**: Write a function that takes a string and returns its reverse.
string = "hello how are, i am fine, what about you, nice to meet you"
print(reduce(lambda x, y: y + x, string, ""))
