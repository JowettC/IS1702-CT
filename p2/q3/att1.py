

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
def copyArr(arr):
    res = []
    for item in arr:
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

def clique(followers,s):
    visited = []
    following = convertToGraph(followers)
    stack = []
    count = 0
    clique = []
    stack.append(s)
    
    while len(stack) != 0:
        v = stack[-1]
        del stack[-1]
        if v not in visited:
            visited.append(v)
            if v in clique:
                continue
            add = True
            for i in range(len(clique)):
                if v not in followers[clique[i]] and v not in following[clique[i]]:
                    add = False
            if add:
                clique.append(v)
        for i in range(len(followers[v])):
            n = followers[v][len(followers[v])-1-i]
            if n not in visited:
                stack.append(n)
    return clique
    

    
def get_clique(followers):
    cliques = []

    for i in range(len(followers)):
        cliques.append(clique(followers,i))
    return cliques

file_name = "case1a.csv"
s = 2
# followers = read_file(file_name)
# followers_clone = copy.deepcopy(followers)
followers = [[5, 8, 10], [2, 6], [1, 3], [1, 5], [2, 5], [4, 6, 9], [1, 3, 9], [6], [7, 10], [0, 6, 8, 10], []]
print(get_clique(followers))