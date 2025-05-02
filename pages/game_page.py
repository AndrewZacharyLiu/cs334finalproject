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
from plot_everythingelse import plot_everythingelse
from sample_velocities import sample_velocities
import PygameUtils as pu
from input import InputBox, Button
from display_collision_effect import display_collision_effect
from generate_cage import generate_cage
import state
import time
from remove_moving_obstacle import remove_moving_obstacle
from generate_bars import generate_bars
running = True
def back_home():
    global running
    global state
    running = False
    state.state = state.HOME

def game_page(screen):
    global state
    global running
    global config
    
    frame_count = 0
    collsion_effect_start_time = 0
    agent = Agent(0, 0, 0, 0, config.agent_radius)
    circles = []
    circles.append(agent)
    generate_boundary(config.boundaryRadius, 40 , circles)
    game_surface = screen.subsurface((0, 0, config.GAME_WIDTH, config.HEIGHT))
    vo_surface = screen.subsurface((config.GAME_WIDTH, 0, config.VO_WIDTH, config.HEIGHT))
    back_button = Button(10, 10, 30, 30, "<-",
                        lambda: back_home())
    running = True
    checkbox = pu.checkbox(
        color = (255,255,255),
        x=10,  # Will be repositioned later to top-right
        y=10,
        width = 20,
        height = 20,
        size = 20,
        check=True,
    )
    if (config.obstacleMode == 3):
        generate_bars(circles, config.lowerCircleRadius, config.agent_radius * 2 + 5, config.lowerVelocity+ 10)
        generate_bars(circles, config.lowerCircleRadius, config.agent_radius * 2 + 5, config.lowerVelocity + 10)
        generate_cage(circles, config.spawnRadius,40, escape_angle_width=0)
        

    while running:
        #dt = clock.tick(FPS) / 1000.0  # delta time in seconds
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            camera_offset[0] -= 2
        if keys[pygame.K_RIGHT]:
            camera_offset[0] += 2
        if keys[pygame.K_UP]:
            camera_offset[1] += 2
        if keys[pygame.K_DOWN]:
            camera_offset[1] -= 2

        # --- Event handling ---
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                # Clean up
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                if (checkbox.x <= (mouse_x - config.GAME_WIDTH) <= checkbox.x + checkbox.width and
                    checkbox.y <= mouse_y <= checkbox.y + checkbox.height):
                    checkbox.check = not checkbox.check  # Toggle on click
            back_button.handle_event(event)

        # --- Game logic updates ---
        # update game state here (positions, physics, etc)
        if frame_count % config.framesPerSpawn == 0:
            if config.obstacleMode == 0:
                generate_random_obstacle(circles, config.spawnRadius, config.lowerVelocity, config.upperVelocity, config.lowerCircleRadius, config.upperCircleRadius)
            elif config.obstacleMode == 1: # cage
                remove_moving_obstacle(circles)
                generate_cage(circles, config.spawnRadius,40)
            elif config.obstacleMode ==2: # bars
                generate_bars(circles, config.lowerCircleRadius, config.agent_radius * 2 + 5, config.lowerVelocity)



        agent_collided = handle_collisions(circles)
        if (agent_collided):
            collsion_effect_start_time = time.time()
        update_positions(circles, config.dt)
        handle_despawn(circles, config.despawnRadius)
        recalc_vos(circles, agent)
        if frame_count % 3 == 0:
            agent.vx, agent.vy = sample_velocities(circles, agent, config.vx_max, config.vy_max)

        # --- Drawing ---
        screen.fill((255, 255, 255))  # clear screen with white

        game_surface.fill((200, 200, 200))
        # draw everything here
        for circle in circles:
            circle.draw(game_surface)
        back_button.draw(game_surface)

        display_collision_effect(screen, config.GAME_WIDTH, config.HEIGHT, collsion_effect_start_time)
        # draw stuff for right hand side
        vo_surface.fill((50, 50, 50))  # white background
        if (checkbox.check):
            plot_vos(circles, agent, vo_surface)
        plot_everythingelse(circles, agent, vo_surface)
        checkbox.draw(vo_surface)
        font = pygame.font.SysFont(None, 18)
        label_surf = font.render("Display VO Approx", True, (255, 255, 255))
        vo_surface.blit(label_surf, (40, 10))
        pygame.display.flip()  # update the display
        frame_count += 1

