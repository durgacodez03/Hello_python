## Single inheritance : When a child class inherits only one parent class it is called single inheritance"
class A:
    def hello(self):
        print("Hello world")

class B(A):
    pass

b = B()
b.hello()

## Multiple inheritance : When a child class inherits more than one parent class 

class A:
    def hello(self):
        print("Hello A")

class B:
    def hello(self):
        print("Hello B")

class C(B,A):
    print("Hello C")

c = C()
c.hello()

##Multilevel inheritance :

class A:
    def hello(self):
        print("Hello A")
    
class B(A):
    pass

class C(B):
    pass

c = C()
c.hello()

## Heirachy : When the parent class is used in different child class 

class A:
    def hello(self):
        print("Hello A")
class B(A):
    def hello(self):
        print("Hello B")

class C(A):
    pass

c = B()
c.hello()