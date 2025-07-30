from abc import ABC, abstractmethod

class A(ABC):
    def m1(self):
        print("Hello")

    @abstractmethod
    def m2(self):
        pass

class B(A):
    def m2(self):
        print("Hi")

    def m3(self):
        print("Bye")


b=B()
b.m1()
b.m2()
b.m3()


