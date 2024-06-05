mydict = {'name':'ronaldo',2:22,(10,20):100}
print(len(mydict))

print(mydict)
print(mydict.keys())
print(mydict['name'])
print(mydict[(10,20)])

# storing value in dictionary
mydict['score'] = 11
print(mydict)

mydict['score'] = 44
print(mydict)

print('the keys of dict are :',list(mydict))

del mydict['name']
print(mydict)

del mydict['score']
print(mydict)

# sorted(mydict)  ## 

# newdict = {'greet':1 , 'bat':2,5 :'hello'}
# print(newdict)
# sorted(newdict)

##................... another way to craete dict

anotherdict = dict(one = 1 , two = 2 ,three = 3)
print(anotherdict)

print(list(anotherdict))  ### it give keys
print(list(anotherdict.values()))   # it gives values

## ..............................................

thedict = {'one':1 , 'two':2, 'three' :3, 'four':4,'five':5 ,'six':6 }
print(thedict)

to_iterate = iter(thedict)
print(next(to_iterate))
print(next(to_iterate))
print(next(to_iterate))
print(next(to_iterate))
print(next(to_iterate))
print(next(to_iterate))

removed_value = thedict.pop('one')
print('popped key value is :',removed_value)
print('the updated dict:',thedict)

reversing = reversed(thedict)
print(next(reversing))
print(next(reversing))
print(next(reversing))
print(next(reversing))
print(next(reversing))


## updating a dict

thedict.update({'seven':7})
print(thedict)

my_dict = {'A':3, 'B':2}
print(my_dict)

print(my_dict.values())

# mydict.reversed()

keys = ['a' , 'b' , 'c']
val = [1,2,34]
mydict = dict.fromkeys(keys , val)
print(mydict)

the_dict = {'a': [1, 2, 34], 'b': [1, 2, 34], 'c': [1, 2, 34]}
print(the_dict)
print(the_dict.values())


dict1 = {'a':11 , 'b': 12 , 'c':13 , 'd':14}
print(dict1.pop('a'))
print(dict1.popitem())

my_dict = {'a': 1, 'b': 2}
other_dict = {'b': 3, 'c': 4}  ## it updates the my_dict
my_dict.update(other_dict)  # Updates my_dict with {'b': 3, 'c': 4}
print(my_dict)

# setdefault method

# Returns the value of a specified key. If the key does not exist, 
# inserts the key with a specified default value (or None if not specified) and returns the value.
dict3 = {'a': 1, 'b': 3, 'c': 4}
dict4 = dict3.setdefault('b')
print(dict4)

dict5 = dict3.setdefault('e' ,5)
print(dict5)

dict6 = {'a': 1, 'b': 3, 'c': 4}
print(dict6['a'])



#  Write a  Python script to concatenate the following dictionaries to create a new one.

# Sample Dictionary :
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

d1={1:10, 2:20}
d2={3:30, 4:40}
d3={5:50,6:60}
d4 = {}

for d in (d1 , d2 , d3):
  print(d)
  d4.update(d)

print(d4)
# //////////////////////////////////////////////////////////////////////////////////////////////