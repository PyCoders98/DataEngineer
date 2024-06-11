from functools import reduce

##  operator

# 1. **Calculate sum of numbers**: Write a function that takes a 
# list of numbers and returns the sum of all the numbers.

list_of_num = list(range(1,5))

def add(x,y):
    return x+y
    
total_sum = reduce(add, list_of_num)
print(total_sum)

# or

total_sum = reduce((lambda x,y : x+y),list_of_num )
print(total_sum)


# 2. **Calculate product of numbers**: Write a function that takes a list of numbers and 
# returns the product of all the numbers. 

list_of_num = list(range(1,5))

total_product = reduce((lambda x, y : x*y),list_of_num )
print(total_product)


# 3. **Calculate factorial of a number**: Write a function that takes a number
#  and returns its factorial.
 
 ##  operator module , is used to perform some mathematical operations with reduce(even can us ewithout reduce)
import operator
n = 5

def fact(x,y):
    return (x*y)

factorial = reduce(fact, list(range(1,6)))
print('the factorial is :',factorial)

# or

fact = reduce(operator.mul, [1,2,3,4,5])
print(fact)

# 4. **Find maximum number in a list**: Write a function that takes 
# a list of numbers and returns the maximum number.

list_of_num = [33,51,60,4,82,55,7,85,5,3]

def maxi(x,y):
    # return x if x>y else y
    return max(x,y)

maximum = reduce(maxi, list_of_num)
print(maximum)

# 5 **Find minimum number in a list**: Write a function that takes a list of numbers and returns 
# the minimum number.

list_of_num = [33,51,60,4,82,55,7,85,5,3]


def mini(x,y):
    # return x if x<y else y
    return min(x,y)


minimum = reduce(mini, list_of_num)
print(minimum)

# 6. **Calculate cumulative sum**: Write a function that takes a list of numbers and returns a new list where each element is the 
# cumulative sum up to that point.


ls = list(range(1,6))

def calc(emp_ls, y):
    emp_ls.append(emp_ls[-1]+y)   
    return emp_ls

l = reduce(calc, ls[1:], [ls[0]]) 
print('answer of cumulat_sum:',l)

from itertools import accumulate
# ls = list(range(1,6))

# # here a concept can be added which is the  accumulate function in a itertools module

# cum_sum = accumulate(ls)   ## it provides an iterator
# print(next(cum_sum))
# print(next(cum_sum))
# print(next(cum_sum))
# print(next(cum_sum))
# print(next(cum_sum))

# # or

# cum_sum = list(accumulate(ls))
# print(cum_sum)


# 7. **Calculate cumulative product**: Write a function that takes a list of numbers and
# returns a new list where each element is the cumulative product up to that point.

# ls1  = [2,3,54,6]
# ls = [ls1[2]]
# print(type(ls))

ls = list(range(1,8))

prod = list(accumulate(ls, operator.mul))
print(prod)

# 8. **Concatenate strings in a list**: Write a function that takes a list of strings and returns a single string by concatenating 
# all the strings together.

list_of_str = ['a','b','c','d','e']

def conct(x,y):
    return x+y

concat_str = reduce(conct, list_of_str)
print(concat_str)

# 9. **Count occurrences of a specific element in a list**: Write a function that takes a list of elements and a specific element, and r
# eturns the count of occurrences of that element in the list.



# 15. **Reverse a string**: Write a function that takes a string and returns its reverse.

string = 'abcdefg'

def reverse_str(x,y):
    return y+x

the_reversed = reduce(reverse_str, string)
print(the_reversed)

# 14. **Merge dictionaries**: Write a function that takes a list of dictionaries and 
# merges them into a single dictionary.

ls_of_dict = [{'a':'apple', 'b':'ball'}, {'c':'cat','d':'dog'}, {'e':'elephant'}]
# lis = []
# for i in ls_of_dict:
#     lis.append(i)
# print(lis)

def merge_of_dict(x,y):
    x.update(y)
    return x

dict_merged = reduce(merge_of_dict, ls_of_dict)
print(dict_merged)


# 13. **Check if any element in a list is True**: Write a function that takes a list of boolean values
# and returns True if any of the elements are True, otherwise False.

lst_of_bools = [True, False, False,True,True,True,False]

def check_true(x,y):
    return x or y

result = reduce(check_true, lst_of_bools)
print(result)

# 12. **Check if all elements in a list are True**: Write a function that takes a list of boolean values and returns True
# if all the elements are True, otherwise False.

lst_of_bools = [True, False, False,True,True,True,False]

def check_true(x,y):
    return x and y

result = reduce(check_true, lst_of_bools)
print(result)

# 10. **Flatten a list of lists**: Write a function that takes a list of lists and returns a single list 
# by flattening all the sublists.

ls_of_ls = [[2,3,5],[4,5,6],[7,5,1],[4,3]]

def flat_of_list(x,y):
    return x+y


flatten_list = reduce(flat_of_list, ls_of_ls)
print(flatten_list)


# 11. **Calculate average of numbers**: Write a function that takes a list of numbers 
# and returns the average of those numbers.

ls = list(range(1,6))

def calc(emp_ls, y):
    emp_ls.append(emp_ls[-1]+y)   
    return emp_ls

l = reduce(calc, ls[1:], [ls[0]])   # here third argu is initialization(it is a list )with first ele 
# in above line initial val(it is list end having 0 indx ele) is given and list start with 1 index

average = sum(l)/len(ls)
print(average)



