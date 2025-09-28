# Python Algorithms Study Project

A comprehensive collection of algorithm implementations organized by chapters for educational purposes. This project provides hands-on examples of fundamental algorithms and data structures in Python.

## 📚 Chapter Structure

### Chapter 1: Basic Algorithms and Data Structures
- **Sorting**: Bubble Sort
- **Searching**: Linear Search, Binary Search  
- **Recursion**: Factorial, Fibonacci
- **Complexity**: Basic time and space analysis

### Chapter 2: Advanced Sorting and Data Structures
- **Advanced Sorting**: Selection Sort, Insertion Sort, Merge Sort, Quick Sort
- **Data Structures**: Stack, Queue implementations
- **Performance**: Comparison of sorting algorithms

### Chapter 3: Trees and Graph Algorithms
- **Tree Traversals**: Inorder, Preorder, Postorder
- **Graph Algorithms**: BFS (Breadth-First Search), DFS (Depth-First Search)
- **Shortest Paths**: Dijkstra's Algorithm

## 🚀 Getting Started

### Prerequisites
- Python 3.13 or higher
- Poetry (for dependency management)

### Installation
```bash
# Clone the repository
git clone <your-repo-url>
cd python-algorithms

# Install dependencies using Poetry
poetry install

# Activate the virtual environment
poetry shell
```

## 🎮 Usage

### Command Line Options
```bash
# Run a specific chapter
python -m python_algorithms --chapter 1
python -m python_algorithms --chapter 2  
python -m python_algorithms --chapter 3

# Run all chapters
python -m python_algorithms --all

# Get help
python -m python_algorithms --help
```

### Running Tests
Verify that all algorithms work correctly using pytest:
```bash
# Install dev dependencies (including pytest)
poetry install --with dev

# Run all tests
poetry run pytest

# Run tests with verbose output
poetry run pytest -v

# Run specific test file (with verbose output)
poetry run pytest tests/test_chapter_1.py -v
```

### Code Quality & Pre-commit Hooks
This project uses pre-commit hooks to ensure code quality:

```bash
# Install pre-commit hooks (one-time setup)
poetry run pre-commit install

# Run hooks manually on all files
poetry run pre-commit run --all-files

# Run specific tools manually
poetry run black --check .
poetry run ruff check .
poetry run pytest
```

The pre-commit hooks will automatically run on every commit and check:
- **Code formatting** (Black)
- **Linting** (Ruff) 
- **Import sorting** (Ruff)
- **Basic file checks** (trailing whitespace, etc.)
- **All tests** (pytest)

## 🔧 Development

### Adding New Algorithms
1. Navigate to the appropriate chapter directory
2. Add your algorithm function to `algorithms.py`
3. Import and expose it in the chapter's `__init__.py`
4. Add example usage in the chapter's `run_chapter_X()` function
5. Add tests to the appropriate `tests/test_chapter_X.py` file

### Creating New Chapters
1. Create a new directory: `python_algorithms/chapter_X/`
2. Add `__init__.py` and `algorithms.py` files
3. Implement your algorithms in `algorithms.py`
4. Add the chapter import to `python_algorithms/__init__.py`
5. Update the main menu in `__main__.py`

## 🎯 Learning Goals

This project helps you understand:
- **Algorithm Design**: How different approaches solve the same problem
- **Time Complexity**: Big O notation and performance analysis
- **Data Structures**: When and why to use different structures
- **Implementation**: Converting pseudocode to working Python
- **Testing**: Verifying correctness with comprehensive tests

## 🤝 Contributing

Feel free to add new algorithms, improve existing implementations, or enhance documentation. Each algorithm should include:
- Clear docstrings with parameter and return descriptions
- Example usage in the chapter's run function
- Appropriate test cases

## 📖 Study Tips

1. **Start with Chapter 1** to build foundational understanding
2. **Run each algorithm** to see it in action with sample data
3. **Modify the examples** to test edge cases and different inputs
4. **Compare implementations** to understand trade-offs
5. **Add timing** to measure performance differences

Happy coding and learning! 🐍✨
