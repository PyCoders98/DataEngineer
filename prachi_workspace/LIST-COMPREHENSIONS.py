
# 1. Write a list comprehension to generate the squares of numbers from 1 to 10.

sq_num = [x**2 for x in range(1,11)]
print(sq_num)

# 2. Given a list of numbers, write a list comprehension to extract only the even number from thelist.

even = [x for x in range(1,11) if x%2 == 0]
print(even)

# 3. **Convert Celsius temperatures to Fahrenheit**:
# Given a list of temperatures in Celsius, write a list comprehension to convert 
# each temperature to Fahrenheit using the formula: \( \text{F} = \frac{9}{5} \times \text{C} + 32 \).

celcius = [32,32, 26, 45]
cel_to_fehr = [((9/5)*x + 32) for x in celcius]
print(cel_to_fehr)

# 4. **Extract words longer than 5 characters from a sentence**:
# Given a sentence, write a list comprehension to extract only the words longer than 
# 5 characters.

fruits = ['Apricot', 'apple', 'Blackberry', 'Blueberry', 'Boysenberry']
words = [x for x in fruits if len(x) > 5]
print(words)


# 5. **Generate a list of tuples containing numbers and their squares**:
#    Write a list comprehension to generate a list of tuples where each tuple contains a number 
# and its square from 1 to 5.

square = [(x,x**2) for x in [2,5,34,6,7,9]]
print(square)