class string:
    def __init__(self):
        self.string = ''
    def getString(self):
        self.string = input()
    def printString(self):
        print(self.string.upper())
s = string()
s.getString()
s.printString()