class Person:
	def __init__(self, firstName, lastName, idNumber):
		self.firstName = firstName
		self.lastName = lastName
		self.idNumber = idNumber
	def printPerson(self):
		print("Name:", self.lastName + ",", self.firstName)
		print("ID:", self.idNumber)

class Student(Person):
    def __init__(self, firstName, lastName, idNumber, scores):
        super().__init__(firstName, lastName, idNumber)
        self.score = scores
		
    def calculate(self):
        # print(self.score)
        lengthOfS = len(self.score)
        sumOfS = 0
        for i in self.score:
            sumOfS += i
        avgOfS = sumOfS // lengthOfS

        grade = ""
        if avgOfS >= 90 and avgOfS <= 100:
            grade = "O"
        elif avgOfS >= 80 and avgOfS < 90:
            grade = "E"
        elif avgOfS >= 70 and avgOfS < 80:
            grade = "A"
        elif avgOfS >= 55 and avgOfS < 70:
            grade = "P"
        elif avgOfS >= 40 and avgOfS < 55:
            grade = "D"
        else:
            grade = "T"
        return grade
line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input()) # not needed for Python
scores = list( map(int, input().split()) )
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())