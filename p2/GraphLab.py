from queue import Queue
from time import sleep
import random
import copy

class Graph:
    # class constructor
    def __init__(self):
        self.vertices = []
    
    # checks whether the graph is empty
    def isEmpty(self):
        return len(self.vertices) == 0		
    
    def addVertex(self, vertex, x = None, y = None):
        if not isinstance(vertex, Vertex):
            vertex = Vertex(vertex)
        if vertex in self.vertices:
            print("Vertex already added in the graph!")
            return False
        if x == None or y == None:
            x = random.randrange(551)
            y = random.randrange(551)
        while self.isCoordsOccupied(x, y):
            x = random.randrange(551)
            y = random.randrange(551)
        self.vertices.append(vertex)
        if vertex.x == None:
            vertex.setCoords(x, y)
        return self.vertices
        
    def isCoordsOccupied(self, x, y):
        for v in self.vertices:
            coords = v.getCoords()
            if coords[0] >= x - 40 and coords[0] <= x + 40 and coords[1] >= y - 40 and coords[1] <= y + 40:
                return True
        return False
   
    
    def addEdge(self, v1, v2, weight = 1):
        if not isinstance(v1, Vertex) or not isinstance(v2, Vertex):
            raise TypeError('values must be a Vertex!')
        if v2 in v1.adjList:
            raise Exception('Edge already created!')
        v1._addEdge(v2, weight)
        
    def isAdj(self, v1, v2):
        for a in v1.adjList:
            if a[0] == v2:
                return True
        return False
    
    def deleteEdge(self, v1, v2):
        if not isinstance(v1, Vertex) or not isinstance(v2, Vertex):
            raise TypeError('values must be a Vertex!')
        if not self.isAdj(v1, v2):
            raise Exception('Vertex ' + str(v1.value) + ' does not have ' + str(v2.value) + ' edge')
        v1._deleteEdge(v2)
    
            
    #to count number of vertices in the graph
    def count_v(self):
        return len(self.vertices)
    
    #to delete the vertex from the graph        
    def deleteVertex(self, vertex):
        if not isinstance(vertex, Vertex):
            raise TypeError('value must be a Vertex!')
        if not vertex in self.vertices:
            raise ValueError('Vertex does not exist in graph')
        for e in self.vertices:
            e._deleteEdge(vertex)
        self.vertices.remove(vertex)
        return self.vertices
    
    # returns a string representation of the array
    def __repr__(self):	
        return str(self.vertices)
      
            
    def getVertexWithValue(self, value):
        for v in self.vertices:
            if v.value == value:
                return v
            

        
class UndirectedGraph(Graph):
    def __init__(self):
        super().__init__()
        
    def addEdge(self, v1, v2, weight = 1):
        if not isinstance(v1, Vertex) or not isinstance(v2, Vertex):
            raise TypeError('values must be a Vertex!')
        if v2 in v1.adjList:
            raise Exception('Edge already created!')
        v1._addEdge(v2, weight)
        v2._addEdge(v1, weight)
        
    def deleteEdge(self, v1, v2):
        if not isinstance(v1, Vertex) or not isinstance(v2, Vertex):
            raise TypeError('values must be a Vertex!')
        if not self.isAdj(v1, v2):
            raise Exception('Vertex ' + str(v1.value) + ' does not have ' + str(v2.value) + ' edge')
        v1._deleteEdge(v2)
        v2._deleteEdge(v1)
        
class TSPGraph(UndirectedGraph):
    def __init__(self):
        super().__init__()
        
    def addVertex(self, v, x, y):
        v.setCoords(x, y)
        if len(self.vertices) > 0:
            for u in self.vertices:
                self.addEdge(u, v)
        self.vertices.append(v)
    
    def addEdge(self, v1, v2):
        if not isinstance(v1, Vertex) or not isinstance(v2, Vertex):
            raise TypeError('values must be a Vertex!')
        if v2 in v1.adjList:
            raise Exception('Edge already created!')
        v1Coords = v1.getCoords()
        v2Coords = v2.getCoords()
        weight = ((v1Coords[0] - v2Coords[0]) ** 2 + (v1Coords[1] - v2Coords[1]) ** 2) ** 0.5
        v1._addEdge(v2, weight)
        v2._addEdge(v1, weight)
        
    def generateRandomNodes(self, num):
        for i in range(num):
            self.addVertex(i)
        for i in range(len(self.vertices) - 1):
            v1 = self.vertices[i]
            for j in range(i + 1, len(self.vertices)):
                v2 = self.vertices[j]
                self.addEdge(v1, v2)
            
        
class Vertex:
    
    def __init__(self, value, x = None, y = None):
        self.value = value 
        self.adjList = []
        self.setCoords(x, y)
		
    def getAdjList(self):
        return self.adjList

    #to add edge to this vertex
    def _addEdge(self, vertex, weight):
        if not isinstance(vertex, Vertex):
            raise TypeError("Value must be a Vertex!")
        if vertex == self:
            raise Exception("cannot add edge to itself")
        if vertex in self.adjList:
            raise Exception('Edge already exists')
        self.adjList.append([vertex, weight])
    
    def _deleteEdge(self, vertex):
        if not isinstance(vertex, Vertex):
            raise TypeError("Value must be a Vertex!")
        for i in range(len(self.adjList) - 1, -1, -1):
            if self.adjList[i][0] == vertex:
                self.adjList.pop(i)
    
    # return a string representation of the vertex
    def __repr__(self):
        return str(self.value)		
        
    def setCoords(self, x, y):
        self.x = x
        self.y = y
        
    def getCoords(self):
        return (self.x, self.y)
        
    def __eq__(self, other):
        return isinstance(other, Vertex) and self.value == other.value
        
    def __hash__(self):
        return hash(str(self.value))

        
def shortest_path(graph, initial, target):
    visited = {initial: 0}
    paths = {}
    nodes = set(graph.vertices)
    while len(nodes) > 0:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        if min_node == None:
            break
        nodes.remove(min_node)
        current_weight = visited[min_node]
        for node in min_node.adjList:
            weight = current_weight + node[1]
            if node[0] not in visited or weight < visited[node[0]]:
                visited[node[0]] = weight
                paths[node[0]] = min_node
    path = [target]
    next = target
    while next != initial:
        next = paths[next]
        path.append(next)
    return visited[target], path[::-1]
        
def dfs_traversal(v):
    q = Queue()
    g = Graph()
    visited = []
    _dfs(v, visited, g, q)
    
def _dfs(v, visited, g, q):
    setVisitedDfs(v, visited, g, q)
    for u in v.adjList:
        setVisitedDfs(u[0], visited, g, q)
    
def setVisitedDfs(v, visited, g, q):
    if v not in visited:
        visited.append(v)
        g.addVertex(v)
        print(v)
        q.put(v.value)
        _dfs(v, visited, g, q)
        
def bfs_traversal(v):
    q = Queue()
    g = Graph()
    visited = []
    queue = []
    setVisitedBfs(v, visited, queue, g, q)
    while len(queue) > 0:
        v = queue.pop(0)
        for u in v.adjList:
            setVisitedBfs(u[0], visited, queue, g, q)

def setVisitedBfs(v, visited, queue, g, q):
    if v not in visited:
        g.addVertex(v)
        print(v)
        visited.append(v)
        q.put(v.value)
        queue.append(v)
        
def topsort(graph):
    s = []
    visited = []
    for v in graph.vertices:
        if v not in visited:
            topsort_dfs(v, s, visited)
    return s[::-1]
    
def topsort_dfs(v, s, visited):
    visited.append(v)
    for u in v.adjList:
        if u[0] not in visited:
            topsort_dfs(u[0], s, visited)
    s.append(v)
    
def getMinDistNode(arr):      
    lowest = arr[0]
    for e in arr:
        if e[1] < lowest[1]:
            lowest = e
    return lowest
    
def retrieveVertex(g, vertex):
    for e in g.vertices:
        if e == vertex:
            return e 
    return None
    
def greedy1(g, initial):
    q = Queue()
    graph = copy.deepcopy(g)
    initial = retrieveVertex(graph, initial)
    path = [initial]
    q.put([initial])
    dist = 0
    graph.deleteVertex(initial)
    min = (initial, 0)
    while len(path) != len(g.vertices):
        min = getMinDistNode(min[0].adjList)
        graph.deleteVertex(min[0])
        path.append(min[0])
        dist += min[1]
        q.put(path + [])
    min = retrieveVertex(g, min[0])
    for e in min.adjList:
        if e[0] == initial:
            dist += e[1]
            break
    path.append(initial)
    return dist, path
    
def greedy2(g):
    q = Queue()
    graph = copy.deepcopy(g)
    
    # dictionary to store distances between any two points
    distance_dict = {}
    
    # stores the initial two nodes that are nearest to each other
    first = None
    second = None
    min_dist = 100000
    
    # handshake between all possible two points in the tour
    for node in g.vertices:
        for (neighbor, weight) in node.adjList:
            distance_dict[str(node)+str(neighbor)] = weight
            
            if weight < min_dist:
                min_dist = weight                
                first = node
                second = neighbor

    path = [first, second]
    dist = 0
    
    graph.deleteVertex(first)
    graph.deleteVertex(second)
    q.put(path[:])
    
    # while the path is not complete
    while len(path) != len(g.vertices):
        # variable to represent node with nearest distance from all nodes in the path
        nearest_in_path = None
        nearest_to_add = None
        
        # represents nearest distance
        nearest_dist = 1000000
        
        # for each vertice alr in the tour
        for vertice in path:
        
            # for each vertice that is not in the tour
            for neighbor in graph.vertices:
                
                # get distance between two points using the dictionary
                dist = distance_dict[str(vertice)+str(neighbor)] 
                    
                if dist < nearest_dist:
                    nearest_dist = dist
                    nearest_in_path = vertice
                    nearest_to_add = neighbor
        
        # get position of vertice in path that contains shortest distance
        curr_pos = path.index(nearest_in_path)    
        
        # choose where to insert the neighbor to the tour
        # e.g. path is A-B, A-C is the next shortest distance to add into the tour
        # compare between C-A-B and A-C-B
        if curr_pos == 0:
            next_in_path = path[curr_pos+1]
            
            # calculating distance of C-A-B
            d1 = nearest_dist + distance_dict[str(nearest_in_path) + str(next_in_path)]
           
            # calculating distance of A-C-B
            d2 = nearest_dist + distance_dict[str(nearest_to_add) + str(next_in_path)]
            
            # append C to the front of the tour
            if d1 < d2:
                path.insert(0,nearest_to_add)
            
            # append C after the first in the tour
            else:
                path.insert(1,nearest_to_add)
                
        # e.g. path is ...-X-Y, Y-Z is the next shortest distance to add into the tour
        # compare between X-Y-Z and X-Z-Y
        elif curr_pos == len(path) - 1:
            prev_in_path = path[curr_pos-1]
            
            # calculating distance of X-Y-Z
            d1 = distance_dict[str(prev_in_path) + str(nearest_in_path)] + nearest_dist
           
            # calculating distance of X-Z-Y
            d2 = distance_dict[str(prev_in_path) + str(nearest_to_add)] + nearest_dist
            
            # append Z to the back of the tour
            if d1 < d2:
                path.append(nearest_to_add)
            
            # append Z before the last in the tour
            else:
                path.insert(len(path)-1,nearest_to_add)
            
        # e.g. path is A-B-C, B-D is the next shortest distance to add into the tour
        # compare between A-D-B-C and A-B-D-C
        else:
            prev_in_path = path[curr_pos-1]
            next_in_path = path[curr_pos+1]
            
            # calculating distance of A-D-B-C
            d1 = distance_dict[str(prev_in_path) + str(nearest_to_add)] + nearest_dist + distance_dict[str(nearest_in_path) + str(next_in_path)]
           
            # calculating distance of A-B-D-C
            d2 = distance_dict[str(prev_in_path) + str(nearest_in_path)] + nearest_dist + distance_dict[str(nearest_to_add) + str(next_in_path)]
            
            # append D before B
            if d1 < d2:
                path.insert(curr_pos, nearest_to_add)
            
            # append D after B
            else:
                path.insert(curr_pos + 1,nearest_to_add) 
        
        # remove vertex from remaining vertexes to add
        graph.deleteVertex(nearest_to_add)
        q.put(path[:])
    # to make the path go back to its start
    path.append(path[0])
    
    total_dist = 0
    for i in range(len(path)-1):
        curr_v = path[i]
        next_v = path[i+1]
        
        # calculate total distance
        total_dist += distance_dict[str(curr_v) + str(next_v)]
        
        # put vertice in queue for visualization
                
    return total_dist, path
    
def two_opt(arr, g):
    q = Queue()
    q.put(arr)
    line_arr = generate_line_arr(arr)
    next_arr = resolve_lines(arr, line_arr)
    while next_arr != arr:
        arr = next_arr
        q.put(arr)
        line_arr = generate_line_arr(arr)
        next_arr = resolve_lines(arr, line_arr)
        line_arr = generate_line_arr(arr)
    q.put(arr)
    return next_arr
    
def resolve_lines(result, lineArr):
    for i in range(len(lineArr) - 2):
        for j in range(i + 2, len(lineArr)):
            if do_lines_intersect(lineArr[i], lineArr[j]):
                temp = result[:i + 1]
                temp += result[j:i : -1]
                temp += result[j + 1:]
                return temp 
    return result
      
      
def has_intersect_lines(lineArr):
    for i in range(0, len(lineArr) - 2):
        for j in range(i + 2, len(lineArr)):
            if do_lines_intersect(lineArr[i], lineArr[j]):
                return True
    return False

def generate_line_arr(result):
    lineArr = []
    for i in range(0, len(result) - 1):
        lineArr.append(Line(Point(v=result[i]), Point(v=result[i + 1])))
    return lineArr
  
class Point:
    def __init__(self, x = 0, y = 0, v = None):
        if v != None:
            self.x = v.x 
            self.y = v.y
        else:
            self.x = x
            self.y = y 
  
    def get_x(self):
        return self.x
  
    def get_y(self):
        return self.y 
  
    def __repr__(self):
        return '(' + str(self.x) + ', ' + str(self.y) + ')'
  
class Line:
    def __init__(self, p1, p2):
        self.point1 = p1
        self.point2 = p2 
  
    def get_first(self):
        return self.point1
  
    def get_second(self):
        return self.point2
  
    def __repr__(self):
        return 'p1: ' + str(self.point1) + ', p2: ' + str(self.point2)

def cross_product(a, b):
    return a.x * b.y - b.x * a.y

def is_point_on_line(line, point):
    tempLine = Line(Point(0, 0), Point(line.get_second().x - line.get_first().x, line.get_second().y - line.get_first().y))
    tempPoint = Point(point.x - line.get_first().x, point.y - line.get_first().y)
    r = cross_product(tempLine.get_second(), tempPoint)
    return abs(r) < 0.000001

def is_point_right_of_line(line, point): 
    tempLine = Line(Point(0, 0), Point(line.get_second().x - line.get_first().x, line.get_second().y - line.get_first().y));
    tempPoint = Point(point.x - line.get_first().x, point.y - line.get_first().y);
    return cross_product(tempLine.get_second(), tempPoint) < 0

def line_segment_touches_or_crosses_line(line1, line2):
    return (is_point_right_of_line(line1, line2.get_first()) ^ is_point_right_of_line(line1, line2.get_second()))

def do_lines_intersect(line1, line2):
    return line_segment_touches_or_crosses_line(line1, line2) and line_segment_touches_or_crosses_line(line2, line1)