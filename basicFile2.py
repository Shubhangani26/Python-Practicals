def capitalize():
    f1 = open("file3.txt",'r')
    f2 = open("file4.txt",'w')
    while 1 :
      line = f1.readline()
      if not line:
        break
      line = line.rstrip()
      lenght = len(line)
      str = ""
      str= str + line[0].upper()
      i = 1
      while i < lenght:
        if(i=="."):
          str = str+ line[i]
          i+=1
          if i >=lenght:
             break
          str = str +line[i].upper()
        else:
          str = str + line[i]
        i=i+1
      f2.write(str)
    else:
      print("source file doesnt exist ")
    f1.close()
    f2.close()
capitalize()



