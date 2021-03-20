def getNeighCount(my_list,i,j):
    count = 0
    # 1st row
    if i == 0:
        # top left corner
        if j == 0:
            if my_list[i][j+1]:
                count += 1
            if my_list[i+1][j]:
                count += 1
            if my_list[i+1][j+1]:
                count += 1
        #  not corner
        elif j != len(my_list[i])-1:
            if my_list[i][j+1]:
                count += 1
            if my_list[i][j-1]:
                count += 1
            if my_list[i+1][j+1]:
                count += 1
            if my_list[i+1][j]:
                count += 1
            if my_list[i+1][j-1]:
                count += 1
        # top rigth corner
        else:
            if my_list[i][j-1]:
                count += 1
            if my_list[i+1][j]:
                count += 1
            if my_list[i+1][j-1]:
                count += 1
    #  last row
    elif i == len(my_list)-1:
        # bottom left
        if j == 0:
            if my_list[i][j+1]:
                count += 1
            if my_list[i-1][j]:
                count += 1
            if my_list[i-1][j+1]:
                count += 1
        #  not corner
        elif j != len(my_list[i])-1:
            if my_list[i][j+1]:
                count += 1
            if my_list[i][j-1]:
                count += 1
            if my_list[i-1][j+1]:
                count += 1
            if my_list[i-1][j]:
                count += 1
            if my_list[i-1][j-1]:
                count += 1
        # bottom right corner
        else:
            if my_list[i][j-1]:
                count += 1
            if my_list[i-1][j]:
                count += 1
            if my_list[i-1][j-1]:
                count += 1
    # middle rows
    else:
        # side
        if j == 0:
            if my_list[i][j+1]:
                count += 1
            if my_list[i+1][j]:
                count += 1
            if my_list[i+1][j+1]:
                count += 1
            if my_list[i-1][j]:
                count += 1
            if my_list[i-1][j+1]:
                count += 1
        # not side
        elif j != len(my_list[i])-1:
            if my_list[i][j+1]:
                count += 1
            if my_list[i][j-1]:
                count += 1
            if my_list[i+1][j+1]:
                count += 1
            if my_list[i+1][j]:
                count += 1
            if my_list[i+1][j-1]:
                count += 1
            if my_list[i-1][j+1]:
                count += 1
            if my_list[i-1][j]:
                count += 1
            if my_list[i-1][j-1]:
                count += 1
        else:
            if my_list[i][j-1]:
                count += 1
            if my_list[i+1][j]:
                count += 1
            if my_list[i+1][j-1]:
                count += 1
            if my_list[i-1][j]:
                count += 1
            if my_list[i-1][j-1]:
                count += 1
    return count
def copyState(start_state):
    res = []
    count = 0
    for items in start_state:
        res1= []
        for item in items:
            if item == True:
                count = count + 1
            res1.append(item)
        res.append(res1)
    return res,count

# def get_state
def get_state(start_state, t):
    if t <= 0:
        return start_state
    else:
        res,count= copyState(start_state)
        for i in range(0,t):
            if (count < 2 or count >= len(res)*len(res[0]) or len(res)==1 or len(res[0]) == 1):
                resFalse = []
                for i in range(len(res)):
                    line=[]
                    for j in range(len(res[0])):
                        line.append(False)
                    resFalse.append(line)
                return resFalse
            
            for i in range(len(start_state)):
                for j in range(len(start_state[i])):
                    if start_state[i][j]:

                        if getNeighCount(start_state,i,j) == 2 or getNeighCount(start_state,i,j) == 3:
                            continue
                        elif getNeighCount(start_state,i,j) < 2 or getNeighCount(start_state,i,j) > 3:
                            res[i][j] = False
                    else:
                        if getNeighCount(start_state,i,j) == 3:
                            res[i][j] = True
            start_state,count = copyState(res) 
    return res

