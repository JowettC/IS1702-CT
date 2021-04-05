

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
def canAdd(followers,s,cycle):
    for i in range(len(cycle)):
        if s not in followers[cycle[i]] and cycle[i] not in followers[s]:
            return False
    return True


def clique(followers,s):
    cycle = []
    cycles =[]
    for i in range(len(followers[s]):
        

    

    
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
print(canAdd(followers,8,[0,9,10]))
# print(get_clique(followers))

