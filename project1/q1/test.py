
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


def group(s):
    total = sum(s)
    s1 = []
    s2 = []
    if total % 2 == 1 or total ==0:
        return None,None
    else:
        sumToFind = total/2
        # sortS= rmSort(s)
        sortS = sorted(s, key=int, reverse=True)
        hasNegative = False
        negativePos = -1
        for i in range(len(sortS)):
            if sortS[i] < 0:
                hasNegative = True
                negativePos = i

        if hasNegative:
            for i in range(negativePos):
                if sum(s1) < sum(s2):
                     s1.append(sortS[i])
                else:
                    s2.append(sortS[i])
            for i in range(negativePos,len(sortS)):
                if sum(s1) > sum(s2) or sum(s2) + s[i] == sumToFind:
                    s2.append(sortS[i])
                else:
                    s1.append(sortS[i])

        else:
            for i in range(len(sortS)):
                if sum(s1) < sum(s2) or sum(s1)+ s[i] == sumToFind:
                    if s[i] < 0:
                        s2.append(sortS[i])
                    else:
                        s1.append(sortS[i])
                else:
                    if s[i] < 0:
                        s1.append(sortS[i])
                    else:
                        s2.append(sortS[i])
    return s1, s2

S = [9, 4, -5, 7, 10, -19,7,1]
print(group(S))