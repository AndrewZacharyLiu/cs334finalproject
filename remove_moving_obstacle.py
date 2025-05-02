import math
from classes import Obstacle
def remove_moving_obstacle(circles, epsilon=1e-5):
    circles[:] = [
        c for c in circles
        if not (isinstance(c, Obstacle) and math.hypot(c.vx, c.vy) > epsilon)
    ]
