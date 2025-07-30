class A:
    def __init__(self):
        print("hi")
    
    def __del__(self):
        print("bye")


a1=A()
a2=A()
del a1
del a2

