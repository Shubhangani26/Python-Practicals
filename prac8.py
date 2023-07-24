def linearSearch(l,ele):
    for i in l:
        if(i==ele):
            return i
        else:
            return -1
def isNumberic(l):
    isNumberic = False
    for i in l:
        if i.isdigit()==False:
            break
        else :
            isNumberic  =True
        return isNumberic

def oddValue(l):
    count = 0
    for i in l:
        if i%2!=0:
            count+=1
    return count 

def isString(l):
    isString = True
    for i in l:
        if str(i).isdigit()==True:
            isString = False
            break
    return isString

def reverseList(l):      
    l.reverse()
    return l
# def reverse(number):
#   rem =0
#  while(number!=0):
#     digit = number%10
#     rem =rem*10 +digit
#     number=number//10

def largestString(l):
    return max(l)

def removeEle(l,ele):
     l.remove(ele)
     return l
    
def sortList(l):
    l.sort(reverse=True)
    return l
def commonMember(l,m):
    return[i for i in l if i in m]

def menu():

   print(
    ''' \t0.Exit
        1.Check if all elements in list are numbers or not .
        2.If it is a numeric list, then count number of odd values in it.
        3.If list contains all Strings, then display the largest String in the list.
        4.Display list in reverse form.
        5.Find a specified element in list.
        6.Remove the specified element from the list.
        7.Sort the list in descending order.
        8.accept 2 lists and find the common members in them.''')
   print("-----------------------------------------------------------------")

   run = True
   while(run):
    menu()
    i = int (input("enter your choice : "))
    l = eval(input("Enter your list : "))
    match i :
        case 1 :
            print(isNumberic(l))
        case 2 :
            if (isNumberic(l)):
                print("List contain  numbers :")
                print(oddValue(l))
            else :
                print("first please enter numberic list ")
        case 3:
            if isString(l):
                print(largestString(l))
            else:
                print("Please enter a list of strings.")

        case 4 :
            print(reverseList(l))

        case 5:
            ele = int(input("enter element you want to search in a list"))
            print(linearSearch(l,ele))

        case 6 :
            print(removeEle(l,ele))

        case 7 :
            print("Sorted list is : ",sortList(l))
        case 8 : 
            m = eval(int(input("Enter another list")))
            print(commonMember(l,m))