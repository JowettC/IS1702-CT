def get_path(x1, y1, x2, y2, ystep =0, xstep = 0, count = 0):
    if ystep == 0:
        ystep = abs(x1)
<<<<<<< Updated upstream
        # print(ystep)
=======
>>>>>>> Stashed changes
    if xstep == 0:
        xstep = abs(y1)
    if (x1 == x2):
        if (y1 == y2):
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
        # move left
        return get_path(x1 - xstep, y1, x2, y2, ystep,xstep,count+1)
    if(x1 < x2):
        # move right
        return get_path(x1 + xstep, y1, x2, y2,ystep,xstep,count+1)
    if(y1 > y2):
        # print('ran')
        return get_path(x1, y1 - ystep, x2, y2,ystep,xstep,count+1)
    if(y1 < y2):
        # print('ran')
        # move up
        return get_path(x1, y1 + ystep, x2, y2,ystep,xstep,count+1)