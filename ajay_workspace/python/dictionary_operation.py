# Question: Write a function squares_dict that creates a dictionary where the keys are 
# numbers from 1 to 10 and the values are the squares of the keys.

def squares_dict():
    dict={}
    for i in range(1,11):
        dict[i]=i**2
    return dict
print(squares_dict())

# Question: Write a function lengths_dict that takes a list of strings and returns a
# dictionary where the keys are the strings and the values are their lengths.

def lengths_dict(d):
    dict={}
    for i in l1:
        dict[i]=len(i)
    return dict
l1=["Write","a","function","lengths_dict","that","a","list","of","strings","and","returns",
    "a","dictionary","where","the"]

print(lengths_dict(l1))


