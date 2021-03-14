import itertools

def bruteForce(s):
    for i in range(1,len(s)+1):
        ans = sum(s)/2
        numberstoTest = list(itertools.combinations(s,i))
        for numbers in numberstoTest:
            if sum(numbers) == ans:
                return numbers
    return False
def group(s):
    if sum(s) % 2 != 0:
        return None,None
    leftArr = bruteForce(s)
    if leftArr == False:
        return None,None
    else:
        for num in leftArr:
            s.remove(num)
    return list(leftArr),s

s = [-1, 1, 4, 2, 8, 0]
print(group(s))
