from game.map import Map


def main():
    alive_cells = [(50, 50), (51, 50), (52, 50), (52, 51), (51, 52)]
    game_map = Map(alive_cells=alive_cells)
    game_map.initialize()
    game_map.play_turn()
    game_map.play_turn()
    game_map.play_turn()
    game_map.play_turn()


if __name__ == "__main__":
    main()
