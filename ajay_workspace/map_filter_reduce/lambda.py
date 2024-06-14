from random import randint
from functools import reduce
# Given a list, the task is to write a Python program to check if 
# the value exists in the list or not using the lambda function.
l=[1,2,3,4,5,6,7,8]
element = 4
x = lambda l,x:True if element in l else False
if x(l,element):
    print("Element is present!")
else:
    print("Element is not present!")

# Write a lambda function to find the N largest elements in a list of numbers.
l=[randint(10,100) for x in range(10)]
print(l)
largest_number = lambda x,y: x if x>y else y
print(reduce(largest_number,l))