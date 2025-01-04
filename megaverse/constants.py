"""
This module defines constants and loads environment variables for the Crossmint Challenge.

Modules:
    dotenv: A module to load environment variables from a .env file.
    os: A module to interact with the operating system.

Constants:
    BASE_URL (str): The base URL for the Crossmint Challenge API.
    CANDIDATE_ID (str): The candidate ID loaded from the environment variables.
    ENTITY_TYPES (dict): A dictionary mapping entity type names to their string representations.

Functions:
    load_dotenv(): Loads environment variables from a .env file.
"""

from dotenv import load_dotenv
import os

load_dotenv()

BASE_URL = "https://challenge.crossmint.io/api/"
CANDIDATE_ID = os.getenv("CANDIDATE_ID")
ENTITY_TYPES = {"POLYANET": "polyanet", "SOLOON": "soloon", "COMETH": "cometh"}
