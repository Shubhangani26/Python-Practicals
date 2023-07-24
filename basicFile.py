# f = open("from.txt",'r')
# data = f.read(10)
# print(data)
# f.close()

# f =open("from.txt",'r')
# line1 =f.readline()
# print(line1,end="")
# line2 =f.readline()
# print(line2,end="")
# line3 =f.readline()
# print(line3,end="")
# line4 =f.readline()
# print(line4,end="")

# f = open("from.txt",'r')
# line = f.readlines()
# for i in line:
#     print(i,end='')
# f.close()

'''for writing a string we use write() method 
      but for writing the sequence data type like list ,tuple we use writelines() method '''
f = open("file1.txt",'w')
# -------list= [3,1,2,3,4,0] // give error bcz in file handing only string arugment we can give---------
list = ['shubhi','shubh','shubham']
f.writelines(list)
f.write("yes bro!!")
print("done")
f.close()
# name = input("enter your name ")
# age = input(" Enter your age ")

# f = open("file2.txt",'w')
# f.write(name)
# f.write(age)
# f.close()
