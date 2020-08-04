class A:

    def hello_world(self):
        print("Hello0000")

class B:
    def hello_world(self):
        print('hello world')

class C(A,B):
    pass

c = C()
c.hello_world()

print(C.mro())