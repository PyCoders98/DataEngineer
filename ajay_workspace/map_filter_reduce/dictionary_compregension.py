# 1. **Square numbers from 1 to 5 and store them in a dictionary**:
#    Write a dictionary comprehension to generate a dictionary where keys are numbers from 1 to 5,
#  and values are the squares of those numbers.
print({x: x ** 2 for x in range(1, 6)})

# 2. **Convert a list of tuples into a dictionary**:
#    Given a list of tuples where each tuple contains a key-value pair, write a dictionary comprehension to convert the list into a dictionary.
t = [(1, 2), (3, 4), (6, 5)]
print({x: y for x, y in t})


# 3. **Count the frequency of characters in a string**:
#    Given a string, write a dictionary comprehension to count the frequency of each character in the string.
string = "hello how are, i am fine, what about you, nice to meet you"
print({x: string.count(x) for x in string})

# 4. **Convert keys to uppercase in a dictionary**:
#    Given a dictionary with lowercase keys, write a dictionary comprehension to convert all keys to uppercase.

l = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
print({x.upper(): y for x, y in l.items()})

# 5. **Swap keys and values in a dictionary**:
#    Given a dictionary, write a dictionary comprehension to swap keys and values.
l = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5}
print({x: y for y, x in l.items()})
