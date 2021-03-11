def find_minimum(a,k):
    min = a[0]
    max = a[0]

    for j in range (1,len(a)):
        if min > a[j]:
            min = a[j]
        if max < a[j]:
            max = a[j]
    if k <=1:
        return min
    if k >= len(a):
        return max
    for i in range (2,k+1):
        ith_min = max
        for j in range(len(a)):
            if a[j] < ith_min and a[j] > min:
                ith_min = a[j]
        min =ith_min
        print(i)
        print(ith_min)
        print("---")
    return ith_min

a=[3,5,1,10,7,22,15,19,6,8,16]
k =6

print(find_minimum(a,k))