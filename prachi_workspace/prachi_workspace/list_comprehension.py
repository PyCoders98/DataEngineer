new_list = [x for x in range(11)]
print(new_list)

the_list = [x for x in range(11) if x%2 != 0]
print(the_list)

another_list = [x if x%2 == 0 else 'odd' for x in range(11)]
print(another_list)

matrix = [[j for j in range(5)] for i in range(3)]
print(matrix)

list1 = [1,2,3,4]
list2 = [10,20,30,40]

for (a,b) in enumerate(zip(list1 , list2)):
  print(a,b)


for (a) in enumerate(zip(list1 , list2)):
  print(a)


# Display the sum of digits of all the odd elements in a list.
# sum = 0
for i in range(11):
  sum = 0
  if i%2 != 0:
    sum = sum+i
    print('the sum of odd elements are:',sum)
print(sum)

ele_length = [len(word) for word in 'hello']
print(ele_length)

total_length = len(ele_length)
print('the total length is :',total_length)

# creating dictionary using dictionary comprehensions

keys = ['a','b','c','d']
values = [10,20,30,40]
dict2 = {k:v for (k,v) in zip(keys,values)}
print('the dictionary is :',dict2)

dict1 = {x.upper() : x*3 for x in 'hello'}
print(dict1)

# creating dictionary 

my_dict = {'a':1,'b':2 , 'c':3}
print(my_dict)

the_dict = {'name':[2,3,4,5],
            'age' : [20,30,40,50]}
print(the_dict)

for (k,v) in dict1.items():
  print(k,v)

# print('p'*3)

# functions 

def myfun(greet):
  # print(greet)
  return greet

lets_greet = myfun('hello')
print('its time to say;' ,lets_greet)


# local variable

def local_fun():
  thesum = 7
  print(thesum)

local_fun()
# print(thesum) it gives error since outside the function thesum is not defined

# global variable

sum = 3
def add():
  print('accesing global variable inside the function:',sum)

add()   ## calling the function

print('accesing global variable outside the function:' ,sum)

name = 'yes'
def myfun():
  name = 'no'
  print('it will print local;',name)

myfun()
print('it will print global; ' ,name)

string = 'hi'

def my_func():
  global string
  string = string + ' ' + 'there'
  print(string)

my_func()

# some common stuffs

myname = None
print('let see what it print:',myname)

print(True+True+True)
print(False+False+False)
print(True+False)
# print(myname+myname)   ## none cant add

# ................................................................functions

def cube(num):
  return num**3

thecube = cube(4)
print(thecube)

# ....................................................................del keyword


# myvar = 'hello'
# print(myvar)
# del(myvar)
# print(myvar)

#.................................nonlocal variable 
def outer():
  x = 10
  print('one:',x)

  def inner():
    nonlocal x
    x = x+5
    return x
  
  call_inner = inner()
  print(call_inner)

  return x*10

call_outer = outer()
print(call_outer)

# indexing and slicing

word = 'abcdefghijklmnopqrst'
print('1',word[5:9])
print('2' ,word[5:9:-1])
print('3', word[-9:9:-1])
print('4',word[-9:-2:-1])
print('4',word[-9:-2:1])
print('5',word[-9:15])
print('6',word[-9::-1])
print('7',word[::])
print('8',word[::-1])


# input and output function

# number = input('Enter a number')
# print(number)

# if else elif

x = 70

if x>3000:
  print('great than 20')
else:
  pass

y = 20

if y>90:
  print('gretaer than 20')
elif y==30:
  print('30')
elif y<30:
  print('y is less than 30')
else:
  pass

# for loop with dictionary
dict1 = dict()

dict1['a'] = 1
dict1['b'] = 2
dict1['c'] = 3

print(dict1)
dict1.update({'d':4})
print(dict1)

for i in dict1:
  print(i)
for j in dict1.keys():
  print(j)
for k in dict1.values():
  print(k)
for l in dict1.items():
  print('items:',l)

for (key,val) in dict1.items():
  print(key,val)
print()
for i in dict1:
  print(i,dict1[i])


matrix = [[j for j in range(5)] for i in range(3)]
print(matrix)


for i in range(1,4):
  for j in range(1,5):
    print(j)  

new_list = {x : x*2 for x in range(10)}
print(new_list)

###########  list comprehensions

num = [x for x in range(10)]
print(num)

sq_num = [x * 2 for x in range(5)]
print(sq_num)

even =[x if x%2 == 0 else 'odd' for x in range(5)]
print(even)
### ///////////////////////////////////////////////////////////////////