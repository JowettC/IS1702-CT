def gcd_a(x,y):
    t = min(x,y)
    while t != 0:
        if x%t ==0 and y%t ==0:
            return t
        t = t - 1

print(gcd_a(5352, 6690))