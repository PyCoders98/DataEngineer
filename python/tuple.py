print('lets unleash with tuple')

tup = (2)  
print(type(tup))   ## its type is int

wrong_tup = ('a')    ## its type is string
print(type(wrong_tup))

# making_tup = tuple(2)    ## it is not tuple hence throw an error
# print(type(making_tup))

right_tup = ('a',)   ## this is tuple
print(type(right_tup))

create_tup = tuple((2,3,4))
print(type(create_tup))

another_t = 'hi','how are you'
print(type(another_t))

the_tup = (3,25)
new_the_tup = (the_tup)*3
print(new_the_tup)

## concatenation in tuple ( it means it has craeted another tuple concatenating the two )
tup1 = (1,33,2,8)
tup2 = (4,555,34)

tup3 = tup1 + tup2
print('this is tuple concatinating :',tup3)

tup4 = (tup1,tup2)
print('this is nesting of tuple:' , tup4)


## 
#..............................adding two tuples  correspondings elements

tup1 = (1,3,2,8)
tup2 = (4,55,3,4)
tup3 = zip(tup1 , tup2)
print(tup3)

for (i)in zip(tup1 , tup2):
  print('adding:',i)
  
for (i,j)in zip(tup1 , tup2):
  print('adding:',i+j)


#..............................subtract two tuples  correspondings elements

tup1 = (1,3,2,8)
tup2 = (4,55,3,4)

for (i,j )in zip(tup1 , tup2):
  print('subtract:',i-j)

#..............................multi two tuples  correspondings elements
print('multiply...')
tup1 = (1,3,2,8)
tup2 = (4,55,3,4)

for (i,j )in zip(tup1 , tup2):
  print(i*j)

#..............................dividing two tuples  correspondings elements

tup1 = (1,3,2,8)
tup2 = (4,55,3,4)


for (i,j )in zip(tup1 , tup2):
  print(i/j)

# ............................................................................
# deleting entire tuple 

tuple3 = (0,1)
print(tuple3)

del tuple3

## tupl sort
print('sorting the tuple')
tup_to_sort = (4,2,54,6,5678)
print(sorted(tup_to_sort))




## tuple

nested_tup = ((2,3,4),(5,3,4),(2,3,'l'))
print(nested_tup)

print(nested_tup[0])
print(nested_tup[0][1])

for i in nested_tup:
  print(i)

for i in nested_tup:
  print(i[1])

for i,j,k in nested_tup:
  print(i,j,k)

#  ...........//////////////// some differnet things ///////////.................

list_of_tup  = [('A',1),('B',2),('C',3),('D',4)]
print(list_of_tup)

# now unzip this  
 
unzipped_tup = list(zip(*list_of_tup))
print('the unzipped tuple is :' ,unzipped_tup)


##   different ways to creating tuple

# by list
list_to_tup = tuple([3,2,4,3])
print(list_to_tup)

# by dict
dict1 = {'a':1,'B':2,'c':3}
dict_to_tup = tuple(dict1)
print(dict_to_tup)
 # by set
set_to_tup = tuple({2,4,5,6}) 
print(set_to_tup)

##   tuples can be used to create dictionary

mytup = (2,4,5,74,3,2)
mydict = dict()


for i,j in enumerate(mytup):
  mydict[i] = j
print(mydict)

tuples = (11,22,33)
mydict = dict()


t = 12345, 54321, 'hello!'
print(type(t))



