def cyclic(graph):
    visited = set()
    path = [object()]
    path_set = set(path)
    stack = [iter(graph)]
    while stack:
        for v in stack[-1]:
            if v in path_set:
                return False
            elif v not in visited:
                visited.add(v)
                path.append(v)
                path_set.add(v)
                stack.append(iter(graph.get(v, ())))
                break
        else:
            path_set.remove(path.pop())
            stack.pop()
    return True

def graph(array):
  map = {}
  nodes = len(array)
  for nodenum in range(nodes):
    map[nodenum] = []
  for i in range(nodes):
    for j in range(len(array[i])):
      follower = array[i][j]
      map[follower] += [i]
  return map

def is_DAG(followers):
  graphmap = graph(followers)
  ans = cyclic(graphmap)
  return ans