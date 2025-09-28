"""
Chapter 1: Basic Algorithms and Data Structures
"""

from loguru import logger


def bubble_sort(arr):
    """Bubble sort algorithm implementation."""
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def linear_search(arr, target):
    """Linear search algorithm implementation."""
    for i, element in enumerate(arr):
        if element == target:
            return i
    return -1


def binary_search(arr, target):
    """Binary search algorithm implementation. Array must be sorted."""
    left, right = 0, len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return -1


def factorial(n):
    """Calculate factorial of n using recursion."""
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)


def fibonacci(n):
    """Calculate nth Fibonacci number."""
    if n <= 1:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


def run():
    """Run all algorithms in Chapter 1 with example data."""
    logger.info("=" * 50)
    logger.info("CHAPTER 1: Basic Algorithms and Data Structures")
    logger.info("=" * 50)

    # Bubble Sort Example
    logger.info("1. Bubble Sort:")
    test_arr = [64, 34, 25, 12, 22, 11, 90]
    logger.info(f"   Original array: {test_arr}")
    sorted_arr = bubble_sort(test_arr.copy())
    logger.info(f"   Sorted array: {sorted_arr}")

    # Linear Search Example
    logger.info("2. Linear Search:")
    search_arr = [2, 3, 4, 10, 40]
    target = 10
    result = linear_search(search_arr, target)
    logger.info(f"   Searching for {target} in {search_arr}")
    logger.info(
        f"   Result: {'Found at index ' + str(result) if result != -1 else 'Not found'}"
    )

    # Binary Search Example
    logger.info("3. Binary Search:")
    sorted_search_arr = [2, 3, 4, 10, 40]
    target = 10
    result = binary_search(sorted_search_arr, target)
    logger.info(f"   Searching for {target} in {sorted_search_arr}")
    logger.info(
        f"   Result: {'Found at index ' + str(result) if result != -1 else 'Not found'}"
    )

    # Factorial Example
    logger.info("4. Factorial:")
    n = 5
    result = factorial(n)
    logger.info(f"   Factorial of {n}: {result}")

    # Fibonacci Example
    logger.info("5. Fibonacci:")
    n = 10
    fib_sequence = [fibonacci(i) for i in range(n)]
    logger.info(f"   First {n} Fibonacci numbers: {fib_sequence}")
