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
