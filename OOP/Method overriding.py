class A:
    def m(self):
        print("hello")
class B(A):
    def m(self):
        print("Hi")
x=A()
x.m()
x=B()
x.m()
