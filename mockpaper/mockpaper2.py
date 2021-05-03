def mystery(n, n2=0, x=0, y=0, z=0):
    if n2 == 0:
        n2 = n
    if n == 0:
        return 1
    if n == 1:
        return 3
    if n == 2:
        return 5
    if n2 < 3:
        return z
    if x == 0:
        x = 1
        y = 3
        z = 5
    return mystery(n, n2-1, y, z, (z+(y**2) + (x**3) ))


print(mystery(5))

# def mystery2(n):
#     if n == 0:
#         return 1
#     if n == 1:
#         return 3
#     if n == 2:
#         return 5
#     x = 1
#     y = 3 
#     z = 5
#     for i in range(1,(n-1)):
#         w = z + (y**2) + (x**3)
#         x = y
#         y = z
#         z = w
#     return z
# print(mystery2(4))