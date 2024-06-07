# 1. **Square numbers from 1 to 5 and store them in a dictionary**:
#    Write a dictionary comprehension to generate a dictionary where
# keys are numbers from 1 to 5, and values are the squares of those numbers.

square = {k:k**2 for k in range(1,6)}
print(square)

# 2. **Convert a list of tuples into a dictionary**:
#    Given a list of tuples where each tuple contains a key-value pair, 
# write a dictionary comprehension to convert the list into a dictionary.

ls_of_tup = [("a",2),(10,100),('name','bestpeers')]
mydict = {k:v for k,v in ls_of_tup}
print(mydict)

# 3. **Count the frequency of characters in a string**:
# Given a string, write a dictionary comprehension to count the 
# frequency of each character in the string.

mystr = 'lasldjgfkjfjdsjhds'

the_dict = {k:mystr.count(k) for k in mystr}
print(the_dict)


# 4. **Convert keys to uppercase in a dictionary**:
#    Given a dictionary with lowercase keys, write a dictionary comprehension to convert 
# all keys to uppercase.

dict_lower  ={'fruit':'banana', ' flower':'tulip'}

upper_key_dict = {k:k.upper() for k in dict_lower.keys()}
print(upper_key_dict)

# 5. **Swap keys and values in a dictionary**:
#    Given a dictionary, write a dictionary comprehension to swap keys and values.
dict_to_swap ={'fruit':'banana', ' flower':'tulip'}

swapped_dict = {v:k for k,v in dict_to_swap.items()}
print(swapped_dict)