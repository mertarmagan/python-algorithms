"""
Tests for Chapter 3: Trees and Graph Algorithms
"""

from python_algorithms import chapter_3
from python_algorithms.chapter_3.algorithms import (
    create_sample_graph,
    create_sample_tree,
)


class TestChapter3:
    """Test class for Chapter 3 algorithms."""

    def test_binary_tree_traversal(self):
        """Test binary tree traversal algorithms."""
        tree = create_sample_tree()
        traversals = chapter_3.binary_tree_traversal(tree)

        assert traversals["inorder"] == [4, 2, 5, 1, 3]
        assert traversals["preorder"] == [1, 2, 4, 5, 3]
        assert traversals["postorder"] == [4, 5, 2, 3, 1]

    def test_graph_bfs(self):
        """Test breadth-first search algorithm."""
        graph = create_sample_graph()
        bfs_result = chapter_3.graph_bfs(graph, 0)

        # BFS should visit all nodes
        assert len(set(bfs_result)) == 5
        assert 0 in bfs_result
        assert bfs_result[0] == 0  # Should start with 0

    def test_graph_dfs(self):
        """Test depth-first search algorithm."""
        graph = create_sample_graph()
        dfs_result = chapter_3.graph_dfs(graph, 0)

        # DFS should visit all nodes
        assert len(set(dfs_result)) == 5
        assert 0 in dfs_result
        assert dfs_result[0] == 0  # Should start with 0

    def test_dijkstra_algorithm(self):
        """Test Dijkstra's shortest path algorithm."""
        from python_algorithms.chapter_3.algorithms import create_weighted_graph

        weighted_graph = create_weighted_graph()
        distances = chapter_3.dijkstra_algorithm(weighted_graph, "A")

        # Check that we get distances to all vertices
        expected_vertices = {"A", "B", "C", "D", "E"}
        assert set(distances.keys()) == expected_vertices

        # Distance to start should be 0
        assert distances["A"] == 0

        # Check some known shortest distances
        assert distances["C"] == 2  # Direct path A->C
        assert distances["B"] == 3  # A->C->B
