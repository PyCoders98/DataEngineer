# fibonacci
def fib(limit):
    a = 0
    b = 1
    while a < limit:
        yield a
        a, b = b, a + b


print("fibonacci series : ")
for i in fib(10):
    print(i, end=", ")


# Write a Python generator function called power_of_two that generates powers of two up to a given exponent n.
# The generator should take an integer n as input and yield each power of two from 2^0 up to 2^n.
def power_of_two(n):
    a = 0
    while a < n:
        yield 2**a
        a += 1


print("\npower of 2 : ")
for i in power_of_two(8):
    print(i, end=", ")


# Write a Python generator function called even_numbers that takes an integer n as input and yields the first
# n even numbers starting from 2.
def even_numbers(n):
    for i in range(2, n):
        if i % 2 == 0:
            yield i


print("\neven numbers : ")
for i in even_numbers(40):
    print(i, end=", ")


# Write a Python generator function called range_squared that takes two integers start and end as input and generates
# the squares of numbers within the range [start, end).


def range_squared(start, end):
    while start <= end:
        yield start**2
        start += 1


print("\nrange squared : ")
for i in range_squared(2, 30):
    print(i, end=", ")


# Write a Python generator function called countdown that takes an integer n as input and generates a countdown sequence
# starting from n down to 1.

def countdown(n):
    a=abs(n)
    while a>=1:
        yield a
        a-=1
print("\ncountdown : ")
for i in countdown(30):
    print(i,end=", ")

# Write a Python generator function called even_odd that takes an integer n as input and generates a sequence of alternating 
# even and odd numbers starting from 1 up to n.
def even_odd(n):
    for i in range(1,n):
        if i%2==0:
            yield i+1
        else:
            yield i-1
print("\neven odd : ")
for i in even_odd(20):
    print(i,end=", ")


