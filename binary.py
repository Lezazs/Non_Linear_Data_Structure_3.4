from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        """Insert level by level, left to right."""
        new_node = Node(data)
        if self.root is None:
            self.root = new_node
            return
        queue = deque([self.root])
        while queue:
            node = queue.popleft()
            if node.left is None:
                node.left = new_node
                return
            if node.right is None:
                node.right = new_node
                return
            queue.append(node.left)
            queue.append(node.right)

    def bfs(self):
        """Breadth-First Search: visit level by level using a queue."""
        result, queue = [], deque([self.root] if self.root else [])
        while queue:
            node = queue.popleft()
            result.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        return result

    def dfs(self, node="start", result=None):
        """Depth-First Search: go as deep as possible first (recursion)."""
        if node == "start":
            node, result = self.root, []
        if node:
            result.append(node.data)
            self.dfs(node.left, result)
            self.dfs(node.right, result)
        return result


if __name__ == "__main__":
    tree = BinaryTree()
    for letter in "VILANUE":
        tree.insert(letter)
    print("BFS:", " - ".join(tree.bfs()))
    print("DFS:", " - ".join(tree.dfs()))