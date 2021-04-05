

# Python3 implementation of the approach

  
# Function to check if the given set of
# vertices in store array is a clique or not
def is_clique(b):
  
    # Run a loop for all set of edges
    for i in range(1, b):
        for j in range(i + 1, b):
  
            # If any edge is missing
            if (graph[store[i]][store[j]] == 0):
                return False
      
    return True
  
# Function to find all the sizes
# of maximal cliques
def maxCliques(i, l):
  
    # Maximal clique size
    max_ = 0
  
    # Check if any vertices from i+1
    # can be inserted
    for j in range(i + 1, n + 1):
  
        # Add the vertex to store
        store[l] = j
  
        # If the graph is not a clique of size k then
        # it cannot be a clique by adding another edge
        if (is_clique(l + 1)):
  
            # Update max
            max_ = max(max_, l)
  
            # Check if another edge can be added
            max_ = max(max_, maxCliques(j, l + 1))
          
    return max_


def convertGraphToEdges(followers):
    res = []
    for i in range(len(followers)):
        for j in range(len(followers[i])):
            res.append([i,followers[i][j]])
    return res
followers = [[5, 8, 10], [2, 6], [1, 3], [1, 5], [2, 5], [4, 6, 9], [1, 3, 9], [6], [7, 10], [0, 6, 8, 10], []]

edges = convertGraphToEdges(followers)
size = len(edges)

n = len(followers)
MAX = n + 1
n = 0
  
# Stores the vertices
store = [0] * MAX
  
# Graph

graph = [[0 for i in range(MAX)] for j in range(MAX)]
  
# Degree of the vertices
d = [0] * MAX

for i in range(size):
    graph[edges[i][0]][edges[i][1]] = 1
    graph[edges[i][1]][edges[i][0]] = 1
    d[edges[i][0]] += 1
    d[edges[i][1]] += 1
    
print(maxCliques(0, 1))
for list in graph:
    print(list)

