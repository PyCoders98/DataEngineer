# Write a dictionary comprehension that creates a dictionary where keys are numbers from 1 to 5, 
# and values are their squares.

print({x:x**2 for x in range(6) })

# Write a dictionary comprehension that creates a dictionary where keys are numbers from 1 to 10, 
# and values are their squares, but only if the number is even.

print({x:x**2 for x in range(11) if x%2==0})

# Given a list of strings, create a dictionary where keys are the strings, and values are the 
# lengths of the strings.

print({x:len(x) for x in ["hello","how","are","you"]})

# Create a dictionary where keys are numbers from 1 to 5, and values are dictionaries where keys are
# the numbers from 1 to 3, and values are their squares.

print({x:{y:y**2 for y in range(1,3+1)} for x in range(1,5+1) })

# Write a dictionary comprehension that creates a dictionary where keys are numbers from 1 to 10, and
# values are 'Even' if the number is even, and 'Odd' if the number is odd.

print({x:"Even" if x%2==0  else "Odd" for x in range(1,11)  })

# Write a dictionary comprehension that creates a dictionary where keys are numbers from 1 to 20, 
# and values are their squares, but only for odd numbers.

print({x:x**2  for x in range(1,20) if x%2!=0})

# Given a list of strings, create a dictionary where keys are the strings, and values are the uppercase
# versions of the strings.

print({x:x.upper() for x in ["hello","how","are","you","nice","to","meet","you"]})

# Create a dictionary where keys are numbers from 1 to 5, and values are dictionaries where keys are the 
# numbers from 1 to 3, and values are 'Even' if the inner number is even, and 'Odd' otherwise.

print({x:{y:"Even" if y%2==0 else "Odd" for y in range(4)} for x in range(6)})

# Given a dictionary where keys are numbers and values are lists of numbers, create a new dictionary 
# where keys are the same, but values are the sum of the corresponding lists.

l1={1:[1,2,3],2:[2,3,4],3:[4,5,6],4:[5,6,7]}
print({ x:sum(y) for x,y in l1.items()})

# Given a list of names, create a dictionary where keys are the names, and values are their positions 
# in the list (0-indexed).

l8=["hello","how","are","you","I","am","fine","what","about","you"]
print({x[1]:x[0] for x in enumerate(l8)})
