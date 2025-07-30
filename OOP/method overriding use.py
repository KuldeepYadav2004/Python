class Square:
    def __init__(self,side):
        self.side=side
    def get_area(self):
        self.area=self.side**2
        return "Area of square:" + str(self.area)
    
class Cube(Square):
    def __init__(self, side):
        super().__init__(side)
    def get_area(self):
        self.area=6*self.side**2
        return "Area of cube:" + str(self.area)
    

shapes = [Square(int(input("Enter side of square:"))),Cube(int(input("Enter side of cube:")))]
for s in shapes:
    print(s.get_area())



        