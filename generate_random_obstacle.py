import random
import math
from classes import Obstacle

def generate_random_obstacle(circles, spawn_radius, lower_velocity, upper_velocity, lower_circle_radius, upper_circle_radius):
    max_tries = 2

    for _ in range(max_tries):
        angle1 = 2 * math.pi * random.random()
        angle2 = 2 * math.pi * random.random()

        start_x = spawn_radius * math.cos(angle1)
        start_y = spawn_radius * math.sin(angle1)
        velocity = lower_velocity + (upper_velocity - lower_velocity) * random.random()
        vx = velocity * math.cos(angle2)
        vy = velocity * math.sin(angle2)
        new_radius = lower_circle_radius + (upper_circle_radius - lower_circle_radius) * random.random()

        overlaps = False
        for circle in circles:
            dx = circle.x - start_x
            dy = circle.y - start_y
            dist = math.sqrt(dx**2 + dy**2)
            if dist < (circle.radius + new_radius):
                overlaps = True
                break

        if not overlaps:
            new_circle = Obstacle(start_x, start_y, vx, vy, new_radius, collidable=True)
            circles.append(new_circle)
            return True

    return False
