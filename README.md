# Conway's Game of Life
Project made to recreate Conway's game of life. The code contains three different classes:
- `Cell` class: Represents a cell object with different actions (methods). The cell can be set to alive or dead. It can also check its surroundings for life in other neighbouring cells.
- `Map` class: Map where all the cells are contained. The map is a 2-dimension canva where cells are piled up in the form of a grid.
- `GameUI` class: Intended for visualization purposes. This UI uses [PyGame](https://www.pygame.org/docs/) to visualize the different turns in the cell ecosystem. Cells alive are drawn in red.
