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
    if len(res) == 0:
        return []
    else:
        return res + [s]