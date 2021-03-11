def max_array(a):
    if len(a) == 1:
        return a[0]
    if a[0] > max_array(a[1:]):
        return a[0]
    else:
        return max_array(a[1:])

print(max_array[1,2,3,4,5,6])