import config
camera_offset = [0, 0]  # Start at origin
game_zoom = 2.0
def world_to_screen(x, y):
    global config
    return (
        int(config.game_screen_center[0] + (x * game_zoom) - camera_offset[0] ),
        int(config.game_screen_center[1] - (y * game_zoom) + camera_offset[1])
    )
