class String:
    def getstring(self):
        self.sentence=input("Enter a string:")
    def printstring(self):
        print(self.sentence.upper())
        
mystring=String()
mystring.getstring()
mystring.printstring()
