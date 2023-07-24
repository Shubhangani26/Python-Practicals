# def occur(l):
#     dict = {}
#     j = "".join(l)
#     for i in j:
#         if i in dict :
#             dict[i]+=1
#         else:
#             dict[i] = 1
#     return dict
# l = eval(input("enter a list "))
# print(occur(l))  



# def arrange(s):
#     l = list(s)
#     l.sort()
#     return ''.join(l)
# print(arrange('shuBhaNganI'))


# def Sum(n):
#     sum =0
#     for i in range(1,n+1):
#         num = eval('2'*i)
#         sum+=num
#     return sum
# print(Sum(3))
   
# def Set(s1,s2):
#    for x in s1.difference(s2):
#      del x
# def binary(s2,n) :
#     l = list(s2)
#     l.sort()
#     low = 0
#     high = len(l)-1
    
#     while(low<=high):
#         mid = (low+high)//2
#         if(s2[mid]==n):
#            return s2[mid]
#         elif(s2[mid]<n):
#             low= mid+1
#         else:
#             hight =mid-1


# s1 = {5,9,8,70}
# s2 = {3,5,9,0}
# print(Set(s1,s2))
# print(binary(s2,5))