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

def convertToGraph(arr):
    g = {}
    for i in range(len(arr)):
        g[i] = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] in arr[i]:
                g[arr[i][j]].append(i)
    return g

def copyArr(Arr):
    res =[]
    for item in Arr:
        res.append(item)
    return res

def findLargestArr(arr):
    if len(arr) == 0:
        return []
    max = len(arr[0])
    res = arr[0]
    for i in range(1,len(arr)):
        if len(arr[i])>max:
            max = len(arr[i])
            res = arr[i]
    return res
def validate(g,arr):
    res = [arr[0]]
    for i in range(len(arr)-1,0):
        if arr[i] not in g[arr[i-1]]:
            continue
        else:
            res.append(arr[i])
def get_cycle(followers, s):
    g = convertToGraph(followers)
    stack = []
    cycles = []
    visited = []
    stack.append(s)
    while len(stack) > 0:
        havedepth = False
        temp = stack[-1]
        del stack[-1]
        if temp not in visited:
            visited.append(temp)
            if s in g[temp]:
                cycles.append(copyArr(visited))
            # print(v)
        adjList = g[temp]
        for i in range(len(adjList)):
            n = adjList[len(adjList)-1-i]
            if n not in visited:
                havedepth = True
                stack.append(n)
        if havedepth == False:
            del visited[-1]
    res = findLargestArr(cycles)
    return cycles
    if len(res) == 0:
        return []
    else:
        return res + [s]



# file_name = "case1a.csv"
s = 6
# followers = read_file(file_name)
a = [[5, 8, 10], [2, 6], [1, 3], [1, 5], [2, 5], [4, 6, 9], [1, 3, 9], [6], [7, 10], [0, 6, 8, 10], []]
# followers_clone = copy.deepcopy(followers)
print(get_cycle(a,s))
