from game.map import Map
from game.gameui import GameUI


def main():
    alive_cells = [(101, 101), (102, 101), (103, 101), (103, 102), (102, 103)]
    game_map = Map(dimensions = (150, 150), alive_cells=alive_cells)
    game_map.initialize()
    game_ui = GameUI(game_map)
    game_ui.run_game()
    

if __name__ == "__main__":
    main()
