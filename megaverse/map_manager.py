"""
This module provides the MapManager class to interact with the megaverse map API.

Classes:
    MapManager: Manages fetching and parsing of the goal map from the megaverse API.

Methods:
    __init__(self):
        Initializes the MapManager with base URL and candidate ID.

    fetch_goal_map(self):
        Fetches the goal map from the megaverse API.
        Returns:
            dict: The goal map data in JSON format.
        Raises:
            Exception: If the request to fetch the goal map fails.

    parse_goal_map(self, goal_map):
        Parses the goal map to extract instructions for creating elements.
        Args:
            goal_map (dict): The goal map data in JSON format.
        Returns:
            list: A list of instructions for creating elements in the format 
                  [("element_type", row_index, col_index, [optional] attribute)].
"""

import requests
from megaverse.constants import BASE_URL, CANDIDATE_ID

class MapManager:
    def __init__(self):
        self.base_url = BASE_URL
        self.candidate_id = CANDIDATE_ID

    def fetch_goal_map(self):
        url = f"{self.base_url}map/{self.candidate_id}/goal"
        response = requests.get(url)
        if response.status_code == 200:
            return response.json()
        raise Exception(f"Failed to fetch goal map. Status: {response.status_code}")

    def parse_goal_map(self, goal_map):
        instructions = []
        for row_index, row in enumerate(goal_map["goal"]):
            for col_index, cell in enumerate(row):
                if cell == "POLYANET":
                    instructions.append(("polyanet", row_index, col_index))
                elif cell.endswith("_SOLOON"):
                    color = cell.split("_")[0].lower()
                    instructions.append(("soloon", row_index, col_index, color))
                elif cell.endswith("_COMETH"):
                    direction = cell.split("_")[0].lower()
                    instructions.append(("cometh", row_index, col_index, direction))
        return instructions
