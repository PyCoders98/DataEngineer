# Single level inheritance
class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def f1(self):
        print("name : ", self.name)
        print("age : ", self.age)


class B(A):
    def __init__(self, name, age):
        super().__init__(name, age)


obj = B("Aman", 23)
obj.f1()


# Mutiple Inheritance
print()


class A:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def f1(self):
        print("name : ", self.name)
        print("age : ", self.age)


class B:
    def f2(self):
        print("class B")


class C(A, B):
    def __init__(self, name, age):
        super().__init__(name, age)


obj = C("Aman", 23)
obj.f1()
obj.f2()


# Multilevel inheritance
print()
class A:
    def f1(self):
        a = "Hello "
        return a 
class B(A):
    def f2(self):
        b="How "
        return b
class C(B):
    def f3(self):
        c="Are "
        return c
class D(C):
    def f4(self):
        d="You."
        return d
obj=D()
print(D.mro())
print(obj.f1(),obj.f2(),obj.f3(),obj.f4())

# MRO: Method Resolution Order 
class A:
    def msg(self):
        print("Class A")
class B:
    def msg(self):
        print("Class B")
class C(A,B):
    pass
class C(B,A):
    pass

obj=C()

obj.msg()
print(C.mro())
