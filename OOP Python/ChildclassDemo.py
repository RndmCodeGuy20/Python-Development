class Parent:
    def __init__(self, name, age):
        self.name = name
        self.age = age

class Child(Parent):
    def __init__(self, name, age, yob):
        super().__init__(name,age)
        #Parent.__init__(self,name,age)
        self.yob = yob
    def printcred(self):
        print(self.name, self.age, self.yob)


x = Child("Shantanu",19,2002)
x.printcred()