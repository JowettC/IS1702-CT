def mystery(n,n2=0,x=0,y=0,z=0):
    if n2 == 0:
        n2 = n
        y = 3
        x = 1
        z = 5
    if n2 == 0:
        return 1
    if n2 == 1:
        return 3
    if n2 == 2:
        return 5
    if n == 2:
       return z
    return mystery(n-1,99,y,z,z+ (y**2) + (x**3))
print(mystery(5))