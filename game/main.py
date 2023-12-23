from game.map import Map

def main():
    game_map = Map(alive_cells=[(0, 0), (0, 1), (0, 2), (1, 0)])
    game_map.initialize()
    game_map.play_turn()
    game_map.play_turn()
    game_map.play_turn()
    game_map.play_turn()


if __name__=="__main__":
    main()