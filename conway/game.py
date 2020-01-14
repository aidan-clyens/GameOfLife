import pygame
import random


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
                board[y].append(random.randint(0, 1))

        return board

    def count_neighbours(self, x, y):
        count = 0

        if y > 0:
            if x > 0:
                count += self._board[y-1][x-1]
        
            count += self._board[y-1][x]

            if x < self._num_cols - 1:
                count += self._board[y-1][x+1]
        
        if y < self._num_rows - 1:
            if x > 0:
                count += self._board[y+1][x-1]
            
            count += self._board[y+1][x]
            
            if x < self._num_cols - 1:
                count += self._board[y+1][x+1]

        if x > 0:
            count += self._board[y][x-1]
        
        if x < self._num_cols - 1:
            count += self._board[y][x+1]
        
        return count

    def update(self):
        for y in range(0, self._num_rows):
            for x in range(0, self._num_cols):
                num = self.count_neighbours(x, y)

    def draw(self):
        self._screen.fill(BLACK)

        for y in range(0, self._num_rows):
            for x in range(0, self._num_cols):
                if self._board[y][x] == 1:
                    square = pygame.surface.Surface([self._grid_size, self._grid_size])
                    square.fill(WHITE)

                    self._screen.blit(square, [x * self._grid_size, y * self._grid_size])

        pygame.display.flip()
    
    def poll_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self._running = False
    
    def run(self):
        while self._running:
            self.poll_events()
            self.update()
            self.draw()

            self._clock.tick(60)
    
    def quit(self):
        pygame.quit()
