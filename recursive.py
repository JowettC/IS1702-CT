
def ap(a,d,n):
    if n == 0:
        print (a)
        return None
    print (a)
    return ap(a+d,d,n-1)
# ap(5,2,10)