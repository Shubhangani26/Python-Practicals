def copyAlternativeLines(f1,f2):

    try:
     file1=open(f1,"r")
     file2=open(f2,"w+")
     lines=file1.readlines()
     for i in range(0,len(lines)):
        if i%2!=0:           # index starts from 0 , zero is assumed to be odd
            file2.write(lines[i])
        else:
            pass
    except EOFError:
        print("Reached the end of the file")
    except Exception as err:
        print("Ran into some error :(")
        print(type(err))
    else:
        print("Successfully copied data of", f1, " to ", f2)
        file1.close()
        file2.close()

file1="from.txt"
file2="to.txt"
copyAlternativeLines(file1,file2)
def showContent(file):
    try:
        file = open(file, "r")
        for i in file:
            print(i.strip())  #removing the newline character from the string
    except Exception as err:
        print("Ran into some error :(")
        print(type(err))
    else:
        file.close()

showContent("to.txt")