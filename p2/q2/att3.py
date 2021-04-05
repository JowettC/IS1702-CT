from collections import defaultdict

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

def cycle(followers):
    g ={}
    for i in range(len(followers)):
        g[i] = followers[i]
    stack =[]
    for i in range(len(g.keys())):
        v = i
    return g
# Driver program to test above functions
file_name = "case1.csv"
followers = read_file(file_name)

print(cycle(followers))