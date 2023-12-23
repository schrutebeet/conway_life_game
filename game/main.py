from game.map import Map
from game.gameui import GameUI

import click
import pandas as pd
from pathlib import Path
from typing import List, Tuple

@click.command()
@click.option('--start-cells', default='opt\stating_cells.csv', help='csv file with first cells alive. File must be called "stating_cells"')
@click.option('--map-dim', default=(100, 100), nargs=2, type=(int, int), help='X and Y values for the number of cells in each dimension.')
def main(start_cells, map_dim):
    alive_cells = pd.read_csv(Path(start_cells), index_col=False)
    alive_cells = convert_cells_to_list(alive_cells)
    game_map = Map(dimensions = map_dim, alive_cells=alive_cells)
    game_map.initialize()
    game_ui = GameUI(game_map)
    game_ui.run_game()
    
def convert_cells_to_list(cells_df: pd.DataFrame) -> List[Tuple[int, int]]:
    cell_list = [row for row in cells_df.itertuples(index=False, name=None)]
    return cell_list
    print(cell_list)


if __name__ == "__main__":
    main()
