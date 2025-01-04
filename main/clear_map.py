"""
This script is responsible for clearing specified positions on a map in the Megaverse project.

Modules:
    sys: Provides access to some variables used or maintained by the interpreter.
    os: Provides a way of using operating system dependent functionality.
    megaverse.entity_manager: Contains the EntityManager class for managing entities on the map.
    megaverse.utils: Contains utility functions, including setup_logger for logging.

Functions:
    setup_logger: Sets up and returns a logger instance.

Execution:
    When executed, this script will:
    1. Log the start of the map clearing process.
    2. Instantiate the EntityManager.
    3. Define positions to clear on the map (example data).
    4. Clear the specified positions using the EntityManager.
    5. Log the completion of the map clearing process.
    6. Handle and log any exceptions that occur during the process.
"""

from megaverse.utils import setup_logger
from megaverse.entity_manager import EntityManager
import sys
import os

# Add the project root to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


logger = setup_logger()

if __name__ == "__main__":
    try:
        logger.info("Starting map clearing process.")
        entity_manager = EntityManager()

        # Define positions to clear (example data)
        positions_to_clean = {
            (2, 2): "polyanet",
            (3, 3): "soloon",
            (4, 4): "cometh"
        }

        # Clear specified positions
        entity_manager.clear_map(positions_to_clean)

        logger.info("Map clearing process completed.")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
