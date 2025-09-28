"""
Chapter 3: Trees and Graph Algorithms
"""

import heapq
from collections import defaultdict, deque


class TreeNode:
    """Binary Tree Node."""

    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Graph:
    """Graph representation using adjacency list."""

    def __init__(self):
        self.graph = defaultdict(list)

    def add_edge(self, u, v):
        """Add edge between vertices u and v."""
        self.graph[u].append(v)
        self.graph[v].append(u)  # For undirected graph

    def add_directed_edge(self, u, v):
        """Add directed edge from u to v."""
        self.graph[u].append(v)


def binary_tree_traversal(root):
    """Perform different tree traversals."""
    if not root:
        return {"inorder": [], "preorder": [], "postorder": []}

    def inorder(node, result):
        if node:
            inorder(node.left, result)
            result.append(node.val)
            inorder(node.right, result)

    def preorder(node, result):
        if node:
            result.append(node.val)
            preorder(node.left, result)
            preorder(node.right, result)

    def postorder(node, result):
        if node:
            postorder(node.left, result)
            postorder(node.right, result)
            result.append(node.val)

    inorder_result = []
    preorder_result = []
    postorder_result = []

    inorder(root, inorder_result)
    preorder(root, preorder_result)
    postorder(root, postorder_result)

    return {
        "inorder": inorder_result,
        "preorder": preorder_result,
        "postorder": postorder_result,
    }


def graph_bfs(graph, start):
    """Breadth-First Search traversal of graph."""
    visited = set()
    queue = deque([start])
    result = []

    visited.add(start)

    while queue:
        vertex = queue.popleft()
        result.append(vertex)

        for neighbor in graph.graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return result


def graph_dfs(graph, start):
    """Depth-First Search traversal of graph."""
    visited = set()
    result = []

    def dfs_helper(vertex):
        visited.add(vertex)
        result.append(vertex)

        for neighbor in graph.graph[vertex]:
            if neighbor not in visited:
                dfs_helper(neighbor)

    dfs_helper(start)
    return result


def dijkstra_algorithm(graph, start):
    """Dijkstra's algorithm for shortest paths."""
    distances = {vertex: float("infinity") for vertex in graph}
    distances[start] = 0
    priority_queue = [(0, start)]
    visited = set()

    while priority_queue:
        current_distance, current_vertex = heapq.heappop(priority_queue)

        if current_vertex in visited:
            continue

        visited.add(current_vertex)

        for neighbor, weight in graph[current_vertex]:
            distance = current_distance + weight

            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(priority_queue, (distance, neighbor))

    return distances


def create_sample_tree():
    """Create a sample binary tree for demonstration."""
    #       1
    #      / \
    #     2   3
    #    / \
    #   4   5

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    return root


def create_sample_graph():
    """Create a sample graph for demonstration."""
    graph = Graph()
    edges = [(0, 1), (0, 2), (1, 2), (2, 3), (3, 4)]

    for u, v in edges:
        graph.add_edge(u, v)

    return graph


def create_weighted_graph():
    """Create a sample weighted graph for Dijkstra's algorithm."""
    return {
        "A": [("B", 4), ("C", 2)],
        "B": [("A", 4), ("C", 1), ("D", 5)],
        "C": [("A", 2), ("B", 1), ("D", 8), ("E", 10)],
        "D": [("B", 5), ("C", 8), ("E", 2)],
        "E": [("C", 10), ("D", 2)],
    }


def run():
    """Run all algorithms in Chapter 3 with example data."""
    print("=" * 50)
    print("CHAPTER 3: Trees and Graph Algorithms")
    print("=" * 50)

    # Binary Tree Traversal
    print("\n1. Binary Tree Traversals:")
    tree = create_sample_tree()
    traversals = binary_tree_traversal(tree)
    print("   Tree structure:      1")
    print("                       / \\")
    print("                      2   3")
    print("                     / \\")
    print("                    4   5")
    print(f"   Inorder traversal:  {traversals['inorder']}")
    print(f"   Preorder traversal: {traversals['preorder']}")
    print(f"   Postorder traversal: {traversals['postorder']}")

    # Graph BFS and DFS
    print("\n2. Graph Traversals:")
    graph = create_sample_graph()
    print(f"   Graph edges: {[(u, list(graph.graph[u])) for u in graph.graph]}")

    bfs_result = graph_bfs(graph, 0)
    print(f"   BFS from vertex 0: {bfs_result}")

    dfs_result = graph_dfs(graph, 0)
    print(f"   DFS from vertex 0: {dfs_result}")

    # Dijkstra's Algorithm
    print("\n3. Dijkstra's Shortest Path Algorithm:")
    weighted_graph = create_weighted_graph()
    print(f"   Weighted graph: {dict(weighted_graph)}")

    distances = dijkstra_algorithm(weighted_graph, "A")
    print(f"   Shortest distances from A: {distances}")
