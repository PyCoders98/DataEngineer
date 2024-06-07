import math

# Write a Python function that takes a list of numbers and returns a new list containing only the even numbers from the original list.
l = [i for i in range(20)]
print(list(filter(lambda x: x % 2 == 0, l)))

# Create a function that filters a list of strings to return only those that contain a specific substring.
l = ["hello", "how", "are", "you", "I", "am", "fine"]
substring = "h"
print(list(filter(lambda l: substring in l, l)))

# Write a Python program that reads a list of strings from the user and then filters out all the strings t
# hat have a length greater than a specified value.
l = ["apple", "banana", "orange", "grape", "kiwi"]
length = 4
print(list(filter(lambda x: len(x) > length, l)))

# Write a Python function that filters a list of integers to return only prime numbers.
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


# Create a function that filters a list of strings to return only those that are palindromes.
def is_pelindrome(str):
    str2 = str[::-1]
    if str == str2:
        return str
    else:
        return None
print(list(filter(is_pelindrome,["level", "python", "radar", "programming"])))

# Write a Python function that takes a list of words and returns a new list containing only the words that start with a vowel.
def starts_with_vowel(i):
    if i[0]=="a" or i[0]=="e" or i[0]=="i" or i[0]=="o" or i[0]=="u":
        return i
l = ["apple", "banana", "orange", "grape", "kiwi"]
print(list(filter(starts_with_vowel,l)))    



