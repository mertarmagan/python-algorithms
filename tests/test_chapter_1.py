"""
Tests for Chapter 1: Basic Algorithms and Data Structures
"""

from python_algorithms import chapter_1


class TestChapter1:
    """Test class for Chapter 1 algorithms."""

    def test_bubble_sort(self):
        """Test bubble sort algorithm."""
        assert chapter_1.bubble_sort([3, 1, 4, 1, 5]) == [1, 1, 3, 4, 5]
        assert chapter_1.bubble_sort([]) == []
        assert chapter_1.bubble_sort([1]) == [1]
        assert chapter_1.bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

    def test_linear_search(self):
        """Test linear search algorithm."""
        assert chapter_1.linear_search([1, 2, 3, 4, 5], 3) == 2
        assert chapter_1.linear_search([1, 2, 3, 4, 5], 6) == -1
        assert chapter_1.linear_search([], 1) == -1
        assert chapter_1.linear_search([1], 1) == 0

    def test_binary_search(self):
        """Test binary search algorithm."""
        assert chapter_1.binary_search([1, 2, 3, 4, 5], 3) == 2
        assert chapter_1.binary_search([1, 2, 3, 4, 5], 6) == -1
        assert chapter_1.binary_search([], 1) == -1
        assert chapter_1.binary_search([1], 1) == 0

    def test_factorial(self):
        """Test factorial algorithm."""
        assert chapter_1.factorial(5) == 120
        assert chapter_1.factorial(0) == 1
        assert chapter_1.factorial(1) == 1
        assert chapter_1.factorial(3) == 6

    def test_fibonacci(self):
        """Test fibonacci algorithm."""
        assert chapter_1.fibonacci(6) == 8
        assert chapter_1.fibonacci(0) == 0
        assert chapter_1.fibonacci(1) == 1
        assert chapter_1.fibonacci(10) == 55
