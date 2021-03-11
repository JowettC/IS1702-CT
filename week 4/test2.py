def findMis(arr):
    total = 0
    max = len(arr)+1
    for num in arr:
        total += num
    for i in range (1,max+1):
        total -= i
    return -(total)

# print(findMis([2,3,5,6,1,7,4,9]))

def max_array(a):
    if len(a) == 1:
        return a[0]
    if a[0] > max_array(a[1:]):
        return a[0]
    else:
        return max_array(a[1:])