class A:
    def m1(self):
        print("Hello")
        
class B:
    def m2(self):
        print("Hi")
        
class C(A, B):
    def m3(self):
        print("Bye")
        
c = C()
c.m1()
c.m2()
c.m3()
