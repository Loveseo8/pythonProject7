import pygame
import sys

class ShowScore:

    def __init__(self, _screen, _clock, score):
        self.screen = _screen
        self.clock = _clock
        self.width, self.height = self.screen.get_size()
        self.score = score

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
        self.screen.fill((255, 200, 100))
        self.screen.blit(pygame.font.SysFont('Arial', 25).render("Ваш результат: " + str(self.score), True, (255, 0, 0)), (self.width // 2, self.height // 2))
        pygame.display.flip()