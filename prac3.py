def fac(n):
    if(n==0):
        return 1
    else:
        return n*fac(n-1)
def fib(n):
    if(n <= 1 ):
        return n
    else:
        return fib(n-1)+fib(n-2)
def nfib(n):
    return [fac(n),fib(n)]

n = int(input("Enter no. : "))
print("Factorial of "+str(n)+ " is "+ str(fac(n)))
print("Fibonacci of "+str(n)+ " is "+ str(fib(n)))
print("result is " + str(nfib(n)))