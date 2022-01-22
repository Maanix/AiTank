import pygame


class Player:

    def __init__(self, pos_x, pos_y):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.color = (255, 0, 0)
        self.step_size = 10
        self.size = 40

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, (self.pos_x, self.pos_y, self.size, self.size))

    def move_up(self):
        self.pos_y -= self.step_size

    def move_down(self):
        self.pos_y += self.step_size

    def move_left(self):
        self.pos_x -= self.step_size

    def move_right(self):
        self.pos_x += self.step_size
