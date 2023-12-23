class Cell:
    RELATIVE_DIRECTIONS = {
        "bottom_left": (-1, -1),
        "middle_left": (-1, 0),
        "top_left": (-1, 1),
        "middle_bottom": (0, -1),
        "middle_top": (0, 1),
        "bottom_right": (1, -1),
        "middle_right": (1, 0),
        "top_right": (1, 1),
    }

    def __init__(self, position: tuple = (0, 0)) -> None:
        self.position = position
        self._x = self.position[0]
        self._y = self.position[1]
        self._is_alive = False
        self._relative_directions = self.RELATIVE_DIRECTIONS
        self._pos_neighbors = self._calculate_neighbors()
        self.neighbors = {}

    def __str__(self) -> str:
        return f"Cell with position ({self._x}, {self._y})"

    def _calculate_neighbors(self):
        # Define the relative positions of neighbors
        neighbors = {}
        for position, (dx, dy) in self._relative_directions.items():
            neighbor_x, neighbor_y = self._x + dx, self._y + dy
            neighbors[position] = (neighbor_x, neighbor_y)
        return neighbors

    @property
    def is_alive(self):
        return self._is_alive

    @property
    def x(self):
        return self._x

    @property
    def y(self):
        return self._y

    @property
    def pos_neighbors(self):
        return self._pos_neighbors

    @property
    def relative_directions(self):
        return self._relative_directions
