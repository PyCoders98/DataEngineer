
# Question: Write a function list_operations that takes two lists and performs the following operations:
# Append an element to the first list.
# Extend the first list by the second list.
# Insert an element at a specific index in the first list.
# Remove an element from the first list.
# Pop the last element from the first list.
# Clear the second list.
# Find the index of a specific element in the first list.
# Count the occurrences of a specific element in the first list.
# Sort the first list in ascending order.
# Reverse the first list.

list1 = [10,20,30,'a','b']
list2 = [11,22,33]

def list_operations(l1 , l2):

  lis1 = l1
  lis2 = l2

  lis1.append(44)
  print('Append 44 element to the first list:',lis1)

  lis1.extend(lis2)
  print('Extend the first list by the second list :',lis1)

  lis1.insert(4,'Hello Python')
  print('Insert an element at a specific index in the first list:',lis1)

  lis1.remove('b')
  print('list after removed b:',lis1)

  lis1.pop()
  print('list after popped an element:',lis1)

  lis2.clear()
  print('the list2 has been cleared and hence contain no element :',lis2)

  print(lis1)
  print('the index of 30 is :',lis1.index(30))

  print('the count of element 10 is :',lis1.count(10))

  # print('the sorted list is :' ,lis1.sort())   ###  since in our list all the elements are not of the same datatype hence sorting id not possible

  lis1.reverse()
  print('reversed list:',lis1)
  # another way
  # print(lis1[::-1])


list_operations(list1 , list2)

#////////////////////////////////////////////////////////////////////////////////////////////////////////////

# Question: Write a function extract_sublists that takes a list and returns the following:
# The first three elements.
# The last three elements.
# Every second element.
# The list in reverse order.

def extract_sublists(l):

  # print(l[:3])   ## first three elements
  # print(l[-3:])   ## last three elements
  # # print(l)
  # print(l[::2])   ## every second element
  # print(l[::-1]) ## reverse order

  return l[:3] , l[-3:] , l[::2] , l[::-1]

sublists = extract_sublists([11,33,42,3,5,6,7,5,6,43,3,5,6,7])
print(sublists)

#////////////////////////////////////////////////////////////////////////////////////////////
# The list in reverse order.
# Question: Write a function list_comprehension_operations that performs the following:
# Create a list of squares of numbers from 1 to 10.
# Create a list of even numbers from 1 to 20.
# Create a list of tuples where each tuple contains a number and its square from 1 to 5.
# Flatten a list of lists.

def list_comprehension_operations():
  
  ## squared list ................................
  squared_list = []
  for i in range(1,11):
    squared_list.append(i**2)
  print('the squared list is :',squared_list)

## even list.........................
  even_list = []
  for j in range(1,21):
    if j%2 == 0:
      even_list.append(j)
  print('the even list is :',even_list)

# Create a list of tuples where each tuple contains a number and its square from 1 to 5.
  list_of_tuple = []

  for i,j in enumerate(range(1,6)):
    list_of_tuple.append(tuple((i+1,j**2)))
  
  print(list_of_tuple)

###  flatten list.....................
  flatten_list  = []
  list_of_lists = [[2,1,3],[11,33,55,6]]
  for l in list_of_lists:
    for j in l:
      flatten_list.append(j)
  print('the flatten list is :',flatten_list)

# list_to_be_insert = list(range(1,11))
# list_comprehension_operations(list_to_be_insert )

list_comprehension_operations()

#  /////////////////////////////////////////////////////////////////////////////////////////////////
# Question: Write a function squares_dict that creates a dictionary where the keys are numbers from 1 to 10 and the values are the squares of the keys.

def squares_dict():
  mydict = dict()

  for i in list(range(1,11)):
    mydict[i] = i**2

  print(mydict)

# a = list(range(1,11))
# print(a)
squares_dict()

# .////////////////////////////////////////////////////////////////////////////////////////////

# Question: Write a function lengths_dict that takes a list of strings and returns a dictionary where the keys are the strings and the values are their lengths.

# def lengths_dict(l):
#   mydict = {}   ## this shows empty dict
#   for i in list_of_str:
#     if i in mydict:   ## this tells is the key present in dictionary
#       mydict[i] = mydict[i]+1
#     else:
#       mydict[i] = 1

#   print(mydict)

# list_of_str = ['a','b','p','q','a','p']
# lengths_dict(list_of_str)


##################  using dict comprehension   (another way)
list_of_string = ['a','b','p','q','a','p']
lengths_dict = {x : list_of_string.count(x) for x in list_of_string}
print('dictionary where key values are its counts:',lengths_dict)

## ////////////////////////////////////////////////////////////////////////////////////////////////////
# Question: Write a function filter_dict that takes a dictionary and returns a new dictionary containing only the items where the values are even numbers.


def filter_dict(the_dict):
    empty_dict = dict()
    for k,v in the_dict.items():
        # print(k,v)
        if v % 2 == 0:
            empty_dict[k] = v
    return empty_dict

dict_with_even = filter_dict({'a':11 , 'b':12 , 'c':1 , 'd':10, 'e':14})
print(dict_with_even)

## ////////////////////////////////////////////////////////////////////////////////////////////////////


# Question: Write a function advanced_list_operations that performs the following:
# Rotate a list to the right by k steps.
# Remove duplicates from a list while maintaining order.
# Find the intersection of two lists.
# Find the union of two lists.


def advanced_list_operations():
  ## remove duplicates
  the_list = [1,2,3,4,3,2,4,5,6,7]
  unduplicated_list = []
  for i in the_list:
    if i not in unduplicated_list:
      unduplicated_list.append(i)

  list1 = [1,2,3,4]
  list2 = [4,3,5,6]
###   intersection of lists
  intersection_list = []
  for i in list1:
    if i in list2:
      intersection_list.append(i)

###  union of lists
  union_list = []

  for i in list1:
    if i not in union_list:
      union_list.append(i)
    
  for j in list2:
      if j not in union_list:
        union_list.append(j)

###  rotate a list
  # ls1 = list1[:2]
  # ls2 = list2[2:]
  # ls3 = list2+list1
  # print(ls3)

  list_to_be_rotated = [22,1,3,4,3,5,6]
  rotated_list = []
  count = 0
  for i in range(2,len(list_to_be_rotated)):
    rotated_list.append(list_to_be_rotated[i])
    count  = count+1

  for j in range(len(list_to_be_rotated)-count):
    rotated_list.append(list_to_be_rotated[j])

  return unduplicated_list , intersection_list , union_list ,rotated_list

my_list = advanced_list_operations()
print(my_list)
 ##//////////////////////////////////////////////


