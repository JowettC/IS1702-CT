def comSets(arr, length, leftArr, RightArr, sum1, sum2, pos):
    if pos == length:  
        if sum1 != sum2: 
            return False
        else: 
            return leftArr,RightArr
    
    leftArr.append(arr[pos]) 
    res = comSets(arr, length, leftArr, RightArr,  
               sum1 + arr[pos], sum2, pos + 1)
    # print(res)
    if res != False: 
        return res 
    leftArr.pop() 
    RightArr.append(arr[pos]) 
    res= comSets(arr, length, leftArr, RightArr, sum1,  
                     sum2 + arr[pos], pos + 1) 
    if res == False:
        RightArr.pop() 
    return res 

def group(s):
    total = sum(s)
    if total % 2 == 1 : 
        return False
    length = len(s)
    leftArr = [] 
    RightArr = []
    ans = comSets(s, length, leftArr, RightArr, 0, 0, 0)
    if ans == False:
        return None,None
    else:
        return ans



print(group([-1, 1, 4, 2, 8, 0]))