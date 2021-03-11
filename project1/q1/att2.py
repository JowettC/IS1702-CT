
def rmSort(a):
  if len(a) == 1:
    return a 
  mid = len(a)//2
  a1 = rmSort(a[0:mid])
  a2 = rmSort(a[mid:len(a)])  
  return merge(a1, a2)

# Helper Method: Merge
def merge(a1, a2):
	i = 0
	j = 0
	r = []
	while i < len(a1) or j < len(a2):
		if (j == len(a2)) or (i < len(a1) and a1[i] > a2[j]):
			r.append(a1[i]) # pick item from a1
			i += 1
		else:
			r.append(a2[j]) # pick item from a2
			j += 1
	return r


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

# s1 = [-1, 1, 4, 2, 8, 0]
# s2 = [2, 2, 2, 2, 4]
s3 = [1, 3, 5, 10, 2, 4, 9, 5, -1]
s4 = [-14, 3, 4, 13, -1, -5, 0, 5, -10, 8, -4, 10, -12, 11, 9, 12, -6, -11, -9, -8]
s5 = [200,9,1,169,6,30,57]
s1,s2 = group(s5)

sum_s1 = sum(s1)
sum_s2 = sum(s2)
print("Your function returned: ")
print("    s1 = " + str(s1) +", sum(s1) = " + str(sum_s1))
print("    s2 = " + str(s2) +", sum(s2) = " + str(sum_s2))