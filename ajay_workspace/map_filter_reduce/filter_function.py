import math

# 1. **Filter even numbers**: Write a function that takes a list of numbers and returns
# a new list containing only the even numbers.
l = [i for i in range(20)]
print(list(filter(lambda x: x % 2 == 0, l)))

# 2. **Filter odd numbers**: Write a function that takes a list of numbers and returns a
# new list containing only the odd numbers.
l = [i for i in range(20)]
print(list(filter(lambda x: x % 2 != 0, l)))

# 3. **Filter positive numbers**: Write a function that takes a list of numbers and returns
# a new list containing only the positive numbers.
l = [-23, 45, -1, 32, 32, -5, 6, 67, 85, -523, 0, 7643, -4, -6475, 78, -67, -8, 9]
print(list(filter(lambda x: x > 0, l)))

# **Filter negative numbers**: Write a function that takes a list of numbers and returns a
# new list containing only the negative numbers.
l = [-23, 45, -1, 32, 32, -5, 6, 67, 85, -523, 0, 7643, -4, -6475, 78, -67, -8, 9]
print(list(filter(lambda x: x < 0, l)))

# 5. **Filter prime numbers**: Write a function that takes a list of numbers and returns a new
# list containing only the prime numbers.
l = [x for x in range(52)]


def is_prime(n):
    m = math.floor(n / 2)
    flag = 1
    if n > 1:
        for i in range(2, m + 1):
            if n % i == 0:
                flag = 0
                break
        if flag == 1:
            return n
        else:
            return None


print(list(filter(is_prime, l)))

# 6. **Filter strings by length**: Write a function that takes a list of strings and a length
# threshold, and returns a new list containing only the strings that are longer than the threshold.
l = ["apple", "banana", "orange", "grape", "kiwi"]
length = 4
print(list(filter(lambda x: len(x) > length, l)))

# 7. **Filter palindromes**: Write a function that takes a list of strings and returns a new list
# containing only the palindromic strings.
def is_pelindrome(str):
    str2 = str[::-1]
    if str == str2:
        return str
    else:
        return None


l = ["level", "novel", "python", "radar", "naman", "programming"]
print(list(filter(is_pelindrome, l)))

# 8. **Filter uppercase strings**: Write a function that takes a list of strings and returns a new
# list containing only the strings that are entirely in uppercase.
l = ["APPLE", "banana", "ORRANGE", "grape", "kiwi", "PINAPPLE", "PAPAYA"]
print(list(filter(lambda x: x == x.upper(), l)))

# 9. **Filter lowercase strings**: Write a function that takes a list of strings and returns a new
# list containing only the strings that are entirely in lowercase.
l = ["APPLE", "banana", "ORRANGE", "grape", "kiwi", "PINAPPLE", "PAPAYA"]
print(list(filter(lambda x: x != x.upper(), l)))

# 10. **Filter strings containing a specific character**: Write a function that takes a list of strings
# and a character, and returns a new list containing only the strings that contain the given character.
def contains(l):
    ch = "a"
    if ch in l:
        return True


l = ["APPLE", "banana", "ORRANGE", "grape", "kiwi", "PINAPPLE", "PAPAYA"]
print(list(filter(contains, l)))

# 11. **Filter strings containing only digits**: Write a function that takes a list of strings and returns
# a new list containing only the strings that consist of digits only.
l = ["1312", "banana", "73981", "grape", "kiwi", "23312", "1214"]
print(list(filter(lambda x: x.isdigit(), l)))

# 12. **Filter strings containing vowels**: Write a function that takes a list of strings and returns a new
# list containing only the strings that contain at least one vowel.
def contains_vowels(string):
    l = string.lower()
    if "a" in l or "e" in l or "i" in l or "o" in l or "u" in l:
        return True


l = [
    "APPLE",
    "banana",
    "ORRANGE",
    "grape",
    "kiwi",
    "PINAPPLE",
    "PAPAYA",
    "1231",
    "dddd",
]
print(list(filter(contains_vowels, l)))

# 13. **Filter strings containing a specific substring**: Write a function that takes a list of strings and
# a substring, and returns a new list containing only the strings that contain the given substring.
l = ["hello", "how", "are", "you", "I", "am", "fine"]
substring = "he"
print(list(filter(lambda l: substring in l, l)))

# 14. **Filter lists by sum**: Write a function that takes a list of lists of numbers and a threshold, and returns
# a new list containing only the lists whose sum exceeds the threshold.
def filter_by_sum(l, t):
    def calculate_sum(l1):
        return sum(l1)

    return list(filter(lambda lst: calculate_sum(lst) > t, l))


l = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [12, 21, 1], [11, 56, 21]]
print(filter_by_sum(l, t=20))

# 15. **Filter lists by average**: Write a function that takes a list of lists of numbers and an average threshold,
# and returns a new list containing only the lists whose average exceeds the threshold.
def filter_by_sum(l, t):
    def calculate_sum(l1):
        return sum(l1) / len(l1)

    return list(filter(lambda lst: calculate_sum(lst) > t, l))


l = [[1, 2, 3], [4, 5, 6], [7, 8, 9], [12, 21, 1], [11, 56, 21]]
print(filter_by_sum(l, t=20))
