"""
Logging configuration for the Python Algorithms Study Program.

This module sets up loguru with a simple, clean format.
"""

import sys

from loguru import logger


def configure_logging(verbose=False):
    """Configure loguru with simple or verbose format based on verbose flag."""
    # Remove the default logger
    logger.remove()

    if verbose:
        # More detailed format with date, time and level
        format_string = (
            "<green>{time:YYYY-MM-DD HH:mm:ss}</green> | "
            "<level>{level: <8}</level> | "
            "{message}"
        )
        logger.add(
            sys.stderr,
            format=format_string,
            level="INFO",
            colorize=True,
        )
    else:
        # Very simple format - just the message
        logger.add(
            sys.stderr,
            format="{message}",
            level="INFO",
            colorize=False,
        )
