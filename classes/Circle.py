# circle.py
import pygame
import math
from world_to_screen import world_to_screen, game_zoom

class Circle:
    def __init__(self, x, y, vx, vy, radius, outline_color=(0, 0, 255), arrow_color=(0, 0, 0), collidable=True):
        self.x = x
        self.y = y
        self.vx = vx
        self.vy = vy
        self.radius = radius
        self.outline_color = outline_color
        self.arrow_color = arrow_color
        self.collidable = collidable

    def draw(self, surface):
        center_x, center_y = world_to_screen(self.x, self.y)
        pygame.draw.circle(surface, self.outline_color, (center_x, center_y), int(self.radius * game_zoom), 2)

        # Draw the velocity arrow
        arrow_scale = 0.5
        end_x = self.x + self.vx * arrow_scale
        end_y = self.y + self.vy * arrow_scale
        end_x, end_y = world_to_screen(self.x + self.vx * arrow_scale, self.y + self.vy * arrow_scale)
        pygame.draw.line(surface, self.arrow_color, (center_x, center_y), (end_x, end_y), 2)

