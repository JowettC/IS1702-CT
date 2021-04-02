from LinearDSLab import *


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

        
def validateCycle(graph,arr):
    remove =[]
    removetimes=0
    for i in range(0,len(arr)-1):
        # print(arr[i-removetimes+1])
        # print(graph[arr[i-removetimes]])
        if arr[i-removetimes+1] not in graph[arr[i-removetimes]]:
            # print()
            # print("run")
            # del arr[i-removetimes]
            # removetimes += 1
    
    return arr
def get_cycle(followers, s):
    #  convert into dict
    graph = {}
    stack = Stack()
    cycles =[]
    visited = []
    cycle = []
    for i in range(len(followers)):
        graph[i] = followers[i]
    # print (graph)
    stack.push(s)
    while stack.count() != 0:
        havedepth = False
        v = stack.pop()
        # print(v)
        if v not in visited:
            visited.append(v)
            cycle.append(v)
            
            if s in graph[v]:
                cycles.append(copyArr(cycle))
            # print(v)
        for i in range(len(graph[v])):
            n = graph[v][len(graph[v])-1-i]
            if n not in visited:
                havedepth = True
                stack.push(n)
        if havedepth == False:
            del cycle[-1]
                
        
    # TODO: edit this function.
    # print(g)
    # print(followers)
    res ="done"
    return validateCycle(graph,findLargestArr(cycles) + [s])

