

# from colab week 5
# Recursive Merge Sort
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

# From last week:
# Merge Sort
def mSort(a):
	gs = 1
	while gs < len(a):
		mergeGroups(a, gs)
		gs *= 2
	return a

# Helper Method: Level 2
def mergeGroups(a, gs):
	i = 0
	while i < len(a):
		j = i + 2 * gs
		a1 = a[i:i+gs]
		a2 = a[i+gs:i+gs*2]
		a[i:j] = merge(a1, a2)
		i = i + 2 * gs

def sum(S):
    if S == None or len(S) == 0 :
        return 0
    else:
        total = 0
        for num in S:
            total += num
        return total


def group(S):
    total = sum(S)
    if (total == 0 or total % 2 == 1):
        return None,None

    leftArr = []
    rightArr = []
    totalLeft = 0
    totalRight = 0
    for num in rmSort(S):
        if num < 0:
            if totalLeft == totalRight:
                rightArr.append(num)
                totalRight += num
            elif totalLeft < totalRight:
                rightArr.append(num)
                totalRight += num
            elif totalLeft > totalRight:
                leftArr.append(num)
                totalLeft += num
        else:
            if totalLeft == totalRight:
                rightArr.append(num)
                totalRight += num
            elif totalLeft > totalRight:
                rightArr.append(num)
                totalRight += num
            elif totalLeft < totalRight:
                leftArr.append(num)
                totalLeft += num
    if totalLeft != totalRight:
        leftArr1,rightArr1 = findPairOfNumber(rightArr,totalRight,leftArr,totalLeft)
        return leftArr1,rightArr1
    else:
        return leftArr,rightArr

def findPairOfNumber(leftArr,totalLeft,rightArr,totalRight):
    differenceFound = False

    if totalLeft > totalRight:
        difference = (totalLeft - totalRight)/2
        for numLeft in leftArr:
            for numRight in rightArr:
                if (numLeft - numRight) == difference:
                    leftArr.remove(numLeft)
                    rightArr.remove(numRight)
                    leftArr.append(numRight)
                    rightArr.append(numLeft)
                    totalLeft -= difference
                    totalRight += difference
                    differenceFound = True
                    break
    else:
        difference = (totalRight - totalLeft)/2
        for numRight in rightArr:
            for numLeft in leftArr:
                if (numRight - numLeft) == difference:
                    leftArr.remove(numLeft)
                    rightArr.remove(numRight)
                    leftArr.append(numRight)
                    rightArr.append(numLeft)
                    totalLeft += difference
                    totalRight -= difference
                    differenceFound = True
                    break
    if differenceFound == False:
        return None,None
    else:
        return leftArr,rightArr

# s1 = [-1, 1, 4, 2, 8, 0]
# test1 = arrayEqualSum(s1)
# if test1 != False:
#     print(test1)
#     print(test1[0])
#     print("Total = " + str(test1[1]))
#     print(test1[2])
#     print("Total = " + str(test1[3]))
#     print("--------------------------")

# s2 = [2, 2, 2, 2, 4]
# test2 = arrayEqualSum(s2)
# if test2 != False:
#     print(test2[0])
#     print("Total = " + str(test2[1]))
#     print(test2[2])
#     print("Total = " + str(test2[3]))
#     print("--------------------------")

# s3 = [1, 3, 5, 10, 2, 4, 9, 5, -1]
# test3 = arrayEqualSum(s3)
# if test3 != False:
#     print(test3[0])
#     print("Total = " + str(test3[1]))
#     print(test3[2])
#     print("Total = " + str(test3[3]))

#     print("--------------------------")


# s4 = [-14, 3, 4, 13, -1, -5, 0, 5, -10, 8, -4, 10, -12, 11, 9, 12, -6, -11, -9, -8]
# test4 = arrayEqualSum(s4)
# if test4 != False:
#     print(test4[0])
#     print("Total = " + str(test4[1]))
#     print(test4[2])
#     print("Total = " + str(test4[3]))

#     print("--------------------------")
s1 = [-1, 1, 4, 2, 8, 0]
s2 = [2, 2, 2, 2, 4]
s3 = [1, 3, 5, 10, 2, 4, 9, 5, -1]
s4 = [-14, 3, 4, 13, -1, -5, 0, 5, -10, 8, -4, 10, -12, 11, 9, 12, -6, -11, -9, -8]
s5 = [10,90,100,2000,-500,-100,23,500,3000,-1723]
s1,s2 = group(s5)

sum_s1 = sum(s1)
sum_s2 = sum(s2)
print("Your function returned: ")
print("    s1 = " + str(s1) +", sum(s1) = " + str(sum_s1))
print("    s2 = " + str(s2) +", sum(s2) = " + str(sum_s2))

