import config
vo_camera_offset = [0, 0]  # Still available if you want panning
vo_zoom = 10.0  # 2x zoom

def to_vo_screen_coords(x, y):
    global config
    return (
        int(config.vo_screen_center[0] + x * vo_zoom),
        int(config.vo_screen_center[1] - y * vo_zoom)
    )
