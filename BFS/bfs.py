class Vertex:
    def __init__(self, vertex):
        self.name = vertex
        self.distance = 9999
        self.neighbors = []
        self.color = 'black'

    def add_neighbor(self, neighbor_vertex):
        if neighbor_vertex not in self.neighbors:
            self.neighbors.append(neighbor_vertex)
            self.neighbors.sort()


class Graph:
    vertices = {}

    def add_vertex(self, vertex):
        if isinstance(vertex, Vertex) and vertex not in self.vertices:
            self.vertices[vertex.name] = vertex
            return True
        else:
            return False

    def add_edge(self, u, v):
        if u in self.vertices and v in self.vertices:
            for key, value in self.vertices.items():
                if key == u:
                    value.add_neighbor(v)
                if key == v:
                    value.add_neighbor(u)
            return True
        else:
            return False

    def print_graph(self):
        for key in sorted(list(self.vertices.keys())):
            print(key + "'s neighbors are " + str(self.vertices[key].neighbors)+ "and the distance from Root vertex is " + str(self.vertices[key].distance))

    # def bfs(self, root_vertex):
    #     queue = []
    #     root_vertex.distance = 0
    #     root_vertex.color = "red"
    #
    #     for neighbors in root_vertex.neighbors:
    #         self.vertices[neighbors].distance = root_vertex.distance + 1
    #         queue.append(neighbors)
    #
    #     while len(queue) > 0:
    #         u = queue.pop(0)
    #         node_u =

    def bfs(self, vert):
        q = list()
        vert.distance = 0
        vert.color = 'red'
        for v in vert.neighbors:
            self.vertices[v].distance = vert.distance + 1
            q.append(v)

        while len(q) > 0:
            u = q.pop(0)
            node_u = self.vertices[u]
            node_u.color = 'red'

            for v in node_u.neighbors:
                node_v = self.vertices[v]
                if node_v.color == 'black':
                    q.append(v)
                    if node_v.distance > node_u.distance + 1:
                        node_v.distance = node_u.distance + 1


g = Graph()
a = Vertex('A')
g.add_vertex(a)
g.add_vertex(Vertex('B'))
for i in range(ord('A'), ord('K')):
    g.add_vertex(Vertex(chr(i)))

edges = ['AB', 'AE', 'BF', 'CG', 'DE', 'DH', 'EH', 'FG', 'FI', 'FJ', 'GJ', 'HI']
for edge in edges:
    g.add_edge(edge[:1], edge[1:])

g.bfs(a)
g.print_graph()