import pygame
from .settings import TILE_SIZE
from .showscore import ShowScore

class World:

    def __init__(self, _grid_length_x, _grid_length_y, _width, _height, screen, clock):
        self.grid_length_x = _grid_length_x
        self.grid_length_y = _grid_length_y
        self.width = _width
        self.height = _height
        self.screen = screen
        self.clock = clock

        self.world = self.create_world()
        self.tiles = self.load_images()

        self.hero_pos = (9, 12)
        self.score = 0

    def create_world(self):
        world = []
        for x in range(self.grid_length_x):
            world.append([])
            for y in range(self.grid_length_y):
                world_tile = self.grid_to_world(x, y)
                world[x].append(world_tile)
        return world

    def grid_to_world(self, x, y):
        rect = [(x * TILE_SIZE, y * TILE_SIZE), (x * TILE_SIZE + TILE_SIZE, y * TILE_SIZE),
                (x * TILE_SIZE + TILE_SIZE, y * TILE_SIZE + TILE_SIZE), (x * TILE_SIZE, y * TILE_SIZE + TILE_SIZE)]

        isometric_poly = [self.cart_to_isometric(x, y) for x, y in rect]

        minx = min([x for x, y in isometric_poly])
        miny = min([y for x, y in isometric_poly])

        map_data = [[1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1],
                    [1, 2, 3, 0, 2, 2, 2, 1, 1, 1, 2, 1, 1, 1, 2, 2, 3, 1, 2, 2, 2, 1],
                    [1, 2, 1, 1, 2, 1, 2, 0, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 2, 1, 2, 1],
                    [1, 2, 1, 1, 2, 1, 2, 1, 1, 1, 0, 1, 1, 1, 2, 1, 1, 1, 0, 2, 2, 1],
                    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1],
                    [1, 2, 1, 1, 2, 1, 1, 1, 1, 0, 1, 0, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1],
                    [1, 2, 1, 1, 2, 2, 2, 1, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 2, 1, 2, 1],
                    [1, 2, 1, 1, 2, 1, 2, 1, 0, 1, 1, 1, 0, 1, 2, 1, 2, 1, 2, 1, 2, 1],
                    [1, 2, 2, 2, 2, 1, 2, 0, 0, 1, 7, 1, 0, 1, 2, 2, 2, 1, 2, 2, 2, 1],
                    [1, 1, 1, 2, 1, 1, 1, 1, 0, 8, 5, 1, 4, 1, 1, 1, 0, 1, 1, 2, 1, 1],
                    [1, 2, 2, 2, 2, 1, 2, 0, 0, 1, 6, 1, 0, 1, 2, 0, 0, 1, 2, 2, 2, 1],
                    [1, 2, 1, 1, 2, 1, 2, 0, 0, 1, 1, 1, 0, 1, 2, 1, 0, 1, 2, 1, 2, 1],
                    [1, 2, 1, 1, 2, 0, 2, 1, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 2, 1, 2, 1],
                    [1, 2, 1, 1, 2, 1, 1, 1, 1, 0, 1, 0, 1, 1, 2, 1, 2, 1, 1, 1, 2, 1],
                    [1, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 2, 1, 2, 1],
                    [1, 2, 1, 1, 2, 1, 2, 1, 1, 1, 0, 1, 1, 1, 2, 1, 1, 1, 0, 2, 2, 1],
                    [1, 2, 1, 1, 2, 1, 2, 0, 0, 0, 0, 0, 0, 0, 2, 1, 2, 2, 2, 1, 2, 1],
                    [1, 2, 3, 0, 2, 2, 2, 1, 1, 1, 2, 1, 1, 1, 0, 2, 3, 1, 2, 2, 2, 1],
                    [1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1]]

        tile = ""

        for row_nb, row in enumerate(map_data):
            for col_nb, tille in enumerate(row):
                if x == row_nb and y == col_nb:
                    if tille == 1:
                        tile = "wall"
                    if tille == 2:
                        tile = "seed"
                    if tille == 3:
                        tile = "elixir"
                    if tille == 4:
                        tile = "knight"
                    if tille == 5:
                        tile = "dragon_green"
                    if tille == 6:
                        tile = "dragon_yellow"
                    if tille == 7:
                        tile = "dragon_blue"
                    if tille == 8:
                        tile = "dragon_red"

        out = {"grid": [x, y], "cart_rect": rect, "isometric_poly": isometric_poly, "render_position": [minx, miny],
               "tile": tile}
        return out

    def cart_to_isometric(self, x, y):
        isometric_x = x - y
        isometric_y = (x + y) / 2
        return isometric_x, isometric_y

    def load_images(self):
        cube = pygame.image.load("assets/floor.png")
        wall = pygame.image.load("assets/floor.png")
        elixir = pygame.image.load("assets/elixir.png")
        seed = pygame.image.load("assets/seed.png")
        knight = pygame.image.load("assets/knight.png")
        dragon_green = pygame.image.load("assets/dragon_green.png")
        dragon_yellow = pygame.image.load("assets/dragon_yellow.png")
        dragon_blue = pygame.image.load("assets/dragon_blue.png")
        dragon_red = pygame.image.load("assets/dragon_red.png")

        # other object will be loaded here

        return {"cube": cube, "wall": wall, "elixir": elixir, "seed": seed, "knight": knight,
                "dragon_green": dragon_green, "dragon_yellow": dragon_yellow, "dragon_blue": dragon_blue,
                "dragon_red": dragon_red}

    def get_score(self):
        return self.score

    def move_hero(self, direction):
        next_pos = ()
        if direction == 1:
            if self.hero_pos[0] == 0 and [3, 10, 18].count(self.hero_pos[1]):
                next_pos = (18, self.hero_pos[1])
            elif self.hero_pos[0] == 0:
                return [False, 'wall']
            else:
                next_pos = (self.hero_pos[0] - 1, self.hero_pos[1])
        if direction == 2:
            if self.hero_pos[0] == 18 and [3, 10, 18].count(self.hero_pos[1]):
                next_pos = (0, self.hero_pos[1])
            elif self.hero_pos[0] == 18:
                return [False, 'wall']
            else:
                next_pos = (self.hero_pos[0] + 1, self.hero_pos[1])
        if direction == 4:
            if self.hero_pos[1] == 21:
                return [False, 'wall']
            next_pos = (self.hero_pos[0], self.hero_pos[1] + 1)
        if direction == 3:
            if self.hero_pos[1] == 0:
                return [False, 'wall']
            next_pos = (self.hero_pos[0], self.hero_pos[1] - 1)
        if ['dragon_green', 'dragon_yellow', 'dragon_blue', 'dragon_red'].count(
                self.world[next_pos[0]][next_pos[1]]["tile"]) != 0:
            showscore = ShowScore(self.screen, self.clock, self.score)
            showscore.run()
            return [False, 'died']
        if self.world[next_pos[0]][next_pos[1]]['tile'] == 'wall':
            return [False, 'wall']
        if self.world[next_pos[0]][next_pos[1]]["tile"] == 'seed':
            self.score += 1
            if self.score == 147:
                showscore = ShowScore(self.screen, self.clock, self.score)
                showscore.run()
        self.world[self.hero_pos[0]][self.hero_pos[1]]["tile"] = ''
        self.world[next_pos[0]][next_pos[1]]["tile"] = 'knight'
        self.hero_pos = next_pos
        return [True, 'ok']
