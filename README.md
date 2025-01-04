# Megaverse Builder (Crossmint Challenge)

## Overview

The **Megaverse Builder** project is part of the [Crossmint](https://www.crossmint.com/) Challenge. It automates the creation of astral objects (Polyanets, Soloons, and Comeths) based on a goal map fetched from the Megaverse API. This project provides tools to build, clear, and fetch maps programmatically, showcasing scalable and clean code practices.

## Directory Structure

```
megaverse_builder/
├── megaverse/               # Core modules and utilities
│   ├── __init__.py
│   ├── constants.py         # Constants (e.g., API base URL, entity types)
│   ├── entity_manager.py    # Entity creation, verification, and deletion
│   ├── map_manager.py       # Fetch and parse the goal map
│   ├── utils.py             # Logging setup and helper functions
├── main/                    # Main scripts for executing tasks
│   ├── build_map.py         # Script to build the map from the goal map
│   ├── clear_map.py         # Script to clear specific positions from the map
│   ├── fetch_goal_map.py    # Script to fetch and display the goal map
├── README.md                # Project documentation
└── requirements.txt         # Python dependencies
```

## Features

- **Fetch Goal Map**: Retrieve the goal map from the Megaverse API.
- **Build Map**: Create Polyanets, Soloons, and Comeths automatically based on the goal map.
- **Clear Map**: Delete specific entities programmatically.
- **Scalable and Modular Design**: Organized into reusable modules and scripts for extensibility.

## Prerequisites

Ensure you have the following installed:

- Python 3.8 or higher
- `pip` for managing Python packages

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Environment Variables

Create a `.env` file in the project root with your candidate ID:

```bash
CANDIDATE_ID=your_candidate_id_here
```

## Usage

### Fetch the Goal Map

Navigate to the project root and run:

```bash
python3 main/fetch_goal_map.py
```

### Build the Map

To build the map based on the goal map:

```bash
python3 main/build_map.py
```

### Clear Specific Entities

To clear specific entities, modify `positions_to_clean` in `main/clear_map.py` and run:

```bash
python3 main/clear_map.py
```

## Modules

### `megaverse/constants.py`

Defines constants such as API base URL, candidate ID, and entity types. [View the file](megaverse/constants.py)

### `megaverse/utils.py`

Provides utility functions like logging setup. [View the file](megaverse/utils.py)

### `megaverse/map_manager.py`

Handles fetching and parsing of the goal map. [View the file](megaverse/map_manager.py)

### `megaverse/entity_manager.py`

Manages creation, deletion, and verification of entities. [View the file](megaverse/entity_manager.py)

## Scripts

### `main/build_map.py`

Automates the creation of entities based on the goal map. [View the file](main/build_map.py)

### `main/clear_map.py`

Deletes specified entities from the map. [View the file](main/clear_map.py)

### `main/fetch_goal_map.py`

Fetches and displays the goal map for debugging or verification purposes. [View the file](main/fetch_goal_map.py)

Fetches and displays the goal map for debugging or verification purposes.

## Contributing

Contributions are welcome! Please fork the repository, create a feature branch, and submit a pull request.

## License

This project is licensed under the MIT License.

## Contact

For questions or support, contact:

- **Name**: José Daniel Padrón
- **Email**: [info@josedanielpadron.com](mailto:info@josedanielpadron.com)
