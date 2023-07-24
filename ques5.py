from ques3 import fact
from math import *

def seriesSum(n,x):
   sum=1
   count = 2
   for i in range(2,n+1,1):
      if i%2==0:
        sum-=pow(x,count)/fact(count)
      else:
         sum+=pow(x,count)/fact(count)
      count+=2
   return sum

n=int (input("Enter the number of terms in the series :"))
x=int (input("Enter a positive integer:"))
print("Sum of the series is :",seriesSum(n,x))