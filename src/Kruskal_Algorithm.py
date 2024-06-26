class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = []

    def edge(self, u, v, w):
        self.graph.append([u, v, w])

    def search(self, parent, i):
        if parent[i] == i:
            return i
        return self.search(parent, parent[i])

    def union(self, parent, rank, x, y):
        x_root = self.search(parent, x)
        y_root = self.search(parent, y)

        if rank[x_root] < rank[y_root]:
            parent[x_root] = y_root
        elif rank[x_root] > rank[y_root]:
            parent[y_root] = x_root
        else:
            parent[y_root] = x_root
            rank[x_root] += 1

    def kruskal(self):
        result = []
        i, e = 0, 0

        self.graph = sorted(self.graph, key=lambda item: item[2])

        parent = []
        rank = []

        for node in range(self.V):
            parent.append(node)
            rank.append(0)

        while e < self.V - 1:
            u, v, w = self.graph[i]
            i += 1
            x = self.search(parent, u)
            y = self.search(parent, v)

            if x!= y:
                e += 1
                result.append([u, v, w])
                self.union(parent, rank, x, y)

        print("\nEdges:")
        for u, v, weight in result:
            print( u, v, end=" ")
            print("-", weight)
def main():
    g = Graph(5)
    x = int(0)
    y = int(0)
    z = int(0)
    v = int(input("Enter the number of edges: "))
    print("\nEnter the edges and vertices in this format \"x y z\"")
    for i in range(0, v):
        input_tuple = tuple(map(int, input().split()))
        x, y, z = input_tuple
        g.edge(x, y, z)
    g.kruskal()

if __name__ == "__main__":
    print("\tKruskal's Algorithm\n")
    main()