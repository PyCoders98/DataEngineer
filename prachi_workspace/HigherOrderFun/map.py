# Write a  Python program to triple all numbers in a given list of integers. Use Python map

L = [2,3,4,6]

def triple(x):
  return x*3

result = map(triple, L)
print(result)  # here it create a map object and map provides an iterator

print(list(result))


