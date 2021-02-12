def gcd_b(x,y):
    while x!=y:
        if x > y:
            x = x -y
        elif y > x:
            y = y -x
    return x

print(gcd_b(5352, 6690))