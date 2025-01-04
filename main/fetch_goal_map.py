"""
This script fetches and displays the goal map using the MapManager class from the megaverse.map_manager module.

Modules:
    sys: Provides access to some variables used or maintained by the interpreter and to functions that interact strongly with the interpreter.
    os: Provides a way of using operating system dependent functionality like reading or writing to the file system.
    megaverse.map_manager: Contains the MapManager class which is used to manage maps.
    megaverse.utils: Contains utility functions including setup_logger for logging.

Functions:
    setup_logger: Sets up and returns a logger instance.

Execution:
    When executed as the main module, this script will:
    1. Log the start of the goal map fetching process.
    2. Create an instance of MapManager.
    3. Fetch the goal map using the MapManager instance.
    4. Log the fetched goal map.
    5. Handle and log any exceptions that occur during the process.
"""

from megaverse.utils import setup_logger
from megaverse.map_manager import MapManager
import sys
import os

# Add the project root to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


logger = setup_logger()

if __name__ == "__main__":
    try:
        logger.info("Fetching the goal map.")
        map_manager = MapManager()

        # Fetch and display the goal map
        goal_map = map_manager.fetch_goal_map()
        logger.info(f"Goal map: {goal_map}")

    except Exception as e:
        logger.error(f"An error occurred: {e}")
