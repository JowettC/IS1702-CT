from GraphLab import *

g = Graph()
vertices = ['A', 'B', 'C', 'D', 'E', 'F']
adj_matrix = [
    [0,1,1,0,0,0],
    [0,0,1,1,1,0],
    [1,0,0,1,0,0],
    [0,1,0,0,0,1],
    [0,0,0,1,0,0],
    [0,0,0,0,0,0]
]

for v in vertices:
    g.addVertex(Vertex(v))

for i in range(len(vertices)):
    for j in range(len(vertices)):
        if adj_matrix[i][j] == 1:
            v1 = g.getVertexWithValue(vertices[i])
            v2 = g.getVertexWithValue(vertices[j])
            g.addEdge(v1, v2)
print(g.getVertexWithValue("A").getAdjList())