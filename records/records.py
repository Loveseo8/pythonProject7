import pygame
import sys

bg = pygame.image.load("assets/Packman_main_menu2.png")

class Records:


    def __init__(self, _screen, _clock):
        self.screen = _screen
        self.clock = _clock

    def run(self):
        self.playing = True
        while self.playing:
            self.clock.tick(60)
            self.events()
            self.update()
            self.draw()

    def events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()

    def update(self):
        pass

    def draw(self):
        self.screen.fill((0, 0, 0))
        self.screen.blit(bg, (0, 0))
        pygame.display.flip()