"""
Tests for Chapter 2: Advanced Sorting and Data Structures
"""

from python_algorithms import chapter_2


class TestChapter2:
    """Test class for Chapter 2 algorithms."""

    def test_selection_sort(self):
        """Test selection sort algorithm."""
        test_array = [3, 1, 4, 1, 5, 9, 2, 6]
        expected = [1, 1, 2, 3, 4, 5, 6, 9]
        assert chapter_2.selection_sort(test_array.copy()) == expected
        assert chapter_2.selection_sort([]) == []
        assert chapter_2.selection_sort([1]) == [1]

    def test_insertion_sort(self):
        """Test insertion sort algorithm."""
        test_array = [3, 1, 4, 1, 5, 9, 2, 6]
        expected = [1, 1, 2, 3, 4, 5, 6, 9]
        assert chapter_2.insertion_sort(test_array.copy()) == expected
        assert chapter_2.insertion_sort([]) == []
        assert chapter_2.insertion_sort([1]) == [1]

    def test_merge_sort(self):
        """Test merge sort algorithm."""
        test_array = [3, 1, 4, 1, 5, 9, 2, 6]
        expected = [1, 1, 2, 3, 4, 5, 6, 9]
        assert chapter_2.merge_sort(test_array.copy()) == expected
        assert chapter_2.merge_sort([]) == []
        assert chapter_2.merge_sort([1]) == [1]

    def test_quick_sort(self):
        """Test quick sort algorithm."""
        test_array = [3, 1, 4, 1, 5, 9, 2, 6]
        expected = [1, 1, 2, 3, 4, 5, 6, 9]
        assert chapter_2.quick_sort(test_array.copy()) == expected
        assert chapter_2.quick_sort([]) == []
        assert chapter_2.quick_sort([1]) == [1]

    def test_stack_operations(self):
        """Test stack operations."""
        stack_ops = chapter_2.stack_example()
        assert len(stack_ops) == 10  # 5 push + 5 pop operations

        # Test individual stack operations
        stack = chapter_2.Stack()
        assert stack.is_empty()

        stack.push(1)
        stack.push(2)
        assert stack.size() == 2
        assert stack.peek() == 2
        assert stack.pop() == 2
        assert stack.size() == 1

    def test_queue_operations(self):
        """Test queue operations."""
        queue_ops = chapter_2.queue_example()
        assert len(queue_ops) == 10  # 5 enqueue + 5 dequeue operations

        # Test individual queue operations
        queue = chapter_2.Queue()
        assert queue.is_empty()

        queue.enqueue(1)
        queue.enqueue(2)
        assert queue.size() == 2
        assert queue.front() == 1
        assert queue.dequeue() == 1
        assert queue.size() == 1
