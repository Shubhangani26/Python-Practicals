def length(s):
    return len(s)

def maxi(s1,s2,s3):
   if(s1>s2 and s1>s3):
    return s1
   elif(s2>s3 and s2>s1):
    return s2
   else :
    return s3

def vowels(s):
    v = "aeiouvAEIOUV"
    l = list(s)
    for i in len(l) :
        if l[i] in v:
            l[i]= "#"
    j = "".join(l)   # s= ['g','e','e','k']       "".joint(s)=geek
    del l 
    return j
def wordcount(s) :
    return len(s.split()) # split remove all whitspaces

def pal(s) :
    mid = len(s)//2
    start = 0
    last = len(s)-1
    flag = 0
    while(start<=mid):
        if(s[start]==s[last]):
            start = start+1
            last = last-1
        else:
            flag = 1
            break
    if flag ==0:
        print("palindrome")
    else :
        print("not a palindrome")
'''  def pal(s):
        ans = s[ : :-1]
        if (ans==s)
          print("palindrome)
        else
           print("not'''
def menu():
    print(
        '''/0 exit
            1.Find the length of string.
            2.Return maximun of the three strings
            3.Accept a string and replace all vowels with #
            4.Find number of words in the given string 
            5.Check whether the string is a palindrome or not 
            '''
    )
run = True
while(run):
    menu()
    i = int(input("enter your choice :"))
    s = int(input("enter a word"))
    match(i):
        case 1:
              print("The length of string is :", length(s))
        
        case 2:
            t=eval(input("Enter three strings as a tuple:"))
            s=max(t[0],t[1],t[2])
            print("Maximum of the entered three strings is :", s)

        case 3:
           print("Resultant string :",vowels(s))

        case 4:
            print("Number of words in the given string is :",wordcount(s))

        case 5:
            if(pal(s)):
                print("String is Palindrome")
            else:
                print("Not a Palindrome")

        case default:
            if i ==0:
                print("exit")
                run = False
            else:
                print("Wrong input")