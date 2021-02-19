def search(a, k):
    i = 0
    sum = 0
    while i < len(a):
        sum += 1
        if a[i] == k:
            return sum
        i = i + 1 
    return sum

def search2(a, k):
    i = 0
    found = False
    while i < len(a):
        if a[i] == k:
            if found == False:
                found = True
            else:
                return i
        i = i + 1 
    return -1
def search3(a, k):
    i = len(a)-1
    while i > -1:
        if a[i] == k:
            return i
        i = i - 1 
    return -1

x = [1,23,456,23,23,16832146,34565461,65464,2,4,52,3,4,5,1,2,5,44,4,653,23,4,4,8,23]
print(search3(x,23))