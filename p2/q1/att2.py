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
    visited =[]
    # print(g.getVertexWithValue(0).getAdjList())
    stack.append(Vertex(s))
    while len(stack) != 0:
        v = stack[-1]
        del stack[-1]
        if v not in visited:
            visited.append(v)
        test = g.getVertexWithValue(v).getAdjList()
        for i in range(len(test)):
            n = test[len(test)-1 -i]
            if n[0] not in visited:
                print(n[0])
                print(n[0])
                stack.append(n[0])
                # use dfs function
        
    return None



file_name = "case1a.csv"
s = 0
followers = read_file(file_name)
followers_clone = copy.deepcopy(followers)
print(get_cycle(followers,s))
