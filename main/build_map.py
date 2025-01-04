"""
This script builds a map by creating entities based on instructions parsed from a goal map.

Modules:
    sys: Provides access to some variables used or maintained by the interpreter.
    os: Provides a way of using operating system dependent functionality.
    megaverse.map_manager: Contains the MapManager class for managing maps.
    megaverse.entity_manager: Contains the EntityManager class for managing entities.
    megaverse.utils: Contains utility functions, including setup_logger for logging.

Functions:
    setup_logger: Sets up and returns a logger instance.

Classes:
    MapManager: Manages the fetching and parsing of goal maps.
    EntityManager: Manages the creation of entities.

Exceptions:
    Exception: Catches all exceptions and logs an error message.

Usage:
    Run this script directly to start the map building process. The script will:
    1. Fetch and parse the goal map using MapManager.
    2. Create entities based on the parsed instructions using EntityManager.
    3. Log the progress and any errors encountered during the process.

"""

from megaverse.utils import setup_logger
from megaverse.entity_manager import EntityManager
from megaverse.map_manager import MapManager
import sys
import os

# Add the project root to PYTHONPATH
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))


logger = setup_logger()

if __name__ == "__main__":
    try:
        logger.info("Starting map building process.")
        map_manager = MapManager()
        entity_manager = EntityManager()

        # Fetch and parse the goal map
        goal_map = map_manager.fetch_goal_map()
        instructions = map_manager.parse_goal_map(goal_map)

        # Build the map by creating entities
        for instruction in instructions:
            if len(instruction) == 3:
                # The * in the create_entity method calls is used to unpack the instruction tuple into positional arguments.
                entity_manager.create_entity(*instruction)
            elif len(instruction) == 4:
                entity_manager.create_entity(*instruction)

        logger.info("Map building process completed.")
    except Exception as e:
        logger.error(f"An error occurred: {e}")
