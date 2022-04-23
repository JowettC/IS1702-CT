
def mystery(n):
    if n == 0:
        return 1
    if n == 1:
        return 3
    if n == 2:
        return 5
    x = 1
    y = 3
    z = 5
    for i in range(1,(n-1)):
        w =z + (y**2) + (x**3)
        x = y
        y = z
        z = w
    return z
# recursive
def mysteryr(n,x=1,y=3,z=5):
    if n == 0:
        return 1
    if n == 1:
        return 3
    if n == 2:
        return z
    return mysteryr(n-1,y,z,z +(y**2)+(x**3))
    
print(mystery(5))
print(mysteryr(5))