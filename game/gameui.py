import pygame

from game.map import Map

class GameUI:

    def __init__(self, game_map: Map, dimensions: tuple = (900, 900)) -> None:
        pygame.init()
        self.running = True
        self.fps = 5
        self.clock = pygame.time.Clock()
        self.game_map = game_map
        self.height= dimensions[0]
        self.width= dimensions[1]
        self.square_height = self.height / self.game_map.dimensions[0]
        self.square_width = self.width / self.game_map.dimensions[1]
        self.alive_color = (250, 0, 0)  # Red
        self.dead_color = (255, 255, 255)  # White
        self.background_color = (255, 255, 255)  # White
        self.screen = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Conway's Game of Life")
    
    def run_game(self) -> None:
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Fill background
            self.screen.fill(self.background_color)

            # Play one turn and get cells alive
            cells_alive = self.game_map.play_turn()
            for cell in cells_alive:
                start_value_x = cell.x * self.square_width  # Starting from the left-most side in the UI
                start_value_y = (self.game_map.dimension_y - cell.y) * self.square_height  # Starting from top-most side in UI, that is why we subtract "dimension_y"
                pygame.draw.rect(self.screen, self.alive_color, 
                                 (start_value_x, start_value_y, self.square_width, self.square_height))

            pygame.display.update()
            self.clock.tick(self.fps)

    def quit_pygame(self) -> None:
        pygame.quit()

