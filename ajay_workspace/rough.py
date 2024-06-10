from functools import reduce

# # 5. **Calculate Cumulative Sum**: Write a function that takes a list of numbers and returns a new list where each element is the cumulative sum up to that point.
# l = [11, 22, 33, 44, 55, 66]
# l1 = [sum(l[0:x:1]) for x in range(0, len(l) + 1)]
# print(l1[1:])

# l = [
#     "hello",
#     "how",
#     "are",
#     "i",
#     "am",
#     "fine",
#     "what",
#     "about",
#     "you",
#     "nice",
#     "to",
#     "meet",
#     "you",
# ]

# print([x for x in l if len(x) > 3])

# # 9. **Count occurrences of a specific element in a list**: Write a function that takes a list of elements and a specific element,
# # and returns the count of occurrences of that element in the list.
# from functools import reduce

# # def count_occurrences(lst, element):
# #     return reduce(lambda count, x: count + (1 if x == element else 0), lst, 0)

# # # Example usage:
# # element_to_count = 2
# # occurrences = count_occurrences(my_list, element_to_count)
# # print("Number of occurrences of {}: {}".format(element_to_count, occurrences))

# my_list = [1, 2, 3, 4, 2, 2, 5, 2]
# element = 2
# print(reduce(lambda count, x: count + (1 if x == element else 0), my_list, 0))


# def even(limit):
#     num = 0
#     while num <= limit:
#         yield num
#         num += 2


# for n in even(10):
#     print(n)

# def fib(limit):
#     a,b=0,1
#     while a<limit:
#         yield a
#         a,b=b,a+b
# for i in fib(10):
#     print(i,end=",")
# def cumulative_sum(numbers):
    # Define a lambda function to calculate cumulative sum
    # cumulative_func = lambda x: sum(numbers[:x+1])
    # Use map to apply the cumulative function to each index
    # return list(map(cumulative_func, range(len(numbers))))

# Example usage:
# numbers = [10, 20, 30, 40, 50]
# result = cumulative_sum(numbers)
# print(result)  

# print(list(map(lambda x: sum(numbers[:x+1]), range(len(numbers)))))   

# l=[11,221,23,1,657,978,45]
# sum = reduce(lambda a,b:a+b,l)
# avg= len(l)
# print (round((sum/avg),2))
l = [
    {'a': 56, 'b': 2},
    {'c': 3},
    {'c':9},
    {'d': 4, 'e': 5}
]
print(reduce(lambda acc,d:{**acc,**d},l,{}))


