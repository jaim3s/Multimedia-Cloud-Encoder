class A:
    def __init__(self, *args):
        self.args = args

class B:
    def __init__(self, *args):
        print(type(args))
        self.args = args

a = A(1,2,3,4)
b = B(*a.args)
print(b.args)