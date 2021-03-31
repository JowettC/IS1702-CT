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


def makeGraph(followers):
    g = Graph()
    # add vertex
    for i in range(len(followers)):
        g.addVertex(Vertex(i))
    # print(g)
    for i in range(len(followers)):
        for j in range(0,len(followers[i])):            
            v1 = g.getVertexWithValue(i)
            v2 = g.getVertexWithValue(followers[i][j])
            g.addEdge(v1, v2)
    return g


def get_cycle(followers, s):
    # TODO: edit this function.
    g = makeGraph(followers)
    # print(g)
    return g.getVertexWithValue(s).getAdjList()



file_name = "case1.csv"
s = 2
followers = read_file(file_name)
followers_clone = copy.deepcopy(followers)
print(get_cycle(followers,5))
