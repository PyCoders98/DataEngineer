# ////////////////////////////  Indentation //////////////////////////////

# ............................. conditional statement  ...................................................

# every block of statement will take four spaces
# 4 spaces

age = 17

if age>17:
  print('This park is for adults')  # provide four space manually
  print('you are not allowed')
else:
  print('This game is for children')  # provide four space manually

# Line Break

def add(arg1, arg2,
        arg3, arg4):
    pass

num = 13

if (num>6 and
    num<17):
  pass

# hanging indent(first line of parameter is blank)

def myfun(
    arg1, arg2,
    arg3, arg4):
  pass

result1 = myfun(1, 2,
                3, 4)   # aligning vertically

result2 = myfun(
              'a', 'b',
              'c', 'd')   # hanging intent( first line of parameter is empty)


# ///////////////////////////////// code lay out  //////////////////////////////
 
# 1 . Two Blank lines

# if you are having multiple classes or functions in a code file use two blank lines

class Parent:
  print('this is parent class')


class Child:
  print('this is child class')


def add(x, y):
  sum = x+y
  # a single line blank here
  return x+y

## 2 .single blank line 
# multiple methods in a class should have one line blank

class Parent:
  class_var = 3
                  # single line space
  def method_1():
    pass
                  # single line space
  def method_2():
    pass

## //////////////////////////////// comments /////////////////////////////////

# 1 . Block comments

for x in range(0, 10):
  # 4 space indentation s required to block comment 
  # it will loop for 10 times
  # used for looping
  print(x)

# 2 . Inline comments

age = 12  # this is inline comment showing age
name = 'virat kohli'  # this is also inline comments showing cricketer name

# 3 . Documentation comments - ( enclosed inside '''''')

# ///////////////////////////// naming Conventions /////////////////////////////////////

