class Graph:
    def __init__(self, v):
        self.V = 0
        self.vertexes = []

    def add_vertex(self, vertex):
        self.V += 1
        self.vertexes.append(vertex)

    def add_edge(self, frm, to, cost):
        self.graph[frm, to] = cost

    def calculate(self):
        self.graph = [[float("inf") for column in range(self.V)] for rows in range(self.V)]

    def minDis(self, dist, shortestPath):
        mini = float("inf")
        for v in range(self.V):
            if dist[v] <  mini and shortestPath[v] == False:
                mini = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, org):
        dist = [float("inf") for i in range(self.V)]
        shortestPath = [float("inf") for i in range(self.V)]
        dist[org] = 0

        for cout in range(self.V):
            u = self.minDis(dist, shortestPath)

            shortestPath[u] = True
            for v in range(self.V):
                if self.graph[u][v] > 0 and shortestPath[v] == False and dist[v] > dist[u]+self.graph[u][v]:
                    dist[v] = dist[u]+self.graph[u][v]


