class Shape:
    def __init__(self):
        pass
    def area(self):
        return 0
class Square(Shape):
    def __init__(self, length):
        super().__init__()
        self.length = length
    def area(self):
        print(self.length ** 2)
shape = Shape()
shape.area()
square = Square(int(input()))
square.area()