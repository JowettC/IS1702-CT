def get_path(x1, y1, x2, y2, ystep =0, xstep = 0, count = 0):
    if ystep == 0:
        ystep = abs(x1)
        # print(ystep)
    if xstep == 0:
        xstep = abs(y1)
    if (x1 == x2):
        if (y1 == y2):
            print(count)
            return True
    if x1 + xstep > x2 and x1 < x2:
        # print('ran')
        return False
    elif x1 - xstep < x2 and x1 > x2:
        # print('ran')
        return False
    elif y1 + ystep > y2 and y1 < y2:
        # print('ran')
        return False
    elif y1 - ystep < y2 and y1 > y2:
        # print(ystep)
        # print('ran')
        return False
    # TODO: edit this function to make it work. This must be recursive
    if (x1 > x2):
        print('leftran')
        # move left
        return get_path(x1 - xstep, y1, x2, y2, ystep,xstep)
    elif(x1 < x2):
        print('rightran')
        # move right
        return get_path(x1 + xstep, y1, x2, y2,ystep,xstep)
    elif(y1 > y2):
        print('Downran')
        return get_path(x1, y1 - ystep, x2, y2,ystep,xstep)
    elif(y1 < y2):
        print('Upran')
        # move up
        return get_path(x1, y1 + ystep, x2, y2,ystep,xstep)

x1 = 5
y1 = 3
x2 = -1
y2 = 8
print(get_path(x1, y1, x2, y2))