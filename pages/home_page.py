from input import InputBox, Button
import config
import state
import pygame
import sys
running = True
def start_game():
    global running
    global state
    running = False
    state.state = state.GAME

def start_preset():
    global running
    global state
    running = False
    state.state = state.PRESET

def start_custom():
    global running
    global state
    running = False
    state.state = state.CUSTOM

def home_page(screen):
    global state
    global running
    global config
    background = pygame.image.load("assets/background.png").convert()
    background = pygame.transform.scale(background, (config.WIDTH, config.HEIGHT))

    running = True
    preset_button = Button(config.WIDTH // 2 - 100, config.HEIGHT // 2 - 100, 200, 60, "Presets",
                        lambda: start_preset())
    custom_button = Button(config.WIDTH // 2 - 100, config.HEIGHT // 2, 200, 60, "Customize",
                        lambda: start_custom())
    start_button = Button(config.WIDTH // 2 - 100, config.HEIGHT // 2 + 100 , 200, 60, "Start Simulation",
                        lambda: start_game())
    input_boxes = [preset_button, custom_button, start_button]
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
    