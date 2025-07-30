class person:
    count=0 #class variable
    def __init__(self):
        person.count +=1
    @classmethod
    def print_objects_count(cls):
        print('number of objects created:',cls.count)

person.print_objects_count()



p1=person()
p1.print_objects_count()
p2=person()
p1.print_objects_count()
p2.print_objects_count()



