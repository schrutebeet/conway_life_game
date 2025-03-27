# Conway's Game of Life :space_invader::video_game:

This project is a Python implementation of Conway's Game of Life, a cellular automaton devised by mathematician John Conway. The simulation is built using object-oriented programming principles and includes a graphical user interface for visualization.

## Rules of the Game
Any live cell with 2 or 3 live neighbors survives.
Any dead cell with exactly 3 live neighbors becomes a live cell.
All other live cells die in the next generation, and all other dead cells stay dead.


## Features

- **Cell Class**: Represents individual cells in the grid. Each cell can be alive or dead and interacts with its neighbors to determine its state in the next turn.
- **Map Class**: Manages the grid of cells, initializes the game state, and handles the rules of the simulation.
- **GameUI Class**: Provides a graphical interface using [PyGame](https://www.pygame.org/docs/) to visualize the simulation in real-time.


## Project Structure

```
game /
├── .gitignore               # Specifies intentionally untracked files to ignore
├── README.md                # Project documentation
├── poetry.lock              # Poetry lock file for dependencies
├── pyproject.toml           # Poetry configuration file
├── game/                    # Main game logic and implementation
│   ├── cell.py              # Defines the Cell class
│   ├── gameui.py            # Defines the GameUI class for visualization
│   ├── main.py              # Entry point for the application
│   ├── map.py               # Defines the Map class for managing the grid
│   └── __pycache__/         # Compiled Python files
├── game_venv/               # Virtual environment directory
│   ├── Include/
│   ├── Lib/
│   ├── Scripts/
│   └── pyvenv.cfg
└── opt/                     # Optional resources
    └── stating_cells.csv    # CSV file with initial alive cell positions
```

### Key Files

- **`game/main.py`**: Entry point for the application. It initializes the game map, reads the starting cells from a CSV file, and launches the graphical interface.
- **`game/cell.py`**: Defines the `Cell` class, which represents individual cells and their behavior.
- **`game/map.py`**: Defines the `Map` class, which manages the grid of cells and applies the rules of the game.
- **`game/gameui.py`**: Defines the `GameUI` class, which uses PyGame to render the simulation.
- **`opt/stating_cells.csv`**: A CSV file containing the initial positions of alive cells.

## Installation

1. Clone the repository:
   ```sh
   git clone <repository-url>
   cd conway_life_game
   ```

2. Install dependencies using Poetry:
   ```sh
   poetry install
   ```

3. Activate the virtual environment:
   ```sh
   poetry shell
   ```


## Usage
Run the game using the following command:
```sh
# Example
python main.py --start-cells stating_cells.csv --map-dim 100 100
```
- `--start-cells`: Path to the CSV file containing the initial alive cells. Default: opt/stating_cells.csv.
- `--map-dim`: Dimensions of the grid (X, Y). Default: (100, 100).


## Testing
Currently, no unit tests are implemented.


## Dependencies
- Python 3.11
- NumPy
- PyGame
- Click
- Pandas
