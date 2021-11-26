import pygame


class Dragon:
    def __init__(self, color, pos):
        self.name = 'dragon_' + color
        self.position = pos
        self.last_state = ''

    def move(self, world, direction):
        new_pos = ()
        if direction == 'up':
            new_pos = (self.position[0] + 1, self.position[1])
        elif direction == 'down':
            new_pos = (self.position[0] - 1, self.position[1])
        elif direction == 'left':
            new_pos = (self.position[0], self.position[1] - 1)
        else:
            new_pos = (self.position[0], self.position[1] + 1)

        world[self.position[0]][self.position[1]]['tile'] = self.last_state
        self.last_state = world[new_pos[0]][new_pos[1]]['tile']
        world[new_pos[0]][new_pos[1]]['tile'] = self.name
        self.position = new_pos

    def iterate(self, world, hero):
        directions = []
        if self.position[0] != 0 and self.position[0] != 18:
            if ['seed', 'hero', '', 'knight', 'elixir'].count(world[self.position[0] + 1][self.position[1]]['tile']):
                directions.append('up')
            if ['seed', 'hero', '', 'knight', 'elixir'].count(world[self.position[0] - 1][self.position[1]]['tile']):
                directions.append('down')
        if self.position[1] != 0 and self.position[1] != 21:
            if ['seed', 'hero', '', 'knight', 'elixir'].count(world[self.position[0]][self.position[1] - 1]['tile']):
                directions.append('left')
            if ['seed', 'hero', '', 'knight', 'elixir'].count(world[self.position[0]][self.position[1] + 1]['tile']):
                directions.append('right')

        if self.position[0] < hero[0] and directions.count('up'):
            self.move(world, 'up')
        elif self.position[0] > hero[0] and directions.count('down'):
            self.move(world, 'down')
        elif self.position[1] > hero[1] and directions.count('left'):
            self.move(world, 'left')
        elif self.position[1] < hero[1] and directions.count('right'):
            self.move(world, 'right')
        elif len(directions):
            self.move(world, directions[0])

        if self.position[0] == hero[0] and self.position[1] == hero[1]:
            return True
        else:
            return False
