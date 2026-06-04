# Disjoint Set (Union-Find) class
class DisjointSet:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [1] * n

    def find(self, u):
        if self.parent[u] != u:
            self.parent[u] = self.find(self.parent[u])
        return self.parent[u]

    def union(self, u, v):
        root_u = self.find(u)
        root_v = self.find(v)

        if root_u != root_v:
            # Union by rank
            if self.rank[root_u] > self.rank[root_v]:
                self.parent[root_v] = root_u
            elif self.rank[root_u] < self.rank[root_v]:
                self.parent[root_u] = root_v
            else:
                self.parent[root_v] = root_u
                self.rank[root_u] += 1

# Kruskal's algorithm to find the Minimum Spanning Tree (MST)
def kruskal_mst(n, edges):
    # Sort edges by weight
    edges.sort(key=lambda x: x[2])

    # Initialize Disjoint Set for Kruskal's algorithm
    ds = DisjointSet(n)
    mst_weight = 0
    mst_edges = 0

    # Process each edge in the sorted edge list
    for u, v, w in edges:
        # Check if the edge creates a cycle
        if ds.find(u) != ds.find(v):
            ds.union(u, v)
            mst_weight += w
            mst_edges += 1

            # If we've added n-1 edges, the MST is complete
            if mst_edges == n - 1:
                break

    return mst_weight

# Input reading
n, m = map(int, input().split())  # Number of taps (vertices) and pipes (edges)
edges = []

for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((u, v, w))

# Output the total weight of the MST
result = kruskal_mst(n, edges)
print(result)
