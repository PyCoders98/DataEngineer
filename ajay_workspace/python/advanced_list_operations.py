# Rotate a list to the right by k steps.
l1=[1,2,3,4,5,6,7,8,9]
# k=int(input("Enter steps : "))
k=2
rotate = int(k%len(l1))
print(l1[-rotate:]+l1[:-rotate])


# Remove duplicates from a list while maintaining order.
l2=[12,21,34,32,55,21,2,3,5,12,23,2,4,77,55,12,89,98,9,12,2]
l3=[]
for i in l2:
    if i not in l3:
        l3.append(i)
print(l3)

# Find the intersection of two lists.
l4=[]
for i in l1:
    if i in l2:
        l4.append(i)
print(l4)


# Find the union of two lists.
l5=[]
for i in l1:
    if i not in l5:
        l5.append(i)
for j in l2:
    if j not in l5:
        l5.append(j)
print(l5)
