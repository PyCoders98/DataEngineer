# list comprehensions

# its a concise way to create a list , where each ele in created list is the result of 
# some operation applied on ele of another iterable

# Que . make a list where ele are the square of ele of a list ..
mylist = [1,2,3,4]
squares = [x**2 for x in mylist]
print(squares)

# Que .Filtering odd numbers from a list

num_list = [11,2,4,32,5,6,7,8,4]

odd_list = [x for x in num_list if x%2 != 0]
print(odd_list)

# Que .Generate a list of characters from a string

mystring = 'hello'

list_of_char = [letter for letter in mystring]
print(list_of_char)

# Que. Create a list of lengths of words in a sentence

sent = 'This is absolutely amazing'

len_of_words = [len(word) for word in sent.split(' ')]
print(len_of_words)

# Que.  Generate a list of tuples containing a number and its square

list_of_tup = [(x, x**2) for x in range(2,6)]
print(list_of_tup)

# Que. 
list1 = [1,2,3]
list2 = [4,5,6]

mylist = [(x,y) for x,y in zip(list1, list2)]
print(mylist)

# for x,y in zip(list1, list2):
#   print(x,y)

# Que .Create a list of lowercase letters

str = 'abcDefGhiJK'
letters = [letter.lower() for letter in str ]
print(letters)

# Que .convert lower letter to upper and upper to lower

str1 = 'mnDgsjEJyAjisAF'

conversion = [letter.upper() if letter.islower() else letter.lower() for letter in str1 ]
print(conversion)

# or 

the_list = ['apple', 'banana', 'cherry', 'date']

swap_word = [x.swapcase() for x in the_list ]
print(swap_word)

# Que  Nested if.

numbers = [3, 8, 4, 9, 10, 6, 7]

new_list = [(x) for x in numbers if x > 5 if x % 2 == 0 ]
print(new_list)

# Que .. Generate a list of common multiples of 3 and 5 up to 100

multiples = [x for x in range(1,100)  if x%3 == 0 and x%5 == 0]
print(multiples)

# Que .Create a list of reversed strings from another list
list1 = ['a', 'b' ,'c' ,'d']

reversed_list = [list1[i] for i in range(len(list1)-1, -1, -1)]
print(reversed_list)

# Que .Create a list of characters that are not vowels from a string
my_str = 'hellohithere'
vowels = ['a','e','i','o','u']

list_not_vow = [x for x in my_str if x not in vowels]
print(list_not_vow)

# Que .List of words with their first and last letter swapped

word_list = ['apple', 'banana', 'cherry', 'date']

swap_list = [(x[-1]+ x[1:-1]+x[0]) for x in word_list]
print(swap_list)

