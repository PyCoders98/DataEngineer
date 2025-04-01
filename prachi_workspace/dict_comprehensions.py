# Dictionary comprehensions

# Que .1 create a dictionary of squares of numbers from 1 to 10

sq_dict = {k: k**2 for k in range(1,10)}
print(sq_dict)

# Que. Create a dictionary of even numbers as keys and their squares as values

even_dict = {k:k**2 for k in range(10) if k%2 == 0}
print(even_dict)

# Que . 3. Create a dictionary of words and their lengths from a sentence

my_string =  'Python is awesome'
# splitted = my_string.split()
# print(splitted)

# dict_result = { k:len(k) for k in splitted}
# print(dict_result)

dict_result = { k : len(k) for k in my_string.split()} 
print(dict_result)

# Ques 4 .....

new_string =  'Python is awesome , Python is easy , Python is amazing'
words = new_string.split(' ')
print(words)

my_dict = {k : words.count(k) for k in set(words)}
print(my_dict)

# Create a dictionary of lowercase characters from a string
the_str = 'HIDSGJDUEKD'

lower_dict = {k : k.lower() for k in the_str}
print(lower_dict)

# . Create a dictionary of numbers and their squares, excluding odd numbers

sq_dict = {k : k**2 for k in range(10) if k%2 != 0}
print(sq_dict)

# Create a dictionary of words with the letters sorted

word_list = ['apllesd', 'programming' , 'hello']

sort_dict = {word : ''.join(sorted(word)) for word in word_list}   # in string sort method is not there but using sorted() an iterator
                                                                  # will be created and here we joined that
print(sort_dict)


# Create a dictionary of words and their lengths, but only for words with more than 5 letters

fruits = ['apple', 'banana', 'cherry', 'date']

f_dict = {k : len(k) for k in fruits if len(k)>5}
print(f_dict)

#  Create a dictionary of numbers and their parity (even or odd)

parity = {k :('even' if k%2 == 0 else 'odd') for k in range(1,10)}
print(parity)

#  Create a dictionary of numbers and their squares, but only for multiples of 3

the_dict = {k : k**2 for k in range(10) if k%3 == 0}
print(the_dict)