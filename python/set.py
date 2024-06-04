myset = set((2,44,64,7))
print(myset)

myset.add(99)
print(myset)

myset.remove(99)   
print(myset)

# myset.remove(3446)   ## if element doesnt exists it doesnt throw error
# print(myset)

myset.discard(4567)  ## if element doesnt exists it doesnt throw error

myset.update(['hi' ,'hello'])
print(myset)

myset.update((100 ,200))
print(myset)

# myset.update(90000)   ## it throws error since update takes only iterable
# print(myset)

popped_item = myset.pop()
print('throw popped item :',popped_item)
print('remaining set:',myset)

myset.clear()
print(myset)

my_set1 = {1, 2, 3, 4, 5}
removed_element = my_set1.pop()  # Removes and returns an arbitrary element
print(removed_element)  # Output will vary, as it depends on the specific set contents                                                   

my_set2 = {}
popped_ele = my_set2.pop()
print(popped_ele)
