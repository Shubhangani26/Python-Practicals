class Student:
    maxAvgmarks=[]
    def __init__(self,n,marks=[0,0,0]):
        self.name =n
        self.marks = marks
    def calcAvg(self):          
        Student.maxAvgmarks.append(self.name,self.marks/len(self.marks))                                             
        s = sum(self.marks)/len(self.marks)
        
        return s
    def avgMarks(self):


# class Student:
#     avgScores = []
#     def __init__(self, n,marks=[0,0,0]):
#         self.name = n
#         self.marks=marks
#         self.calcAvg()

#     def calcAvg(self):
#         Student.avgScores.append((self.name, sum(self.marks)/len(self.marks)))
#         print(Student.avgScores)
#         return (sum(self.marks)/len(self.marks))

#     def maxAvgMarks():
#         maxAvg=0
#         name=""
#         for i in Student.avgScores:
#               if i[1]>maxAvg:
#                 maxAvg=i[1]
#                 name=i[0]
#         return (maxAvg,name)


# students = [Student("Shubhi", [23, 34, 32]), Student("Qwe", [45, 34, 32]), Student("Ary", [23, 100, 32])]
# print("Name of the student with highest average marks :",Student.maxAvgMarks()[1])
# print("The student's average marks :",Student.maxAvgMarks()[0])