import pygame
import sys
from .world import World
from.settings import TILE_SIZE

class Game:

    def __init__(self, _screen, _clock):
        self.screen = _screen
        self.clock = _clock
        self.width, self.height = self.screen.get_size()

        self.world = World(19, 22, self.width, self.height)

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

        pygame.display.flip()
