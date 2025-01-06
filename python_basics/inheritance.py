class person:
    def __init__(self,fname,lname):
        self.firstName = fname
        self.lastName = lname
    
    def printName(self):
        print(self.firstName,self.lastName)

x = person("Jhon","Deo")
x.printName()


class student(person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationYear = year
y = student("Mike","leo",2019)
y.printName()
print(y.graduationYear)
