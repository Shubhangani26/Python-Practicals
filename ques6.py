tuple1=(1,2,5,7,9,2,4,6,8,10)
tuple2=(11,13,15)
t3=()
for i in tuple1:
    if i%2==0:
        t3+=i,
print("Tupple with even numbers present :",t3)
t4=tuple1+tuple2
print("Adding tuple2 with tuple1",t4)
print("Maximum value :",max(t4))
print("Minimum value :",min(t4))