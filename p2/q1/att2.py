# EXTRACT THIS CODE & SUBMIT AS p2q1.py TO RED!!!
# Filename: p2q1.py
# Team ID: <TODO: replace with team ID (e.g. Gx_Ty)>

# Except import statements, all other statements should only be in functions.
# import GraphLab  # <-- uncomment if you want to use GraphLab
import copy
import time
from GraphLab import *

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


def formatGraph(followers):
    g = Graph()
    for i in range(len(followers)):
        g.addVertex(Vertex(i))
    # print(g.getVertexWithValue(0))
    for i in range(len(followers)):
        for j in range(len(followers[i])):
            v1 = g.getVertexWithValue(i)
            v2 = g.getVertexWithValue(followers[i][j])
            g.addEdge(v2,v1)
    return g

def get_cycle(followers, s):
    stack =[]
    g = formatGraph(followers)
    # for i in range(11):
    #     print(g.getVertexWithValue(i).getAdjList())
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



file_name = "case1a.csv"
s = 0
followers = read_file(file_name)
followers_clone = copy.deepcopy(followers)
print(get_cycle(followers,s))
print(type(get_cycle(followers,s)[0]))
