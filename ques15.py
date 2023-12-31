class Student:
    avgScores = []

    def __init__(self, n, marks=[0, 0, 0]):
        self.name = n
        self.marks = marks
        self.calcAvg()

    def __del__(self):
        print('Destructor called. Student is deleted.')

    def calcAvg(self):
        Student.avgScores.append((self.name, sum(self.marks)/len(self.marks)))
        print(Student.avgScores)
        return (sum(self.marks)/len(self.marks))

    def maxAvgMarks():
        maxAvg = 0
        name = ""
        for i in Student.avgScores:
            if i[1] > maxAvg:
                maxAvg = i[1]
                name = i[0]
        return (maxAvg, name)

n=int(input("Enter the number of students: "))
students=[]
name=""
marks=[]
for i in range(n):
    print("Enter the data for student ",i+1," : ")
    name=input("Enter name :")
    marks=eval(input("His marks in three subjects :"))
    student=Student(name,marks)
    students.append(student)
print("Name of the student with highest average marks :",
      Student.maxAvgMarks()[1])
print("The student's average marks :", Student.maxAvgMarks()[0])