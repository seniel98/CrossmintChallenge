"""
This module provides the EntityManager class for managing entities in the Megaverse.

Classes:
    EntityManager: A class to handle creation and deletion of entities on a map.

Methods:
    __init__(): Initializes the EntityManager with base URL and candidate ID.
    create_entity(entity_type, row, column, attribute=None): Creates an entity of the specified type at the given position.
    clear_map(positions_to_clean): Clears specified positions on the map by deleting entities.

Attributes:
    base_url (str): The base URL for the API.
    candidate_id (str): The candidate ID for API requests.
"""


import requests
import time
from megaverse.constants import BASE_URL, CANDIDATE_ID, ENTITY_TYPES


class EntityManager:
    def __init__(self):
        self.base_url = BASE_URL
        self.candidate_id = CANDIDATE_ID

    def create_entity(self, entity_type, row, column, attribute=None):
        url = f"{self.base_url}{entity_type}s"
        payload = {"candidateId": self.candidate_id,
                   "row": row, "column": column}
        if attribute:
            payload["color" if entity_type ==
                    "soloon" else "direction"] = attribute

        for attempt in range(3):
            response = requests.post(url, json=payload)
            if response.status_code in (200, 201):
                return True
            if response.status_code == 429:
                time.sleep(2)
        return False

    def clear_map(self, positions_to_clean):
        for (row, column), entity_type in positions_to_clean.items():
            url = f"{self.base_url}{entity_type}s"
            payload = {"candidateId": self.candidate_id,
                       "row": row, "column": column}
            response = requests.delete(url, json=payload)
