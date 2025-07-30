class A:
    def m(self):
        print("Hello")
    
class B:
    def m(self):
        print("Hi")

class C(A,B):
    pass
c=C()
c.m()


