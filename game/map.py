import time
from typing import List, Union

import numpy as np

from game.cell import Cell


class Map:
    def __init__(
        self,
        dimensions: tuple = (100, 100),
        alive_cells: List[tuple] = [()],
        n_turns: Union[int, np.inf] = np.inf,
    ) -> None:
        self.dimensions = dimensions
        self.alive_cells = alive_cells

    def initialize(self):
        """Initialize the map class with orders. Create these orders through several for loops."""
        # Initialize all cells
        for x in range(self.dimensions[0]):
            for y in range(self.dimensions[1]):
                self._create_dead_cell_i_j(x, y, is_alive=False)

        # Come to life all those first cells determined by the user
        for pos_x, pos_y in self.alive_cells:
            cell_i_j = getattr(self, f"cell_{pos_x}_{pos_y}")
            self._revive_cell(cell_i_j)

        # Match cells with neighbouring cells
        for x in range(self.dimensions[0]):
            for y in range(self.dimensions[1]):
                cell_i_j = getattr(self, f"cell_{x}_{y}")
                self._match_neighbouring_cells(cell_i_j)

    def play_turn(self):
        # Change temporary status
        for x in range(self.dimensions[0]):
            for y in range(self.dimensions[1]):
                cell_i_j = getattr(self, f"cell_{x}_{y}")
                cell_i_j._Cell__change_tmp_status()

        # Change real status
        for x in range(self.dimensions[0]):
            for y in range(self.dimensions[1]):
                cell_i_j = getattr(self, f"cell_{x}_{y}")
                cell_i_j._Cell__change_status()

        for x in range(self.dimensions[0]):
            for y in range(self.dimensions[1]):
                cell_i_j = getattr(self, f"cell_{x}_{y}")
                if cell_i_j.is_alive:
                    print(cell_i_j)
        time.sleep(2)
        print("\n")

    def _create_dead_cell_i_j(self, x, y, is_alive: bool = False) -> None:
        """Create a dynamic cell based on the position of the loops. Store it as an attribute.

        Args:
            x (int): Value of the first element in the position vector (x-axis).
            y (int): Value of the second element in the position vector (y-axis).
        """
        setattr(self, f"cell_{x}_{y}", Cell((x, y)))

    def _revive_cell(self, cell_i_j: Cell) -> None:
        cell_i_j._is_alive = True

    def _match_neighbouring_cells(self, cell_i_j):
        """Add neighboring cells to target cell. E.g., for cell in position (0, 0), add as neighbors
           cells like (0, 1), (0, -1), (1, -1)...

        Args:
            cell_i_j (Cell): Target cell.
        """
        for position, (pos_x, pos_y) in cell_i_j.pos_neighbors.items():
            try:
                cell_i_j.neighbors[position] = getattr(self, f"cell_{pos_x}_{pos_y}")
            except AttributeError:  # For when there is no neighbouring cell
                cell_i_j.neighbors[position] = None
