import math
from classes import *

def generate_boundary(radius, num, circles):
    angle_step = 2 * math.pi / num
    c = math.sqrt(2 * radius**2 * (1 - math.cos(angle_step))) / 2

    for i in range(num):
        angle = angle_step * i
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        circles.append(Obstacle(x, y, 0, 0, c, collidable=False))