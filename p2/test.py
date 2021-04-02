# EXTRACT THIS CODE & SUBMIT AS p2q1.py TO RED!!!
# Filename: p2q1.py
# Team ID: <TODO: replace with team ID (e.g. Gx_Ty)>

# Except import statements, all other statements should only be in functions.
# import GraphLab  # <-- uncomment if you want to use GraphLab
import copy
import time
from GraphLab import *
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


def makeGraph(followers):
    g = Graph()
    # add vertex
    for i in range(len(followers)):
        g.addVertex(Vertex(i))
    for i in range(len(followers)):
        for j in range(0,len(followers[i])):            
            v1 = g.getVertexWithValue(i)
            v2 = g.getVertexWithValue(followers[i][j])
            g.addEdge(v1, v2)
    return g

def copyArray(arr):
    res =[]
    for item in arr:
        res.append(item)
    return res
def exist(arr,ele):
    for item in arr:
        if item[0]==ele:
            return True
    else:
        return False
def longestArr(arr):
    res = len(arr[0])
    res1 = arr[0]
    for i in range(len(arr)):
        length = len(arr[i])
        if length > res:
            res = len(arr[i])
            res1 = arr[i]
    return res1
        
def get_cycle(followers, s):
    g = makeGraph(followers)
    # test = g.getVertexWithValue(s).getAdjList()
    # test1 = test[0][0]
    # print(test[0][0].getAdjList())
    stack = Stack()
    visited =[]
    stack.push([g.getVertexWithValue(s)])
    cycles =[]
    while stack.count() > 0:
        v = stack.pop()
        # print(v[0])
        if v[0] not in visited:
            visited.append(v[0])
        for i in range(len(v[0].getAdjList())):
            n = v[0].adjList[len(v[0].getAdjList())-1-i]
            
            if n[0] not in visited:
                stack.push(n)
                if exist(n[0].getAdjList(),g.getVertexWithValue(s)):
                    # print(n[0])
                    copy = copyArray(visited)
                    # print(copy)
                    cycles.append(copy+[n[0]])
                # print(str(n) + " --- " + str(n[0].getAdjList()))
                
        # print (visited)
    return longestArr(cycles)


file_name = "case1.csv"
s = 2
followers = read_file(file_name)
followers_clone = copy.deepcopy(followers)

print(get_cycle(followers,0)) 
