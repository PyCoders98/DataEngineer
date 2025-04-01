#  ....................... map() function ........................

# 1. **Square each element**: Write a function that takes a list of numbers and returns a new list
# where each element is the square of the corresponding element in the input list.

num = [2,3,5,7,9,6]

def square(x):
  return x**2

# use map function

sq_list = map(square, num)  ## it is a map object and an iterator
print(list(sq_list))

# 2. **Convert Fahrenheit to Celsius**: Write a function that takes a list of temperatures in Fahrenheit and returns a new list
# where each temperature is converted to Celsius.

# °C = (°F - 32) × 5/9
temp = [33,53,22,43]

def fah_to_celcius(x):
  celcius = (x - 32)*(5/9)
  return celcius

new_temp = list(map(fah_to_celcius, temp)) 
print(new_temp)


# 3. **Convert Strings to Uppercase**: Write a function that takes a list of strings and 
# returns a new list where each string is converted to uppercase.

list_of_str = ['apple' , 'banana', 'grapes']

def to_upper(x):
  return x.upper()

uppercase = list(map(to_upper, list_of_str))
print(uppercase)

# 4. **Calculate Length of Strings**: Write a function that takes a list of strings and returns a new list where each 
# element is the length of the corresponding string in the input list.

list_of_str1 = ['apple' , 'banana', 'grapes']

def length_of_str(x):
  return len(x)

length = list(map(length_of_str, list_of_str1))
print(length)

# or 

# length = list(map(lambda x : len(x), list_of_str1))
# print(length)


# 5. **Remove Leading Zeros from Strings**: Write a function that takes a list of strings 
# representing numbers and returns a new list where leading zeros are removed from each string.

list_of_num = ['12434','0753','95','00943','00007']

def myfun(x):
  return x.lstrip('0')    

new_list = list(map(myfun, list_of_num))
print(new_list)


# 6. **Check if Numbers are Even**: Write a function that takes a list of numbers and 
# returns a new list where each element is True if the corresponding number in the input list is even,
# and False otherwise.

num = list(range(10))
print(num)

def func(x):
  if x%2 == 0:
      return True
  else:
    return False

new_list = list(map(func, num))
print(new_list)

# 7. **Calculate Square Root of Numbers**: Write a function that takes a list of numbers and returns 
# a new list where each element is the square root of the corresponding number in the input list.
import math
num = [34,4,9,16,20]

def sq_root(x):
  return math.sqrt(x)

square_root = list(map(sq_root, num))
print(square_root)


# 8. **Count Occurrences of Characters in Strings**: Write a function that takes a
# list of strings and a character, and returns a new list where each element is the 
# count of the given character in the corresponding string.

mystring = ['papaya', 'banana']

def count_of_chars(string, char):
    return string.count(char)

the_count = list(map(lambda ele: count_of_chars(ele, 'a'), mystring))
print(the_count)


# 9. **Filter Strings by Length**: Write a function that takes a list of strings and a length threshold,
# and returns a new list containing only the strings that are longer than the threshold.

mystring = ['papaya', 'banana','appy']

def my_func(x, thresh):
  return  len(x) > thresh
    
a = list(filter(lambda  ele: my_func(ele, 4) , mystring))
print(a)

# 10. **Convert List of Lists to List of Sums**: Write a function that takes a list of lists of numbers 
# and returns a new list where each element is the sum of the corresponding list in the input list.

ls_of_ls = [[2,3,4],[1,4,5],[7,2,1]]

def add(x):
  return sum(x)

sum_of_each_ele = (list(map(add,ls_of_ls)))
print(sum_of_each_ele)


# 11. **Calculate Factorial of Numbers**: Write a function that takes a list of numbers and returns a 
# new list where each element is the factorial of the corresponding number in the input list.


# 12. **Convert List of Tuples to List of Sums**: Write a function that takes a list of tuples of 
# numbers and returns a new list where each element is the sum of the numbers in the corresponding 
# tuple in the input list.

ls_of_tup = [(2,3),(4,5,8,7),(6,7,3)]
 
def sum_of_tup(x):
  return sum(x)

tuples_sum = list(map(sum_of_tup, ls_of_tup))
print(tuples_sum)


# 13. **Capitalize First Letter of Strings**: Write a function that takes a list of strings and
# returns a new list where the first letter of each string is capitalized.


mystring = ['papaya', 'banana','appy']

def capital(x):
  return x.capitalize()

cap_str = list(map(capital, mystring))
print(cap_str)


# 14. **Calculate Exponential of Numbers**: Write a function that takes a list of numbers and 
# returns a new list where each element is e raised to the power of the corresponding number in 
# the input list.

import math
ls = [3,4,7,8,4,5]

def exponen(x):
  return math.exp(x)

exponential_ls = list(map(exponen, ls))
print(exponential_ls)


# 15. **Calculate Cumulative Sum**: Write a function that takes a list of numbers and returns
# a new list where each element is the cumulative sum up to that point.

# num = [3,4,5,6,7]

# def cum_sum(x,y):
#   return x+y

# my_sum = list(map(lambda ele: cum_sum(ele , ele ),  num))
# print(my_sum)
