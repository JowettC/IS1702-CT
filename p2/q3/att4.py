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

def find_cliques(graph):
  p = set(graph.keys())
  r = set()
  x = set()
  cliques = []
  for v in degeneracy_ordering(graph):
    neighs = graph[v]
    # print(neighs)
    find_cliques_pivot(graph, r.union([v]), p.intersection(neighs), x.intersection(neighs), cliques)
    p.remove(v)
    x.add(v)
  return sorted(cliques)

def find_cliques_pivot(graph, r, p, x, cliques):
  if len(p) == 0 and len(x) == 0:
    cliques.append(r)
  else:
    u = iter(p.union(x)).__next__()
    for v in p.difference(graph[u]):
      neighs = graph[v]
      find_cliques_pivot(graph, r.union([v]), p.intersection(neighs), x.intersection(neighs), cliques)
      p.remove(v)
      x.add(v)

def degeneracy_ordering(graph):
  ordering = []
  ordering_set = set()
  degrees = defaultdict(lambda : 0)
  degen = defaultdict(list)
  max_deg = -1
  for v in graph:
    deg = len(graph[v])
    degen[deg].append(v)
    degrees[v] = deg
    if deg > max_deg:
      max_deg = deg

  while True:
    i = 0
    while i <= max_deg:
      if len(degen[i]) != 0:
        break
      i += 1
    else:
      break
    v = degen[i].pop()
    ordering.append(v)
    ordering_set.add(v)
    for w in graph[v]:
      if w not in ordering_set:
        deg = degrees[w]
        degen[deg].remove(w)
        if deg > 0:
          degrees[w] -= 1
          degen[deg - 1].append(w)

  ordering.reverse()
  return ordering

def get_clique(followers):
    g = {}
    for i in range(len(followers)):
        g[i] = followers[i]
    for i in range(len(followers)):
      for j in range(len(g[i])):
        if i not in g[g[i][j]]:
          g[g[i][j]].append(i)
      
    # print(g)
    allCycles = find_cliques(g)
    allCycles.sort(key=len, reverse= True)
    res = list(allCycles[0])
    return res

file_name = "case1a.csv"
s = 2
followers = read_file(file_name)
followers_clone = copy.deepcopy(followers)
print(get_clique(followers))
