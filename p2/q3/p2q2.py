def convertToGraph(arr):
    g = {}
    for i in range(len(arr)):
        g[i] = []
    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if arr[i][j] in arr[i]:
                g[arr[i][j]].append(i)
    return g

def is_DAG(followers):
    g = convertToGraph(followers)
    previousList =[]
    
    for item in g.keys():
        if item in previousList:
            continue
        stack = []
        visited = []
        stack.append(item)
        while len(stack) > 0:
            haveDepth = False
            temp = stack[-1]
            del stack[-1]
            if temp not in visited:
                visited.append(temp)
                # print(v)
            adjList = g[temp]
            for i in range(len(adjList)):
                n = adjList[len(adjList)-1-i]
                if n not in visited:
                    haveDepth = True
                    stack.append(n)
                else:
                    # print (visited)
                    # print(n)
                    return False
            if haveDepth == False:
                del visited[-1]
        previousList = visited
            
        return True