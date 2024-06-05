l1=[1,232,12,34,2,55,32,89,56,53423,4,31,23,12,8,23,212,67,90,32,111]
l2=[43,32,2321,56,675,634,532,1,22,123,32,54,76,8,9,67,54,2343,123,21,32,356,5467,8,7]

def Append_an_element_to_the_first_list(l1):
    element = int(input("Enter element you want to append : "))
    print("Before appending : ",l1)
    l1.append( element )
    print("After appending : ",l1)
    
def Extend_the_first_list_by_the_second_list(l1,l2):
    print(f" Before Extending \n List 1 : {l1} \n List 2 : {l2}")
    l1.extend(l2)
    print(f" After Extending : {l1}")
    
def Insert_an_element_at_a_specific_index_in_the_first_list(l1):
    pos = int(input("Enter position : "))
    element=int(input("Enter element : "))
    print("Before  inserting : ",l1)
    l1.insert(pos,element)
    print("After  inserting : ",l1)

def Remove_an_element_from_the_first_list(l1):
    element = int(input("Enter element you want to remove : "))
    print("Before Removing : ",l1)
    l1.remove(element)
    print("After Removing : ",l1)
    
def Pop_the_last_element_from_the_first_list(l1):
    print( "Before Popping : ",l1)
    l1.pop()
    print( "After Popping : ",l1)

def Clear_the_second_list(l2):
    print("Before Clearing : ",l2)
    l2.clear()
    print("After  Clearing : ",l2)

def Find_the_index_of_a_specific_element_in_the_first_list(l1):
    print(l1)
    index = int(input("Enter element you want to find the of : "))
    print("Index of element is : ",l1.index(index))
    
def Count_the_occurrences_of_a_specific_element_in_the_first_list(l1):
    print(l1)
    element = int(input("Enter you want to count the occurrences : "))
    print( "Number of occurrences of element is : ",l1.count(element))

def Sort_the_first_list_in_ascending_order(l1):
    print("Before Sorting : ",l1)
    l1.sort(reverse=False)
    print("After Sorting : ",l1)
    
def Reverse_the_first_list(l1):
    print("Before Reversing : ",l1)
    l1.reverse()
    print("After reversing : ",l1)    

def list_operations(l1,l2):
    while(True):
        print("1. Append an element to the first list.\n2. Extend the first list by the second list.\n3. Insert an element at a specific index in the first list.\n4. Remove an element from the first list.\n5. Pop the last element from the first list.\n6. Clear the second list.\n7. Find the index of a specific element in the first list.\n8. Count the occurrences of a specific element in the first list.\n9. Sort the first list in ascending order.\n10. Reverse the first list.\n11 Break")
        no = int(input("Enter no to perform operation : "))
        if no==1:
            Append_an_element_to_the_first_list(l1)
        elif no==2:
            Extend_the_first_list_by_the_second_list(l1,l2) 
        elif no==3:
            Insert_an_element_at_a_specific_index_in_the_first_list(l1) 
        elif no==4: 
            Remove_an_element_from_the_first_list(l1) 
        elif no==5: 
            Pop_the_last_element_from_the_first_list(l1)
        elif no==6: 
            Clear_the_second_list( l2)
        elif no==7: 
            Find_the_index_of_a_specific_element_in_the_first_list(l1)
        elif no==8: 
            Count_the_occurrences_of_a_specific_element_in_the_first_list(l1)
        elif no==9: 
            Sort_the_first_list_in_ascending_order(l1)
        elif no==10: 
            Reverse_the_first_list(l1)
        else:
            break

list_operations(l1,l2)