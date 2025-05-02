import time
import pygame
def display_collision_effect(screen, width, height, effect_start_time):
    """Displays a fading border based on the score result."""
    elapsed_effect_time = (time.time() - effect_start_time) * 1000  # Convert to ms
    effect_duration = 500  # Effect lasts 500 millisecondsss

    if elapsed_effect_time > effect_duration:
        return  # Don't draw if the effect has expired

    # Determine color based on score
    
    color = (255, 0 , 0)

    # Calculate fade-out effect (opacity decrease)
    fade_factor = max(0, 1 - (elapsed_effect_time / effect_duration))
    alpha = int(255 * fade_factor)

    # Draw fading border
    border_thickness = 10
    border_surface = pygame.Surface((width, height), pygame.SRCALPHA)
    pygame.draw.rect(border_surface, (*color, alpha), (0, 0, width, height), border_thickness)
    screen.blit(border_surface, (0, 0))