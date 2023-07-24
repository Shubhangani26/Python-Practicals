def linearSearch(l,ele):
    for i in l:
        if ( i == ele):
            return i
        else :
            return -1
def binarySearch(l,ele):
    low = 0
    upper = len(l)-1
    while(low<=upper):
        mid = (low+upper)//2
        if(l[mid]==ele):
            print(mid)
            return True
        else:
            if(l[mid]<ele):
               low = mid
            else:
                upper= mid 
    return False

l = [8,9,5,0,6]
ele = 8
print(binarySearch(l,ele))