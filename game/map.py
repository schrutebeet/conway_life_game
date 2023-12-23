from game.cell import Cell


class Map:
    def __init__(self, dimensions: tuple = (10, 10)) -> None:
        self.dimensions = dimensions

    def initialize(self):
        """Initialize the map class with orders. Create these orders through several for loops.
        """
        for x in range(1, self.dimensions[0] + 1):
            for y in range(1, self.dimensions[1] + 1):
                self._create_cell_i_j(x, y)
                cell_i_j = getattr(self, f"cell_{x}_{y}")
                self._match_neighbouring_cells(cell_i_j)

    def _create_cell_i_j(self, x, y) -> None:
        """Create a dynamic cell based on the position of the loops. Store it as an attribute.

        Args:
            x (int): Value of the first element in the position vector (x-axis).
            y (int): Value of the second element in the position vector (y-axis).
        """
        setattr(self, f"cell_{x}_{y}", Cell((x, y)))

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

Map().initialize()
