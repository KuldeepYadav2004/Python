from abc import ABC, abstractmethod

class Shape(ABC):
    def __init__(self):
        self.area= 0
    @abstractmethod
    def get_area(self):
        pass
class Square(Shape):
    def __init__(self,side):
        super().__init__()
        self.side = side
    def get_area(self):
        self.area = self.side**2
        return "Area of square:" + str(self.area)
class Rectangle(Shape):
    def __init__(self,length,breadth):
        super().__init__()
        self.length= length
        self.breadth=breadth
    def get_area(self):
        self.area=self.length*self.breadth
        return"Area of Rectangle:"+ str(self.area)
s=Square(int(input("Enter side of square:")))
print(s.get_area())
s=Rectangle(int(input("Enter the Length of rectangle:")),int(input("Enter the breadth of rectangle:")))
print(s.get_area())

