class ComplexNumber:
    def __init__(self,real=0,imginary=0):
        self.real =real
        self.imginary=imginary
    
    def print_complex_number(self):
        print(self.real,"+",self.imginary,"i")

    def __add__(self,other):
        new=ComplexNumber()
        new.real=self.real + other.real
        new.imginary=self.imginary+other.imginary
        return new
c1=ComplexNumber(4,5)
c1.print_complex_number()
c2= ComplexNumber(3,4)
c2.print_complex_number()
c3=c1+c2
c3.print_complex_number()


    