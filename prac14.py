
def alternateFile(f1,f2):
  try :

    file1 =open.file(f1,"r")
    file2 = open.file(f2,"a+")
    lines = f1.readlines()
    for l in lines :
        if l%2==0:
            pass
        else:
            f2.write[lines(l)]
    
  except EOFError:
        print("Reach to the end")
  except :
    print("Run error ")
  else:
    print("Successfully copied from ",f1,"to",f2)
    f1.close()
    f2.close()
f1 ="from.txt"
f2 = "to.txt"

alternateFile(f1,f2)