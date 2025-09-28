"""
Command Line Interface argument parsing for Python Algorithms Study Program.
"""

import argparse

# Define the argument parser at module level
parser = argparse.ArgumentParser(
    description="Python Algorithms Study Program",
    formatter_class=argparse.RawDescriptionHelpFormatter,
    epilog="""
Examples:
  python -m python_algorithms --chapter 1
  python -m python_algorithms --chapter 2
  python -m python_algorithms --all
  python -m python_algorithms --chapter 1 --verbose
    """,
)

parser.add_argument(
    "--chapter",
    "-c",
    type=int,
    choices=[1, 2, 3],
    help="Run specific chapter (1, 2, or 3)",
)

parser.add_argument(
    "--all",
    "-a",
    action="store_true",
    help="Run all chapters",
)

parser.add_argument(
    "--verbose",
    "-v",
    action="store_true",
    help="Enable detailed logging with timestamps",
)
