def fac(n):
    if(n==0):
        return 1
    else:
        return n*fac(n-1)

def series(n,x):
    sum = 1
    count = 2
    for i in range(2,n+1,1):
        if i%2 == 0 :
            sum -= pow(x,count)/fac(count)
        else :
            sum +=pow(x,count)/fac(count)
        count+=2
    return sum
n = int(input("enter the no. of terms in the series : "))
x = int(input("Enter positive no. "))
print("Sum of the series ",series(n,x))