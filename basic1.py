# def occur(s):
#     count = {}
#     for i in s :
#         if i in count:
#             count[i]+=1
#         else:
#             count[i]=1
#     return count
# print(occur('google.com'))


# def change(d):
#    ch = d[0]
#    d = d.replace(ch,"&")
#    d = ch + d[1::]
#    return d
# print(change("restart"))
 

# def removeNthch(str,n):
#     first = str[:n]
#     last =  str[n+1::]
#     return first + last
# print(removeNthch("shubhi",3))


# def upperCase(s):
#     count={"upper":0,"lower":0}
#     for i in s :
#         if  i.isupper():
#             count["upper"]+=1
#         elif i.islower():
#             count["lower"]+=1
#         else :
#             pass
#     return count
# print(upperCase("sHubHANganI"))

# def replace(n):
#     v = "aeiouvAEIOUV"
#     for i in n :
#         n=n.replace(v,"#")
#     return n
# print(replace("Shubhi"))4

# def minsum(l):
#     d= []
#     for i in range(len(l)):
#        d.append(sum(l[i]))
#     return min(d)
# print(minsum([[1,2],[2,3],[4,5]]))

# def series(n):
#     s =0
#     for i in range(1,n+1,1):
#        sum = 1/(i+(i-1)) 
#        s = sum+s 
#     return s
# print(series(3))

# class Name:
#     def __init__(self,f,m,l):
#       self.f =f
#       self.m =m
#       self.l =l
# f = "sita"
# name = Name(f,"F","Smith")
# f = "dd"
# name.l ="mita"
# print(name.f,name.l)

# a = [1,2,3]
# b = a[0:]
# print(b)

# l = []
# def convert(b):
#     if(b==0):
#         return 1
#     dig = b%2
#     l.append(dig)
#     convert(b//2)
# convert(6)
# l.reverse()
# for i in l:
#    print(i)

# a =[2,6,1]
# b = a
# b[0]=5
# print(a)

# s = "shubhi"
# print(s.split("h"))

# marks = {60,70,75}
# marks.add(2)
# print(marks)

# names = ["john","ben","walter","mile"]
# names.sort()
# print(names)

# def pattern(n):
#     for i in range(1,n+1):
#         for j in range(1,i+1):
#             print(j,end=" ")
#         print('\n')
# pattern(4)

#print(set.symmetric_difference({1,2,4,6,7}{3,2,1,6,7}))
#print("sum of 2 and 3 is " + 5)

sub = {"maths" : ["j","s","b"],
        "Physics":["j","m","m" ],
        "bio":["j","s" ]
        }
for i in sub:
     if(len(sub(i)[1] ) < m):
         m =

