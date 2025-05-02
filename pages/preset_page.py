from input import InputBox, Button
import config
import state
import pygame
import sys

running = True
def asteroid():
    global running
    global state
    global config
    config.agent_radius = 15
    config.spawnRadius = 75
    config.despawnRadius = 120
    config.vx_max = 15
    config.vy_max = 15
    config.lowerVelocity = 7
    config.upperVelocity = 15
    config.lowerCircleRadius = 7
    config.upperCircleRadius = 15
    config.framesPerSpawn = 50
    config.boundaryRadius = 100
    config.obstacleMode = 0
    running = False
    state.state = state.HOME

def bullet():
    global running
    global state
    config.agent_radius = 15
    config.spawnRadius = 75
    config.despawnRadius = 120
    config.vx_max = 15
    config.vy_max = 15
    config.lowerVelocity = 30
    config.upperVelocity = 60
    config.lowerCircleRadius = 2
    config.upperCircleRadius = 2
    config.framesPerSpawn = 10
    config.boundaryRadius = 100
    config.obstacleMode = 0
    running = False
    state.state = state.HOME

def cagetrap():
    global running
    global state
    config.agent_radius = 3
    config.spawnRadius = 120
    config.despawnRadius = 125
    config.vx_max = 15
    config.vy_max = 15
    config.lowerVelocity = 20
    config.upperVelocity = 20
    config.framesPerSpawn = 275
    config.boundaryRadius = 130
    config.obstacleMode = 1
    running = False
    state.state = state.HOME

def bars():
    global running
    global state
    config.agent_radius = 20
    config.despawnRadius = 250
    config.vx_max = 15
    config.vy_max = 15
    config.lowerVelocity = 20
    config.upperVelocity = 20
    config.lowerCircleRadius = 2
    config.upperCircleRadius = 2
    config.framesPerSpawn = 250
    config.boundaryRadius = 150
    config.obstacleMode = 2
    running = False
    state.state = state.HOME

def death():
    global running
    global state
    config.agent_radius = 3
    config.spawnRadius = 120
    config.despawnRadius = 250
    config.vx_max = 15
    config.vy_max = 15
    config.lowerVelocity = 20
    config.upperVelocity = 20
    config.framesPerSpawn = 275
    config.boundaryRadius = 130
    config.obstacleMode = 3
    running = False
    state.state = state.HOME

def back_home():
    global running
    global state
    running = False
    state.state = state.HOME

def preset_page(screen):
    global state
    global running
    global config
    background = pygame.image.load("assets/background.png").convert()
    background = pygame.transform.scale(background, (config.WIDTH, config.HEIGHT))
    running = True
    asteroid_button = Button(config.WIDTH // 2 - 100, config.HEIGHT // 2 - 160, 200, 60, "Asteroid",
                        lambda: asteroid())
    bullet_button = Button(config.WIDTH // 2 - 100, config.HEIGHT // 2 - 80, 200, 60, "Bullet",
                        lambda: bullet())
    cagetrap_button = Button(config.WIDTH // 2 - 100, config.HEIGHT // 2, 200, 60, "Cage Escape",
                        lambda: cagetrap())
    bars_button = Button(config.WIDTH // 2 - 100, config.HEIGHT // 2 + 80 , 200, 60, "Bar Escape",
                        lambda: bars())
    death_button = Button(config.WIDTH // 2 - 100, config.HEIGHT // 2 + 160 , 200, 60, "Death",
                        lambda: death())
    back_button = Button(10, 10, 30, 30, "<-",
                        lambda: back_home())
    input_boxes = [asteroid_button, bullet_button, cagetrap_button, bars_button, death_button, back_button]

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
