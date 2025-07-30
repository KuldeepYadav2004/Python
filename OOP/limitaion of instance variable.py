class person:
    def __init__(self):
        self.count =0
        self.count +=1
    def print_objects_count(self):
        print('number of objects created:',self.count)

p1=person()
p1.print_objects_count()
p2=person()
p2.print_objects_count()
