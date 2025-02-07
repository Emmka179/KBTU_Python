class Strings:
    def getString(self):
        self.text = input("Enter a string: ")

    def printString(self):
        print(self.text.upper())

s = Strings()
s.getString()
s.printString()