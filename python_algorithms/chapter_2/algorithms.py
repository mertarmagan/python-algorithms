"""
Chapter 2: Advanced Sorting and Data Structures
"""

from collections import deque


def selection_sort(arr):
    """Selection sort algorithm implementation."""
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(arr):
    """Insertion sort algorithm implementation."""
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
    return arr


def merge_sort(arr):
    """Merge sort algorithm implementation."""
    if len(arr) <= 1:
        return arr

    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])

    return merge(left, right)


def merge(left, right):
    """Helper function for merge sort."""
    result = []
    i = j = 0

    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr):
    """Quick sort algorithm implementation."""
    if len(arr) <= 1:
        return arr

    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]

    return quick_sort(left) + middle + quick_sort(right)


class Stack:
    """Simple stack implementation using list."""

    def __init__(self):
        self.items = []

    def push(self, item):
        """Add item to top of stack."""
        self.items.append(item)

    def pop(self):
        """Remove and return top item from stack."""
        if not self.is_empty():
            return self.items.pop()
        raise IndexError("Stack is empty")

    def peek(self):
        """Return top item without removing it."""
        if not self.is_empty():
            return self.items[-1]
        raise IndexError("Stack is empty")

    def is_empty(self):
        """Check if stack is empty."""
        return len(self.items) == 0

    def size(self):
        """Return size of stack."""
        return len(self.items)


class Queue:
    """Simple queue implementation using deque."""

    def __init__(self):
        self.items = deque()

    def enqueue(self, item):
        """Add item to rear of queue."""
        self.items.append(item)

    def dequeue(self):
        """Remove and return item from front of queue."""
        if not self.is_empty():
            return self.items.popleft()
        raise IndexError("Queue is empty")

    def front(self):
        """Return front item without removing it."""
        if not self.is_empty():
            return self.items[0]
        raise IndexError("Queue is empty")

    def is_empty(self):
        """Check if queue is empty."""
        return len(self.items) == 0

    def size(self):
        """Return size of queue."""
        return len(self.items)


def stack_example():
    """Demonstrate stack operations."""
    stack = Stack()
    operations = []

    # Push operations
    for item in [1, 2, 3, 4, 5]:
        stack.push(item)
        operations.append(f"Push {item}, stack: {stack.items}")

    # Pop operations
    while not stack.is_empty():
        popped = stack.pop()
        operations.append(f"Pop {popped}, stack: {stack.items}")

    return operations


def queue_example():
    """Demonstrate queue operations."""
    queue = Queue()
    operations = []

    # Enqueue operations
    for item in [1, 2, 3, 4, 5]:
        queue.enqueue(item)
        operations.append(f"Enqueue {item}, queue: {list(queue.items)}")

    # Dequeue operations
    while not queue.is_empty():
        dequeued = queue.dequeue()
        operations.append(f"Dequeue {dequeued}, queue: {list(queue.items)}")

    return operations


def run():
    """Run all algorithms in Chapter 2 with example data."""
    print("=" * 60)
    print("CHAPTER 2: Advanced Sorting and Data Structures")
    print("=" * 60)

    # Test array for sorting algorithms
    test_arr = [64, 34, 25, 12, 22, 11, 90]

    # Selection Sort
    print("\n1. Selection Sort:")
    print(f"   Original: {test_arr}")
    print(f"   Sorted: {selection_sort(test_arr.copy())}")

    # Insertion Sort
    print("\n2. Insertion Sort:")
    print(f"   Original: {test_arr}")
    print(f"   Sorted: {insertion_sort(test_arr.copy())}")

    # Merge Sort
    print("\n3. Merge Sort:")
    print(f"   Original: {test_arr}")
    print(f"   Sorted: {merge_sort(test_arr.copy())}")

    # Quick Sort
    print("\n4. Quick Sort:")
    print(f"   Original: {test_arr}")
    print(f"   Sorted: {quick_sort(test_arr.copy())}")

    # Stack Example
    print("\n5. Stack Operations:")
    stack_ops = stack_example()
    for op in stack_ops:
        print(f"   {op}")

    # Queue Example
    print("\n6. Queue Operations:")
    queue_ops = queue_example()
    for op in queue_ops:
        print(f"   {op}")
