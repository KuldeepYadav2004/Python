class A:
    def m1(self):
        print("Hello")
class B(A):
     def m2(self):
         print("Hi")

class C:
    def m3(self):
        print("bye")

class D(B,C):
    def m4(self):
        print('welcome')
d=D()
d.m1()
d.m2()
d.m3()
d.m4()
