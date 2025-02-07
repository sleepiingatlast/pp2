class str_oper:
    def getString(self):
        self.ex = input("введите строку: ")
    
    def printString(self):
        print(self.ex.upper())
        
class_using = str_oper()
class_using.getString()
class_using.printString()
        