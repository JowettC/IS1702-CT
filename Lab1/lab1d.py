def gcd_d(x, y):
    k = 0
    while x %2 == 0 and y % 2 == 0:
            x = x /2
            y = y /2
            k = k + 1
    while x != y:
            if x % 2 ==0:
                x = x/2
            elif y % 2 ==0:
                y = y/2
            elif x > y:
                x = (x-y)/2
            else:
                y = (y-x)/2
    print((x * 2**k))
    return  (x * 2**k)
