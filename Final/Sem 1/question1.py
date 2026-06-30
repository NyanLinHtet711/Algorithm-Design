class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
    
    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]
    
    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x != root_y:
            self.parent[root_x] = root_y

def min_cost_to_build_lines(n, m, lines):
    lines.sort(key=lambda x: x[2])
    
    uf = UnionFind(n)
    
    min_cost = 0
    lines_built = 0
    
    # Kruskal's algorithm to find the MST
    for i in range(m):
        city1, city2, cost = lines[i]
        if uf.find(city1) != uf.find(city2):
            uf.union(city1, city2)
            min_cost += cost
            lines_built += 1
            if lines_built == n - 1:
                break
    
    return min_cost

# Input: Read the number of cities and number of lines
n, m = map(int, input().split())

# Read the high-speed lines information
lines = []
for _ in range(m):
    city1, city2, cost = map(int, input().split())
    lines.append((city1, city2, cost))

result = min_cost_to_build_lines(n, m, lines)
print(result)
