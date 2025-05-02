import random
import math
from classes import Obstacle
import config
def generate_cage(circles, radius, num, escape_angle_width=math.pi/3):
    import config
    angle_step = 2 * math.pi / num
    c = math.sqrt(2 * radius**2 * (1 - math.cos(angle_step))) / 2

    escape_center = random.uniform(0, 2 * math.pi)
    escape_start = escape_center - escape_angle_width / 2
    escape_end = escape_center + escape_angle_width / 2
    for i in range(num):
        angle = angle_step * i
        norm_angle = angle % (2 * math.pi)

        # If this angle is within the escape range, skip placing a circle
        if escape_start <= norm_angle <= escape_end:
            #print("case1")
            continue
        elif escape_start < 0 and (norm_angle >= (escape_start + 2 * math.pi) or norm_angle <= escape_end):
            #print("case2")
            continue
        elif escape_end > 2 * math.pi and (norm_angle <= (escape_end % (2 * math.pi)) or norm_angle >= escape_start):
            #print("case3")
            continue
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        vx = -x / radius
        vy = -y / radius
        circles.append(Obstacle(x, y, vx * config.lowerVelocity, vy * config.lowerVelocity, c, collidable=False))

    