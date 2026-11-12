from collections import deque


class Graph:
    def __init__(self):
        self.adj = {}

    def add_edge(self, u, v):
        self.adj.setdefault(u, []).append(v)
        self.adj.setdefault(v, []).append(u)

    def bfs(self, start):
        """Breadth-First Search: visit level by level using a queue."""
        visited, result = {start}, []
        queue = deque([start])
        while queue:
            v = queue.popleft()
            result.append(v)
            for nb in self.adj[v]:
                if nb not in visited:
                    visited.add(nb)
                    queue.append(nb)
        return result

    def dfs(self, v, visited=None, result=None):
        """Depth-First Search: go as deep as possible first (recursion)."""
        if visited is None:
            visited, result = set(), []
        visited.add(v)
        result.append(v)
        for nb in self.adj[v]:
            if nb not in visited:
                self.dfs(nb, visited, result)
        return result


if __name__ == "__main__":
    g = Graph()
    for u, v in [("V", "I"), ("V", "N"), ("V", "L"), ("I", "A"), ("I", "U"),
                 ("N", "L"), ("N", "E"), ("L", "U"), ("A", "E")]:
        g.add_edge(u, v)
    print("BFS:", " - ".join(g.bfs("V")))
    print("DFS:", " - ".join(g.dfs("V")))