class A:
    def m(self):
        print("Hello")
    
class B:
    def m(self):
        print("Hi")

class C(A,B):
    def m2(self):
        self.m()
        B.m(self)
c=C()
c.m2()




