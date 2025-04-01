# mylist = [2,3,'g']
# print(type(mylist))

# myset = {2,5,'k'}
# print(type(myset))

# myset2 = set((2,6,'l'))
# print(type(myset2))

# myset3 = set([2,6,'l'])
# print(type(myset3))

# nested_lsit = [[1,2,3],[5,6,7]]
# print(type(nested_lsit))
# print(nested_lsit)

# print(nested_lsit[0])
# print(nested_lsit[0][0])

# list3d  = [[[3,4,6],[9,2,'h']]]
# print(list3d[0])

# print(list3d[0][0])

# print(list3d[0][0][0])

# thelist = [3,2,5,7,54,8,4,3,26,8]
# print(thelist[-2:3:-1])
# print(thelist[-1:-1:-1])
# print(thelist[-1:-1])
# print(thelist[0:-1])

# #  appending in a list
# list4 = [3,5,2,6]
# list4.append(8)
# print(list4)

# list4.append(('f',1))
# print(list4)

# list4.append(['d','r'])
# print(list4)

# list4.append({'d':'r'})
# print(list4)

# list4.append({0,'j'})
# print(list4)

# list4.append(set((4,'p')))
# print(list4)

# # extend in list

# list4.extend([10,20,30])
# print(list4)


# list4.extend((10,20,30))
# print(list4)


# list4.extend({'A':20})
# print(list4)


# list4.extend({10,20})
# print(list4)

# # remove function()
# print('remove age 22.............')
# age = [22,34,23,12,22,5]
# age.remove(22)
# print(age)

# print('removing all occured 22')

# for i in age:
#   if i == 22:
#     age.remove(i)
#     print('the age now:',age)
#   print('let see the age now:',age)
#   # but the above code skips the elements in checking ...... hence list comprehensions is the best way
# # you can understand these issue here

# print('the isue of skipping of elements')

# age = [22,34,23,12,22,22]

# for i in age:
#   if i == 22:
#     age.remove(i)
#     print('the age now:',age)
#   print('let see the issued age now:',age)




# # print('age after removing some age:' ,newage)

# # reverse and reversed function 
# reverselist = [4,3,6,5]
# print(reverselist)

# reverselist.reverse()
# print(reverselist)


# # reversefun

# lis = ['d',9,4,'o']
# print(lis)

# reversed_iterator = reversed(lis)
# print(reversed_iterator)

# print(next(reversed_iterator))
# print(next(reversed_iterator))
# print(next(reversed_iterator))
# print(next(reversed_iterator))

# # we can cnvert reverse iterator in list
# iterator_into_list = list(reversed(lis))
# print(iterator_into_list)

# # program to change first and last element 

# mylis = [3,2,67,8,5,4]
# def change_el():
#   mylis[0],mylis[-1] = mylis[-1] , mylis[0]

# change_el()
# print(mylis)

# # sum function 

# tosum = [1,2,2,5,15]
# add = sum(tosum)
# print(add)

# ## program to find min and max of two numbers

# a = 30
# b = 20

# if a>b:
#   print('a is maximum')

# # using function 
# def maxi(a,b):
#   if a > b:
#     return a
#   else:
#     return b
  
# maximum = maxi(2,5)
# print(maximum)

# maximum_of_num = max(345646,54)
# print(maximum_of_num)

# print(max([32,5,4,6,7]))
# print(max((32,5,4,6,7)))


# # ..................................some mathematical operations
# ## concatenation of lists 

# list1 = [32,33,34,35]
# list2 = [2,3,4,5]
# print('concatenated list:',list1+list2)

# list1.extend(list2)
# print('extended list :',list1)

# ##  ...............................nesting of list...........

# list1 = [32,33,34,35]
# list2 = [2,3,4,5]
# list3 = [list1,list2]
# print('the nested list:' ,list3)
# #..............................adding two lists  correspondings elements

# print('adding')

# list1 = [1,3,4,5]
# list2 = [2,3,4,5]
# added_list = []

# for i in range(len(list1)):
#   added_list.append(list1[i]+list2[i])

# print(added_list)

# # another approach to add corresponding elemnets of lists

# for i in zip(list1 , list2):
#   print(i)

# print('using zipping')
# for i,j in zip(list1 , list2):
#   print(i+j)

# ##  ......................................subtracting two lists  correspondings elements

# print('subtracting two lists  correspondings elements')
# for i,j in zip(list1 , list2):
#   print(i-j)


# ## ..........................................multi 

# print('multi two lists  correspondings elements')
# for i,j in zip(list1 , list2):
#   print(i*j)


# company = ['Bestpeers']
# company = ['Bestpeers']*3
# office = ['A','B']*3

# print(company)
# print(office)

# ##..........................................divide

# print('dividing two lists  correspondings elements')
# for i,j in zip(list1 , list2):
#   print(i/j)


# ## different ways of ceating list
# # by tuple
# # by dict
# # by set

# dict1 = {'a':1,'B':2,'c':3}
# print(list(dict1))

# ###...............................................  list programms  ................

# # sum of elements of list 

# mylist = [3,4,4,2]

# sum = 0
# for i in mylist:
#   sum = sum+i
#   print('each sum :',sum)
# print('total sum :',sum)

# ## maximum elements

# thelist = [2,44,15,7,5,7,4,426,6]

# max_ele = thelist[0]

# for ele in thelist[1:]:
#   if ele > max_ele :
#     max_ele = ele
# print(max_ele)

# ## minimum elements

# thelist = [2,44,15,7,5,7,4,426,6]

# min_ele = thelist[0]

# for i in thelist[1:]:
#   if i < min_ele:
#     min_ele = i
# print(min_ele)

# ###  oops concept practice

# ## finding average of all elements of a list

# thelist = [2,44,15,7,5,7,4,426,6]
# def average_of_list(lis):
#   average = (len(thelist))/2
#   return average

# average_is = average_of_list(thelist)
# print(average_is)


# ## count ooccurences of specific elements
# thelist = [2,44,15,7,5,7,4,426,6]
# ele = 7
# count = 0
# for i in thelist:
#   if i == ele:
#     count = count+1
# print(count)

# ## reverse a list
# thelist = [2,44,15,7,5,7,4,426,6]
# # print(thelist[-1:-1:-1])
 
# reversed_list = []
# for i in range(len(thelist)-1,-1,-1):
#   reversed_list.append(thelist[i])

# print(reversed_list)


# ## removing duplicates
# thelist = [2,44,15,7,5,7,4,426,6]
# removing_dupli = set(thelist)
# print(removing_dupli)

# ## by using methods
# for i in thelist:
#   if thelist.count(i) > 1:
#     thelist.remove(i)
# print(thelist)


# ## by using dictionary
# lis = [22,1,54,4,6,4,32,3,4,5,7]
# mydict = {}

# for i in lis:
#   if i not in mydict:
#     mydict[i] = 1
#   else:
#     mydict[i] = mydict[i] +1
# print(mydict)

# # ##  sorting a list

# lis = [22, 1, 54, 4, 6, 4, 32, 3, 4, 5, 7]

# for i in range(len(lis)):
#     for j in range(i + 1, len(lis)):  # Start from i + 1 to avoid unnecessary comparisons
#         if lis[i] > lis[j]:
#             temp = lis[i]
#             lis[i] = lis[j]
#             lis[j] = temp  # Swap the elements

# print(lis)

# ## search ele and retuen its index
# ls1 = [12,45,35,6]
# for i in ls1:
#   if i == 45:
#     a = ls1.index(i)

# print(a)


# ## list slicing

# ls2 = [11,22,33,44,55,66,77,88]
# print(ls2[4:6])
# # print(ls2)

# print(ls2[4:6+1])
# print(range(len(ls2[4:6+1])))

# sliced = []
# def slicing(lis , st , end):
#   # sliced = []
#   for i in range(len(lis[st:end+1])):
#     sliced.append(lis[i])
#   return sliced

# a= slicing(ls2 , 1,3)
# print(a)

# ## converting list to tuple

# # lis= [1,2,3,4]
# # tup = ()
# # print(tup)

# def list_to_tuple(lst):
#     new_tuple = ()  # Initialize an empty tuple
#     for element in lst:
#         new_tuple += (element,)  # Add each element of the list to the tuple
#     return new_tuple

# # Example list
# my_list = [10, 20, 30, 40, 50]

# # Convert the list to a tuple
# my_tuple = list_to_tuple(my_list)

# # Printing the original list and the converted tuple
# print("Original list:", my_list)
# print("Converted tuple:", my_tuple)


# # toyota company -- class
# # speed 
# # mileage
# # year
# # color

# # objects = fortuner

# class Toyota():

#   def __init__(self ,speed , mileage , year , color):
#     self.speed = speed
#     self.mileage = mileage
#     self.year = year
#     self.color  = color

#   def blueprint(self):
#     print('the car blueprint is ready')

# obj  = Toyota(200 , 95 , 2000 , 'red')
# print(obj.speed)
# print(obj.mileage)
# print(obj.year)
# print(obj.color)
# obj.blueprint()





# class Toyota():

#   def __init__(self ,speed , mileage , year , color):
#     self.speed = speed
#     self.mileage = mileage
#     self.year = year
#     self.color  = color
#     self.isrunning = False


#   def start(self):
#     if self.isrunning == True:
#       print(f'the car with {self.speed} is running')
#     else:
#       print('the car with {} is not running'.format(self.speed))

# fortuner = Toyota(100,200,2022,['red','blue'])
# fortuner.start()
# print(fortuner.speed)
# print(fortuner.color)
# print(fortuner.mileage)

# suv = Toyota(300,150,2024,['black','grey' , 'orange' , 'teal'])
# print(suv.color)
# suv.start()

# ##  ............................................................................creating simple class
# class Student():

#   def __init__(self,name ,standard , blood_g , age , height):
#     self.name = name
#     self.standard = standard
#     self.blood_g = blood_g
#     self.age = age
#     self.height  = height

#   def is_playable(self):
#     if self.age > 12:
#       print('yes the student age is {} so he is playable'.format(self.age))
#     else:
#       print(f'the student age is {self.age} so he is not playable')

#   def consider_tall(self):
#     if self.height >= 5:
#       print(f'yes , since height of {self.name} is {self.height}, hence he considered to be tall')
#     else:
#       print('he is not tall')

# first_stu = Student('A','10th','o',14,5)
# print(first_stu.name)
# print(first_stu.standard)
# print(first_stu.blood_g)
# print(first_stu.age)
# print(first_stu.height)
# first_stu.is_playable()
# first_stu.consider_tall()

# sec_stu = Student('B',11,'b',11,4.5)
# sec_stu.is_playable()
# sec_stu.consider_tall()

# ### ..............................................................................................

# ##..............................................................................................
# class Student():

#   def __init__(self,name ,id):
#     self.name = name
#     self.id = id
#     self.courses = []

#   def course_det(self , course):
#     self.courses.append(course)

# stu1 = Student('a',101)
# print(stu1.name)
# print(stu1.id)
# stu1.course_det(['DBMS' ,'DS', 'PYTHON' ])
# print(stu1.courses)

# ## .............................................................................................
# print('lets unleash object oriented')

# class Student():

#   def __init__(self,name,id):
#     self.name = name
#     self.id = id
#     self.courses = []

#   def enroll_courses(self,course) :
#     self.courses.append(course)

#   def display_info(self):
#     return f"Student ID: {self.id}, Name: {self.name}"

# class Course(): 

#   def __init__ (self , c_id,c_name):
#     self.c_id = c_id
#     self.c_name = c_name

#   def display_info(self):
#         print(f"Course ID: {self.c_id}, Name: {self.c_name}")

# # student objects
# stu = Student('aaaa',11)
# # print(stu.name)
# # print(stu.id)

# course1 = Course(1111,'dbms')
# # course1.display_info()

# stu.enroll_courses(course1)
# print(stu.display_info())





# # class Student:
# #     def __init__(self, student_id, name, age):
# #         self.student_id = student_id
# #         self.name = name
# #         self.age = age
# #         self.courses = []  # List to store enrolled courses

# #     def enroll_course(self, course):
# #         self.courses.append(course)

# #     def display_info(self):
# #         return f"Student ID: {self.student_id}, Name: {self.name}, Age: {self.age}"

# # class Course:
# #     def __init__(self, course_id, name, credits):
# #         self.course_id = course_id
# #         self.name = name
# #         self.credits = credits

# #     def display_info(self):
# #         return f"Course ID: {self.course_id}, Name: {self.name}, Credits: {self.credits}"

# # # Create student objects
# # student1 = Student(1, "Alice", 20)
# # student2 = Student(2, "Bob", 21)

# # # Create course objects
# # course1 = Course(101, "Mathematics", 3)
# # course2 = Course(102, "Physics", 4)

# # # Enroll students in courses
# # student1.enroll_course(course1)
# # student1.enroll_course(course2)
# # student2.enroll_course(course2)

# # # Display student and course information
# # print(student1.display_info())
# # for course in student1.courses:
# #     print("Enrolled in:", course.display_info())

# # print(student2.display_info())
# # for course in student2.courses:
# #     print("Enrolled in:", course.display_info())

# ###########################################################
# class Employee():

#   def __init__(self,name,age,salary):
#     self.name = name
#     self.age = age
#     self.salary = salary
#     self.is_employee = True

#   def is_working(self):
#     if self.is_employee == True:
#       print(f'yes the employee {self.name} is working')

# obj = Employee('aajay',27,30000)
# print(obj.name)
# print(obj.age)
# print(obj.salary)
# obj.is_working()

# ## reverse
# ls = [2,3,4,46,4]
# print(ls[::-1])
# print(range(len(ls)-1,-1,-1))

# word = 'heleh'
# ls = list(word)
# print(ls)
# reverse = ''

# # for i in range(len(ls)-1,-1,-1):
# #   print(ls[i])

# # def fun():
# #   for i in range(1000):
# #     yield i

# # ls_of_1000 = fun()
# # print(next(ls_of_1000))
# # print(next(ls_of_1000))
# # print(next(ls_of_1000))
# # print(next(ls_of_1000))
# # print(next(ls_of_1000))


# #################################################################################

# # .........................................list 3 june.....................................
# ls = [2,4]
# ls.append(5)
# print(ls)

# ls.append([2,3,4,5,6,7,8,9,0])
# print(ls)

# ls.append({'A':8})
# print(ls)

# ls.append({3,7})
# print(ls)

# ##################### extend somehow works as concatenate
# ls.extend('y')
# print(ls)

# ls.extend([6,5])
# print(ls)

# ls.extend({'G':'grapes'})
# print(ls)

# ###################...........................concatenate
# print('now lets concatenate')
# l1 = [1,2]
# l2 = [3,4]
# # l3 = l1+l2
# # print(l3)

# print(l1+l2)

# ##########################  this is adding of two lists
# for i,j in zip(l1,l2):
#   print(i+j)

# ######################  insert

# lis = [1,2,6,7,5,6,4,6,65,3]
# lis.insert(2,'hello')
# print(lis)

# ####################  index
# a = lis.index('hello')
# print(a)

# the_lis = ['a',7,3,4,5,3,4,'a','b','a']
# b = the_lis.index(3,4)
# print(b)

# print(the_lis.clear())

# ######################  sort

# ls = [23,4,6,7,5,5,4]
# ls.sort()
# print(ls)



## //////////////////////////////////////////////////////////////////////
# simple assignment , shallow copy , deep copy
#  ......... Simple assignment in Python never copies data. ..................

lis1 = [2,3,4]
lis2 = lis1         ## here lis2 has new reference only and pointing to the same list object
print(id(lis1))
print(id(lis2))
##  ..they both have same id ie (they refer to the same object).(same memory location) 
lis2[2] = 'hi'
print(lis2)
print(lis1)
# ............  shallow copy ..........................

# here a new list object is created and pointing to the same original list
# 1...................
lis3 = ['a','c']
lis4  =lis3.copy()
print(lis3)
print('the shallow copy is :' ,lis4)
print('the id of shallow copy lis4 is :',id(lis3))
print('the id of shallow copy lis4 is :',id(lis4))
# 2..........................
ls  =[1,2,3,[4,5]]
ls_copy = ls.copy()

ls_copy[2] = 'hi'
print(ls_copy)
print(ls)


# lis4[1] = 'hello'
# print(lis4)
# print(lis3)


#  slicing is  also a shallow copy 

mylist = [2,3,4]
mylist_slice = mylist[:]
print(mylist_slice)
print(id(mylist))
print(id(mylist_slice))

mylist_slice[1] = 'hello'
print(mylist_slice)
print(mylist)


# ........... deep copy ..............................

# Fibonacci series:
# the sum of two elements defines the next
a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

tup1 = (2,3,4)
tup2 = (5,3,7)

tup3 = tup1+tup2
print(tup3)

tup4 = (tup1,tup2)
print(tup4)

tup5 = zip(tup1 , tup2)
print(tup5)

print(next(tup5))
print(next(tup5))
print(next(tup5))

ls4= [1,2] 
ls5 = [5,6]
ls6 = zip(ls4 , ls5)

print(next(ls6))
print(next(ls6))