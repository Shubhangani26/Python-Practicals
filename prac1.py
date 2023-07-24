from math import *
def side(s1,s2,s3):
   s  = (s1+s2+s3)/2
   area = sqrt((s*(s-s1)*(s-s2)*(s-s3)))
   return (area,s*2)
   
s1 = int(input("enter side"))
s2 = int(input("enter side"))
s3 = int(input("enter side"))
print(side(s1,s2,s3))