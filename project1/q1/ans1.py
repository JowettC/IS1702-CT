
def getCombination(arr, n, r, total): 
      
    # A temporary array to  
    # store all combination 
    # one by one 
    data = [0]*r; 
  
    # Print all combination  
    # using temprary array 'data[]' 
    return combinationUtil(arr, data, 0,  
                        n - 1, 0, r,total)
    
  
# arr[] ---> Input Array 
# data[] ---> Temporary array to 
#         store current combination 
# start & end ---> Staring and Ending 
#             indexes in arr[] 
# index ---> Current index in data[] 
# r ---> Size of a combination  
# to be printed  
def combinationUtil(arr, data, start,  
                    end, index, r, total): 
                          
    # Current combination is ready  
    # to be printed, print it 
    if (index == r): 
        test = []
        for j in range(r): 
            test.append(data[j])
        # print(test)
        if(sum(test) == total):
            
            return test
        return False; 
  
    # replace index with all 
    # possible elements. The 
    # condition "end-i+1 >=  
    # r-index" makes sure that  
    # including one element at 
    # index will make a combination  
    # with remaining elements at  
    # remaining positions 
    i = start;  
    while(i <= end and end - i + 1 >= r - index): 
        data[index] = arr[i]; 
        
        ansFound = combinationUtil(arr, data, i + 1,  
                        end, index + 1, r,total)
        if (ansFound!= None and ansFound != False):
            if sum(ansFound) == total:
                return ansFound
        i += 1; 

def group(s):
    total = sum(s)
    # print(total//2)
    if (total % 2 !=0):
        return None,None
    else:
        for i in range(1,len(s)+1):
            ans = getCombination(s, len(s), i,total//2)
            if ans != None:
                for num in ans:
                    s.remove(num)
                return ans,s
        return None,None

s = [135, 129, 141, 121, 105, 109, 105, 147]
print(group(s))
# print(sum([135, 129, 141, 121]))
  
# This code is contributed by mits 