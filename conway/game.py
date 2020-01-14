import pygame

BLACK = pygame.color.Color(0, 0, 0)
WHITE = pygame.color.Color(255, 255, 255)

class Game:
    def __init__(self, screen_size):
        pygame.init()

        self._screen_size = screen_size

        self._screen = pygame.display.set_mode(screen_size)
        self._clock = pygame.time.Clock()

        self._running = True

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
