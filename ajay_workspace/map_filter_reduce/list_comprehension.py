# 1. **Generate squares of numbers from 1 to 10**:
#    Write a list comprehension to generate the squares of numbers from 1 to 10.
print([x**2 for x in range(1,11)])


# 2. **Extract even numbers from a given list**:
#   Given a list of numbers, write a list comprehension to extract only the even numbers from the list.
l=[i for i in range(2,50)]
print([i for i in l if i%2==0])

# 3. **Convert Celsius temperatures to Fahrenheit**:
#    Given a list of temperatures in Celsius, write a list comprehension to convert each temperature to 
# Fahrenheit using the formula: \( \text{F} = \frac{9}{5} \times \text{C} + 32 \).

l=[12,31,45,64,31,2,798,123,-40,-34,-12]
print([round((((x-32)*5)/9),2)   for x in l])

# 4. **Extract words longer than 5 characters from a sentence**:
#    Given a sentence, write a list comprehension to extract only the words longer than 5 characters.
l = ["apple", "banana", "orange", "grape", "kiwi"]
print([x for x in l if len(x)>5])

# 5. **Generate a list of tuples containing numbers and their squares**:
#    Write a list comprehension to generate a list of tuples where each tuple contains a number and its square from 1 to 5.
l=[i for i in range(1,6)]
print([(i,i**2) for i in l])
