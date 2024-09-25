class shape:
    def __init__(self):
        pass
    def area(self):
        return 0
class square(shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    def area(self):
        print(self.length ** 2)
class rectangle(shape):
    def __init__(self, length, width):
        super().__init__()
        self.length = length
        self.width = width
    def area(self):
        print(self.length * self.width)
shape = shape()
len = int(input())
wdth = int(input())
rec = rectangle(len, wdth)
rec.area()