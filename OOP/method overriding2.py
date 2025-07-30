class Square:
    def __init__(self,side):
        self.side=side
    def find_area(self):
        self.area=self.side**2
        print("Area of square:",self.area)
class Cube(Square):
    def __init__(self, side):
        super().__init__(side)
    def find_area(self):
        self.area=6*self.side**2
        print("Area of cube:",self.area)

s=Square(4)
s.find_area()
s=Cube(5)
s.find_area()


        