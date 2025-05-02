from input import InputBox, Button
import config
import state
import pygame
import sys

running = True


def submit(agent_radius_input,spawn_input,despawn_input, vx_max_input, vy_max_input, obstacle_lower_velocity_input, obstacle_upper_velocity_input, obstacle_lower_radius_input, obstacle_upper_radius_input, frames_per_spawn_input, boundary_radius_input):
    global running
    global state
    global config
    config.agent_radius = int(agent_radius_input.text)
    config.spawnRadius = int(spawn_input.text)
    config.despawnRadius = int(despawn_input.text)
    config.vx_max = int(vx_max_input.text)
    config.vy_max = int(vy_max_input.text)
    config.lowerVelocity = int(obstacle_lower_velocity_input.text)
    config.upperVelocity = int(obstacle_upper_velocity_input.text)
    config.lowerCircleRadius = int(obstacle_lower_radius_input.text)
    config.upperCircleRadius = int(obstacle_upper_radius_input.text)
    config.framesPerSpawn = int(frames_per_spawn_input.text)
    config.boundaryRadius = int(boundary_radius_input.text)
    config.obstacleMode = 0
    running = False
    state.state = state.HOME
def back_home():
    global running
    global state
    running = False
    state.state = state.HOME

def customize_page(screen):
    global state
    global running
    global config
    background = pygame.image.load("assets/background.png").convert()
    background = pygame.transform.scale(background, (config.WIDTH, config.HEIGHT))
    running = True
    agent_radius_input = InputBox(config.WIDTH // 2 - 100, config.HEIGHT // 2 -240, 200, 30, "agent radius")
    spawn_input = InputBox(config.WIDTH // 2 - 100, config.HEIGHT // 2 -200, 200, 30, "spawn radius")
    despawn_input = InputBox(config.WIDTH // 2 - 100, config.HEIGHT // 2 -160, 200, 30, "despawn radius")
    vx_max_input = InputBox(config.WIDTH // 2 - 100, config.HEIGHT // 2 -120, 200, 30, "agent speed x max")
    vy_max_input = InputBox(config.WIDTH // 2 - 100, config.HEIGHT // 2 -80, 200, 30, "agent speed y max")
    obstacle_lower_velocity_input = InputBox(config.WIDTH // 2 - 100, config.HEIGHT // 2 - 40, 200, 30, "obstacle min speed")
    
    obstacle_upper_velocity_input = InputBox(config.WIDTH // 2 - 100, config.HEIGHT // 2, 200, 30, "obstacle max speed")
    
    obstacle_lower_radius_input = InputBox(config.WIDTH // 2 - 100, config.HEIGHT // 2 +40, 200, 30, "obstacle min radius")
    obstacle_upper_radius_input = InputBox(config.WIDTH // 2 - 100, config.HEIGHT // 2 + 80, 200, 30, "obstacle max radius")
    frames_per_spawn_input = InputBox(config.WIDTH // 2 - 100, config.HEIGHT // 2 + 120, 200, 30, "frames per spawn")
    boundary_radius_input = InputBox(config.WIDTH // 2 - 100, config.HEIGHT // 2 + 160, 200, 30, "boundary radius")
    submit_button = Button(config.WIDTH // 2 - 100, config.HEIGHT // 2 + 200, 200, 60, "Submit",
                        lambda: submit(agent_radius_input, spawn_input,despawn_input, vx_max_input, vy_max_input, obstacle_lower_velocity_input, obstacle_upper_velocity_input, obstacle_lower_radius_input, obstacle_upper_radius_input, frames_per_spawn_input, boundary_radius_input))
    
    back_button = Button(10, 10, 30, 30, "<-",
                        lambda: back_home())
    input_boxes = [agent_radius_input, spawn_input,despawn_input, vx_max_input, vy_max_input, obstacle_lower_velocity_input, obstacle_upper_velocity_input, obstacle_lower_radius_input, obstacle_upper_radius_input, frames_per_spawn_input, boundary_radius_input, submit_button, back_button]

    while running:
        screen.blit(background, (0, 0))
        for box in input_boxes:
            box.draw(screen)


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sys.exit()
            for box in input_boxes:
                box.handle_event(event)
        pygame.display.flip()
