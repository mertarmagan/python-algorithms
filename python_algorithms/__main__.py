"""
Main entry point for the Python Algorithms Study Program.
"""

import sys

from loguru import logger

from . import chapter_1, chapter_2, chapter_3
from .cli import parser
from .logging_config import configure_logging

EXIT_SUCCESS = 0
EXIT_FAILURE = 1


def main():
    """Main function to run algorithm chapters."""
    # Parse arguments first to get verbose flag
    args = parser.parse_args()

    # Configure logging based on verbose flag
    configure_logging(verbose=getattr(args, "verbose", False))

    # Chapter modules mapping
    chapters = {
        1: ("Basic Algorithms and Data Structures", chapter_1),
        2: ("Advanced Sorting and Data Structures", chapter_2),
        3: ("Trees and Graph Algorithms", chapter_3),
    }

    if args.all:
        # Run all chapters
        logger.info("Running all chapters...")
        for chapter_num in sorted(chapters.keys()):
            chapter_name, chapter_module = chapters[chapter_num]
            logger.info(f"Running Chapter {chapter_num}: {chapter_name}")
            chapter_module.run()
            logger.info("=" * 60)
    elif args.chapter:
        # Run specific chapter
        if args.chapter in chapters:
            chapter_name, chapter_module = chapters[args.chapter]
            logger.info(f"Running Chapter {args.chapter}: {chapter_name}")
            chapter_module.run()
        else:
            logger.error(f"Chapter {args.chapter} not found!")
            return EXIT_FAILURE
    else:
        # Show help when no arguments provided
        parser.print_help()
        return EXIT_FAILURE

    return EXIT_SUCCESS


if __name__ == "__main__":
    sys.exit(main())
