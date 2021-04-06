import copy
import time

def read_file(file_name):
    input = []
    with open(file_name, "r") as file:
        for line in file:
            line = line.rstrip("\n")
            current_list = line.split(",")
            # 1st element is the index. assumption: the index is always in sequence: 0, 1, 2,.... etc
            index = int(current_list.pop(0))
            # convert all elements from strings into ints
            current_list = [int(i) for i in current_list]
            input.append(current_list)        # insert into list
    return input
def copyArr(Arr):
    res =[]
    for item in Arr:
        res.append(item)
    return res

def convertToGraph(arr):
    g = {}
    for i in range(len(arr)):
        g[i] = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] in arr[i]:
                g[arr[i][j]].append(i)
    return g
def findLongestArr(arr):
    print(arr)
    if len(arr) <2:
        return arr
    max = len(arr[0])
    for item in arr:
        if len(item) > max:
            max = len(item)
            longest = item
    return longest

def get_cycle(followers,s):
    g = convertToGraph(followers)
    print(g)
    stack = []
    visited =[]
    cycles = []
    stack.append(s)
    count = 0
    while len(stack) != 0:
        count += 1
        if count > 10000:
            break
        hasDepth = False
        v = stack[-1]
        del stack[-1]
        if v not in visited:
            visited.append(v)
            if s in g[v]:
                cycles.append(copyArr(visited))
        for i in range(len(g[v])):
            n = g[v][len(g[v])-1-i]
            if n not in visited:
                hasDepth = True
                stack.append(n)
        if hasDepth == False:
            del visited[-1]
    return findLongestArr(cycles)[0] + [s]
file_name = "case1.csv"
s = 0
followers = read_file(file_name)
followers_clone = copy.deepcopy(followers)
print(get_cycle(followers,s))
