def search(a, k):
    i = 0
    while i < len(a):
        if a[i] == k:
            return i
        i = i + 1 
    return -1
# a)
def search2(a, k):
    i = 0
    count = 0
    while i < len(a):
        if a[i] == k:
            count += 1
        i = i + 1 
    return count
# b)
def search3(a, k):
    i = 0
    count = 0
    while i < len(a):
        if a[i] == k:
            count += 1
        if count == 2:
            return i
        i = i + 1 
    return -1
# c)
def search4(a, k):
    i = 0
    res = -1
    while i < len(a):
        if a[i] == k:
            res = i
        i = i + 1 
    return res