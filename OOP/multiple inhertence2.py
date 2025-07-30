class A:
    def m(self):
        print("Hello")
    
class B:
    def m(self):
        print("Hi")

class C(B,A):
    pass
c=C()
c.m()


