from collections import defaultdict
from dfs.dfsUtil import dfsUtil

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def union(self, parent, u, v):
        parent[u] = v

    def find_parent(self, parent, i):
        if parent[i] == -1:
            return i
        else:
            return self.find_parent(parent, parent[i])

    def connectedComponents(self):
        visited = [False] * (self.V)
        cc = []
        for v in range(self.V):
            if not visited[v] and v in self.graph:
                temp = []
                cc.append(dfsUtil.dfs(temp, v, self.graph, visited))
        return cc

    def unionFind(self):
        parent = [-1] * (self.V)
        for i in self.graph:
            for j in self.graph[i]:
                parent_i = self.find_parent(parent, i)
                parent_j = self.find_parent(parent, j)
                self.union(parent, parent_i, parent_j)
        return parent


if __name__ == '__main__':
    # Create a graph given in the above diagram
    g = Graph(5)
    g.addEdge(1, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 4)

    parent = g.unionFind()
    print(parent)
    for i in range(0, len(parent)):
        if parent[i] == -1:
            print("root node is ", i)

    cc = g.connectedComponents()
    print("Following are connected components")
    print(cc)
