import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Circle as mplCircle, Polygon
from classes import Obstacle
import math
import config
import pygame
from to_vo_screen_coords import to_vo_screen_coords, vo_zoom
from test_velocity import test_velocity

def plot_everythingelse(circles, agent, surface):
    global config
    top_left = (-config.vx_max, config.vy_max)
    top_right = (config.vx_max, config.vy_max)
    bottom_right = (config.vx_max, -config.vy_max)
    bottom_left = (-config.vx_max, -config.vy_max)
    screen_top_left = to_vo_screen_coords(*top_left)
    screen_top_right = to_vo_screen_coords(*top_right)
    screen_bottom_right = to_vo_screen_coords(*bottom_right)
    screen_bottom_left = to_vo_screen_coords(*bottom_left)
   
    pygame.draw.lines(surface, (255, 255, 255), True, [
    screen_top_left,
    screen_top_right,
    screen_bottom_right,
    screen_bottom_left
    ], width=1)

    # Convert to screen space using your transformation


    # DEBUG: show test works for sample space 
    for vx in range(-config.vx_max, config.vx_max + 1 , 3):  # scale by 10 to handle floating points
        for vy in range(-config.vy_max, config.vy_max + 1, 3):
            if test_velocity(circles, [vx, vy], agent) is None:
                pygame.draw.circle(surface, (100, 255, 255), to_vo_screen_coords(vx, vy), 1)
            else:
                pygame.draw.circle(surface, (255, 0, 0), to_vo_screen_coords(vx, vy), 1)
    # Draw agent velocity
    font = pygame.font.SysFont(None, 24)
    vx, vy = agent.vx, agent.vy
    is_safe = test_velocity(circles, [vx, vy], agent)

    color = (0, 150, 0) if is_safe is None else (255, 150, 200)  # Dark green if safe, dark purple if not
    pygame.draw.circle(surface, color, to_vo_screen_coords(vx, vy), 3)

    velocity_text = f"Velocity: ({vx:.2f}, {vy:.2f})"
    if is_safe is not None:
        collision_text = f"Time Until Collision: {is_safe:.3f}s"
    else:
        collision_text = "Safe: No Collision"

    velocity_surf = font.render(velocity_text, True, (255, 255, 255))
    collision_surf = font.render(collision_text, True, (255, 255, 255))

    # calculate positions for top right corner (with padding)
    padding = 10
    screen_width = surface.get_width()
    velocity_pos = (screen_width - velocity_surf.get_width() - padding, padding)
    collision_pos = (screen_width - collision_surf.get_width() - padding, padding + velocity_surf.get_height() + 5)

    # blit to the surface
    surface.blit(velocity_surf, velocity_pos)
    surface.blit(collision_surf, collision_pos)

    
