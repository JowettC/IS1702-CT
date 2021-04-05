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

def is_DAG(followers):
    g = convertToGraph(followers)
    visited =[]
    for item in g.keys():
        if item in visited:
            continue
        stack = []
        # visited = []
        stack.append(item)
        while len(stack) > 0:
            temp = stack[-1]
            del stack[-1]
            if temp not in visited:
                visited.append(temp)
                # print(v)
            adjList = g[temp]
            for i in range(len(adjList)):
                n = adjList[len(adjList)-1-i]
                if n not in visited:
                    stack.append(n)
                else:
                    # print (visited)
                    # print(n)
                    return False
        return True

file_name = "case2.csv"
s = 88

followers = read_file(file_name)
followers_clone = copy.deepcopy(followers)
g = convertToGraph(followers)
result = (is_DAG(followers))
print(result)
# for i in range(len(result)-1):
#     if result[2] not in g[result[1]]:
#         print(g[result[1]])
#     else:
#         print("Fine")
        

