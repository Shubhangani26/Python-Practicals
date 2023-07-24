#to copy the content of a file to another file
f1 = open("file3.txt",'r')
f2 = open("file4.txt",'w')
line = f1.readlines()
while(line !=''):
    f2.write(line)
    line = f1.readline()
print("done")
f1.close()
f2.close()
