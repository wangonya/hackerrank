# https://www.hackerrank.com/challenges/30-inheritance/problem
import builtins


class Person:
    def __init__(self, firstName, lastName, idNumber):
        self.firstName = firstName
        self.lastName = lastName
        self.idNumber = idNumber

    def printPerson(self):
        print("Name:", self.lastName + ",", self.firstName)
        print("ID:", self.idNumber)


class Student(Person):
    def __init__(self, firstName, lastName, id, scores):
        super().__init__(firstName, lastName, id)
        self.scores = scores

    def calculate(self):
        grades = 'OEAPDT'

        a = sum(self.scores) / len(self.scores)

        conditions = [
            90 <= a <= 100, 80 <= a < 90, 70 <= a < 80,
            55 <= a < 70, 40 <= a < 55, a < 40
        ]

        for i, c in enumerate(conditions):
            if c:
                return grades[i]


line = input().split()
firstName = line[0]
lastName = line[1]
idNum = line[2]
numScores = int(input())
scores = list(map(int, input().split()))
s = Student(firstName, lastName, idNum, scores)
s.printPerson()
print("Grade:", s.calculate())
