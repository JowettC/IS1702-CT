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
    for items in start_state:
        res1= []
        for item in items:
            res1.append(item)
        res.append(res1)
    return res

def get_state(start_state, t):

    
    if t <= 0:
        return start_state
    else:
        for i in range(0,t):
            res = copyState(start_state)
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
            start_state = copyState(res)

                        
    return res