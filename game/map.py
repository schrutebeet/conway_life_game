from game.cell import Cell


class Map:
    def __init__(self, dimensions: tuple = (10, 10)) -> None:
        self.dimensions = dimensions

    def _relate_cells(self):
        for x in range(1, self.dimensions[0] + 1):
            for y in range(1, self.dimensions[1] + 1):
                self._create_cell_i_j(x, y)
                cell_i_j = getattr(self, f"cell_{x}_{y}")
                self._match_neighbouring_cells(cell_i_j)

    def _create_cell_i_j(self, x, y) -> None:
        setattr(self, f"cell_{x}_{y}", Cell((x, y)))

    def _match_neighbouring_cells(self, cell_i_j):
        for position, (pos_x, pos_y) in cell_i_j.pos_neighbors.items():
            try:
                cell_i_j.neighbors[position] = getattr(self, f"cell_{pos_x}_{pos_y}")
            except AttributeError:  # For when there is no neighbouring cell
                cell_i_j.neighbors[position] = None

    def initialize(self):
        self._relate_cells()


Map().initialize()
