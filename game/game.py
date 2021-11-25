import pygame
import sys
from .world import World
from.settings import TILE_SIZE, FRAMERATE_DELAY

class Game:

    def __init__(self, _screen, _clock):
        self.screen = _screen
        self.clock = _clock
        self.width, self.height = self.screen.get_size()

        self.direction = 0
        # 0 - nowhere
        # 1 - up
        # 2 - down
        # 3 - right
        # 4 - left
        self.last_update = pygame.time.get_ticks()

        self.world = World(19, 22, self.width, self.height, self.screen, self.clock)

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
                elif event.key == pygame.K_a:
                    self.direction = 1
                elif event.key == pygame.K_d:
                    self.direction = 2
                elif event.key == pygame.K_w:
                    self.direction = 3
                elif event.key == pygame.K_s:
                    self.direction = 4

    def update(self):
        if pygame.time.get_ticks() - self.last_update >= FRAMERATE_DELAY and self.direction != 0:
            res = self.world.move_hero(self.direction)
            if not res[0]:
                self.direction = 0
                if res[1] == 'died':
                    pass
            self.last_update = pygame.time.get_ticks()

    def draw(self):
        self.screen.fill((255, 200, 100))

        for x in range(self.world.grid_length_x):
            for y in range(self.world.grid_length_y):

                square = self.world.world[x][y]["cart_rect"]
                rect = pygame.Rect(square[0][0], square[0][1], TILE_SIZE, TILE_SIZE)
                #pygame.draw.rect(self.screen, (0, 0, 255), rect, 1)

                render_position = self.world.world[x][y]["render_position"]
                self.screen.blit(self.world.tiles["cube"], (render_position[0] + self.width/2, render_position[1] + self.height/18))

                tile = self.world.world[x][y]["tile"]
                if tile != "":
                    if tile == "seed" or tile == "elixir" or tile == "dragon_red" or tile == "dragon_blue" or tile == "knight" or tile == "dragon_green" or tile == "dragon_yellow":
                        self.screen.blit(self.world.tiles[tile], (render_position[0] + self.width / 2,
                                                                  render_position[1] + self.height / 18 - (
                                                                              self.world.tiles[
                                                                                  tile].get_height() - TILE_SIZE + 16)))
                    else:
                        self.screen.blit(self.world.tiles[tile], (render_position[0] + self.width/2, render_position[1] + self.height/18 - (self.world.tiles[tile].get_height() - TILE_SIZE)))


                polygon = self.world.world[x][y]["isometric_poly"]
                polygon = [(x + self.width/2, y + self.height/18) for x, y in polygon]
                #pygame.draw.polygon(self.screen, (255, 0, 0), polygon, 1)

        self.screen.blit(pygame.font.SysFont('Arial', 25).render("Ваш результат: " + str(self.world.get_score()), True, (255, 0, 0)), (0, 0))

        pygame.display.flip()