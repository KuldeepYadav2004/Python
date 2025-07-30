class A:
    def __del__(self):
        print('bye')
    def __init__(self):
        print('hi')
A()
A()
