# .............................. filter ........................

# 1. **Filter even numbers**: Write a function that takes a list of numbers and returns 
# a new list containing only the even numbers.

num = list(range(10))

def filter_even(x):
  if x%2 == 0:
      return True
  else:
      return False
  
even_num = list(filter(filter_even, num))
print(even_num)



# 2. **Filter odd numbers**: Write a function that takes a list of numbers and returns a new list 
# containing only the odd numbers.

num = list(range(10))

def filter_odd(x):
  if x%2 != 0:
      return True
  else:
      return False
  
even_num = list(filter(filter_odd, num))
print(even_num)



# 3. **Filter positive numbers**: Write a function that takes a list of numbers and returns a 
# new list containing only the positive numbers.

list_of_num = [1,4,6,-3,-5,9,0]

def fiter_pos(x):
   if x >= 0:
      return True
   else:
      return False

pos = list(filter(fiter_pos, list_of_num))
print(pos)

# 
# 4. **Filter negative numbers**: Write a function that takes a list of numbers and returns
# a new list containing only the negative numbers.


list_of_num = [1,4,6,-3,-5,9,0]

def fiter_neg(x):
   if x < 0:
      return True
   else:
      return False

neg = list(filter(fiter_neg, list_of_num))
print(neg)

# 5. **Filter prime numbers**: Write a function that takes a list of numbers and returns a new list 
# containing only the prime numbers.


# 6. **Filter strings by length**: Write a function that takes a list of strings and a length threshold, and returns a new list containing only the
# strings that are longer than the threshold.

mystring = ['papaya', 'banana','appy']

def my_func(x, thresh):
  return  len(x) > thresh
    
a = list(filter(lambda  ele: my_func(ele, 4) , mystring))
print(a)

#7. **Filter palindromes**: Write a function that takes a list of strings and returns a new list containing only 
# the palindromic strings.

ls = ['abba','aplle','best','apnnpa', 'malayalam']

def filter_palin(x):
   if x[::-1] == x:
      return x
   
palindrome = list(filter(filter_palin, ls))
print(palindrome)

# #
# 8. **Filter uppercase strings**: Write a function that takes a list of strings and 
# returns a new list containing only the strings that are entirely in uppercase.

ls_of_str = ['hello', 'APPLE','yes', 'NO','HI']

def filter_upper(x):
   if x.isupper():
      return True
   else:
      return False
   
upper_word = list(filter(filter_upper, ls_of_str))
print(upper_word)

# 9. **Filter lowercase strings**: Write a function that takes a list of strings and returns a new list 
# containing only the strings that are entirely in lowercase.


ls_of_str = ['hello', 'APPLE','yes', 'NO','HI']

def filter_lower(x):
   if x.islower():
      return True
   else:
      return False
   
lower_word = list(filter(filter_lower, ls_of_str))
print(lower_word)

# 11. **Filter strings containing only digits**: Write a function that takes a list of strings and returns a new list containing only the strings 
# that consist of digits only.

ls = ['apple','123','hi','hello','78565']

def digit_str(x):
  if x.isdigit():
   return True
  
dig_list = list(filter(digit_str, ls))
print(dig_list)
      
# 12. **Filter strings containing vowels**: Write a function that takes a list of strings and returns a new list containing only
# the strings that contain at least one vowel.


# ls_of_str = ['hello', 'APPLE','yes', 'NO','HI']
# vowels = ['a','e','i','o','u','A','E','I','O','U']

# 14. **Filter lists by sum**: Write a function that takes a list of lists of numbers and a threshold, and returns a new list
# containing only the lists whose sum exceeds the threshold.

ls_of_ls = [[2,3,4],[1,4,5],[7,2,1]]

def my_func(x, thresh):
  return  sum(x) > thresh
    
a = list(filter(lambda  ele: my_func(ele, 9) , ls_of_ls))
print(a)


# 15. **Filter lists by average**: Write a function that takes a list of lists of numbers 
# and an average threshold, and returns a new list containing only the lists whose average 
# exceeds the threshold.
ls_of_ls = [[2,3,4],[1,4,5],[7,2,1],[1,2] ,[1,2,34,5,7]]


def my_func(x, thresh):
  return  (sum(x)/len(x)) > thresh
    
a = list(filter(lambda  ele: my_func(ele, 3) , ls_of_ls))
print(a)


# 13. **Filter strings containing a specific substring**: Write a function that takes a list of 
# strings and a substring, and returns a new list containing only the strings that contain 
# the given substring.

string = ['elephant' , 'sparrow', 'peacock' , 'leopard']

def substring(string , sub):
   return sub in string

mylist = list(filter(lambda x : substring(x , 'le') , string))
print(mylist)

# 10. **Filter strings containing a specific character**: Write a function that takes a list of strings and a character, and returns a new list containing only the strings 
# that contain the given character.

string = ['elephant' , 'sparrow', 'peacock' , 'leopard']

def substring(string , char):
   return char in string

mylist = list(filter(lambda x : substring(x , 'e') , string))
print(mylist)