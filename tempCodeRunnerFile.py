def fac(n):
    if(n==0):
        return 1

    n*fac(n-1)
    print("a")
print(fac(3))