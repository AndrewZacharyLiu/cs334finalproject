import math
from classes import *
def handle_despawn(circles, despawn_radius):
    circles[:] = [
        c for c in circles
        if not (math.hypot(c.x, c.y) > despawn_radius and isinstance(c, Obstacle))
    ]