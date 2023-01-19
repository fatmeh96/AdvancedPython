class Rectangle:
    def __int__(self,width,length):
        self.width=width
        self.length=length
    def area(self):
        return self.width*self.length
rec1=Rectangle()
rec1.__int__(5,10)
print(rec1.area())
