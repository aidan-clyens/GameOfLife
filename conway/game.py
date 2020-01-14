import pygame


BLACK = pygame.color.Color(0, 0, 0)
WHITE = pygame.color.Color(255, 255, 255)

class Game:
    def __init__(self, screen_size, grid_size):
        pygame.init()

        self._screen_size = screen_size
        self._grid_size = grid_size

        self._screen = pygame.display.set_mode(screen_size)
        self._clock = pygame.time.Clock()

        self._board = self.init_board()

        self._running = True

    def init_board(self):
        self._num_rows = int(self._screen_size[1] / self._grid_size) + 1
        self._num_cols = int(self._screen_size[0] / self._grid_size) + 1

        board = []
        for y in range(0, self._num_rows):
            board.append([])
            for x in range(0, self._num_cols):
                board[y].append(0)

        return board

    def draw(self):
        self._screen.fill(BLACK)
        pygame.display.flip()
    
    def poll_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
    
    def run(self):
        while self._running:
            self.poll_events()
            self.draw()

            self._clock.tick(60)
    
    def quit(self):
        pygame.quit()
