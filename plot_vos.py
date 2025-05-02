import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle as mplCircle, Polygon
from classes import Obstacle
import math
import pygame
from to_vo_screen_coords import to_vo_screen_coords, vo_zoom

def plot_vos(circles, agent, surface):

    for circle in circles:
        if not isinstance(circle, Obstacle):
            continue

        vo = circle.velocity_obstacle
        theta = vo['theta']
        beta = vo['beta']
        time_radius = vo['time_horizon_radius']
        outer_radius = 100

        if outer_radius < time_radius + 1:
            continue

        angles = [theta - beta + 2 * beta * i / 24 for i in range(25)]
        x_outer = [outer_radius * math.cos(a) for a in angles]
        y_outer = [outer_radius * math.sin(a) for a in angles]

        x_inner = [time_radius * math.cos(a) for a in reversed(angles)]
        y_inner = [time_radius * math.sin(a) for a in reversed(angles)]

        polygon_points = list(zip(x_inner + x_outer, y_inner + y_outer))
        polygon_points = [to_vo_screen_coords(x + circle.vx, y + circle.vy) for x, y in polygon_points]

        pygame.draw.polygon(surface, (200, 0, 0), polygon_points)  # red VO cone



    
