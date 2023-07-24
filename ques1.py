from math import *
def area(a,b,c):
    s=(a+b+c)/2
    area=sqrt(s*(s-a)*(s-b)*(s-c))
    return area,s*2

a=int(input("Enter the length of the side 1 :"))
b=int(input("Enter the length of the side 2 :"))
c=int(input("Enter the length of the side 3 :"))

t=area(a,b,c)
print("Area of the triangle is :",t[0],"\n","Perimeter of the triangle is :",t[1])