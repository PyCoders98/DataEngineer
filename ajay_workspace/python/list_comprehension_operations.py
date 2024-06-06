# Create a list of squares of numbers from 1 to 10
# l1=[1,2,3,4,5,6,7,8,9,10]
print([x**2 for x in range(1,11)])


# Create a list of even numbers from 1 to 20.
print([x for x in range(1,21) if x%2==0])


# Create a list of tuples where each tuple contains a number and its square from 1 to 5.
print([(x,x**2) for x in range(1,6)])

# Flatten a list of lists.
l1=[[1,2,3],[2,3,4,5],[12,21,34,12]]
print([j for i in l1 for j in i])


# Write a list comprehension that generates a list of numbers from 1 to 100, but only if 
# the number is divisible by 3 and not divisible by 5.

print([x for x in range(1,101) if x%3==0 and x%5!=0])

# Given a matrix (2D list), write a list comprehension to generate a list of all the 
# numbers that are greater than 10.
l1=[[1,11,2,21,34,2],[23,435,776,3,2,90]]
print([y for x in l1 for y in x if y > 10])

# Given a list of temperatures in Celsius, write a list comprehension to convert 
# each temperature to Fahrenheit using the formula: 

l1 = [12,34,76,87,45,122,76,1,112,43,-23,-31,-56,-270,70,-40]
print([((9/5)*i)+32 for i in l1 ])

# Given two lists of equal length, write a list comprehension to create a list of tuples where each
# tuple contains elements from both lists at the same index.

l1=["hello","how","are","you"]
l2=[1,2,3,4]
print([ (i,j) for i,j in zip(l1,l2)])

# Given a list of names, write a list comprehension to create a list of tuples where each tuple contains 
# the index and the corresponding name.

l1=["hello","how","are","you"]
print([i for i in enumerate(l1) ])

# Given two lists, write a list comprehension to generate a list of common elements between them.

l1=[1,5,2,3,4,5,6,7,8]
l2=[5,6,7,8,9,0,12,23,35]
l3=[i for i in set(l1) if i in l2 ]
print(set(l3))

# Given a list of strings, write a list comprehension to generate a list of integers parsed from
# those strings. Handle the exceptions gracefully.

l1=["1","2","3","4","5","dfd"]
print([ int(i) for i in l1 if i.isdigit()])
