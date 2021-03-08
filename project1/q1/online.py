# Python3 program to split an array into Two 
# equal sum subarrays 
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
# Returns split point. If not possible, then 
# return -1. 
def findSplitPoint(arr, n) : 
   
    leftSum = 0 
    
    # traverse array element 
    for i in range(0, n) : 
       
        # add current element to left Sum 
        leftSum += arr[i]  
    
        # find sum of rest array elements (rightSum) 
        rightSum = 0 
        for j in range(i+1, n) : 
            rightSum += arr[j]  
    
        # split poindex 
        if (leftSum == rightSum) : 
            return i+1 
       
    
    # if it is not possible to split array into 
    # two parts 
    return -1
   
    
# Prints two parts after finding split pousing 
# findSplitPoint() 
def printTwoParts(arr, n) : 
   
    splitPo = findSplitPoint(arr, n) 
    
    if (splitPo == -1 or splitPo == n ) : 
        print ("Not Possible") 
        return
       
    for i in range(0, n) : 
        if(splitPo == i) : 
            print ("") 
        print (str(arr[i]) + ' ',end='') 
   
# driver program 
arr = rmSort([1,4,-5,7,10,-19,7,9] )
n = len(arr) 
printTwoParts(arr, n) 
  
# This code is contributed by Manish Shaw 
# (manishshaw1) 