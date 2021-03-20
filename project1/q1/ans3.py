
def findSets(arr, n, set1, set2, sum1, sum2, pos) : 
    if (pos == n) :  
        if (sum1 == sum2) : 
            return set1,set2
        else : 
            return False     
    set1.append(arr[pos]) 
    res = findSets(arr, n, set1, set2,  
               sum1 + arr[pos], sum2, pos + 1) 
    if (res) : 
        return res 
    set1.pop() 
    set2.append(arr[pos]) 
    res= findSets(arr, n, set1, set2, sum1,  
                     sum2 + arr[pos], pos + 1) 
    if not res:         
        set2.pop() 
    return res 

def isPartitionPoss(arr, n) : 
    total = sum(arr)
  
    # for i in range(0, n): 
    #     sum += arr[i] 
    # # partitioned. 
    if (total % 2 != 0) : 
        return False
    set1 = [] 
    set2 = [] 
    return findSets(arr, n, set1, set2, 0, 0, 0) 

def group(s):
    n = len(s)
    ans = isPartitionPoss(s,n)
    if ans == False:
        return None,None
    else:
        return ans
# Driver code 
# arr = [5, 5, 1, 11] 
# n = len(arr) 
# print(group(arr))
      
# This code is contributed by Manish Shaw 
# (manishshaw1) 

s = [135, 129, 141, 121, 105, 109, 105, 147]
print(group(s))