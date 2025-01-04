"""
This module provides utility functions for the CrossmintChallenge project.

Functions:
    setup_logger: Configures and returns a logger instance with INFO level and a specific format.
"""

import logging


def setup_logger():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - %(levelname)s - %(message)s")
    return logging.getLogger()
