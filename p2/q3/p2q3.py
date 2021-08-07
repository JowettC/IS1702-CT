from collections import defaultdict

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
      
<<<<<<< Updated upstream
    print(g)
    allCycles = find_cliques(g)
    allCycles.sort(key=len, reverse= True)
    res = list(allCycles[0])
    return res
  
followers_1a = [[5, 8, 10], [2, 6], [1, 3], [1, 5], [2, 5], [4, 6, 9], [1, 3, 9], [6], [7, 10], [0, 6, 8, 10], []]
print(get_clique(followers_1a))
=======
    # print(g)
    allCycles = find_cliques(g)
    allCycles.sort(key=len, reverse= True)
    res = list(allCycles[0])
    return res
>>>>>>> Stashed changes
