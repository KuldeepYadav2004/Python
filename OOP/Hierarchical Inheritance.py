class A:
    def m1(self):
        print("Hello")
        
class B(A):
    def m2(self):
        print("Hi")
        
class C(A):
    def m3(self):
        print("Bye")
        
b = B()
b.m1()
b.m2()

c = C()
c.m1()
c.m3()
