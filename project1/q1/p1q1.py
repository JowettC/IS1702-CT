def findNumToSum(arr, target):
    s = []
    while sum(s) != target:
        for i in range(0,len(arr)):
            s.append(arr[i])
            if sum(s) == target:
                return s
            if sum(s)> target:
                s.remove(arr[i])
                continue
            for j in range(i+1,len(arr)):
                s.append(arr[j])
                print(s)
                if sum(s) == target:
                    return s
                if sum(s) > target:
                    s.remove(arr[j])
                    if j == len(arr)-1:
                        while s[len(s)-1] != arr[i]:
                            del s[len(s)-1]
                    continue
                if j == len(arr)-1:
                    while s[len(s)-1] != arr[i]:
                        del s[len(s)-1]
            s.remove(arr[i])
    return False
                
# print(findNumToSum([1,2,3,7,7],5))               


def group(s):
    if sum(s) % 2 != 0:
        return None,None
    ans = sum(s)/2
    leftArr = findNumToSum(s, ans)
    if leftArr == False:
        return None,None
    else:
        for num in leftArr:
            s.remove(num)
    
        return leftArr,s