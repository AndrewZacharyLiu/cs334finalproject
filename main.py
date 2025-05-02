from classes import *
import pygame
import sys
from generate_boundary import generate_boundary
from generate_random_obstacle import generate_random_obstacle
from handle_collisions import handle_collisions
from handle_despawn import handle_despawn
from update_positions import update_positions
import config
from world_to_screen import camera_offset
from recalc_vos import recalc_vos
from plot_vos import plot_vos
from sample_velocities import sample_velocities
from pages import *
import state

pygame.init()

# Set up display
#WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((config.WIDTH, config.HEIGHT))
#screen_center = (WIDTH // 2, HEIGHT // 2)


pygame.display.set_caption("My Game")

# Set up clock for frame rate
while(True):
    #print("main loop hit top" + str(state.state))
    if (state.state == state.HOME):
        home_page(screen)
    elif (state.state == state.GAME):
        game_page(screen)
    elif (state.state == state.PRESET):
        preset_page(screen)
    elif (state.state == state.CUSTOM):
        customize_page(screen)
    else:
        break


# Main game loop
