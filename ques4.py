def digits(n):
   s = set()
   if n >=10:
     while(n>0):
        d = n%10
        s.add(d)
        n = n//10
    
   return s
print(digits(2))
    