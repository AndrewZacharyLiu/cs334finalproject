from classes import Circle
def update_positions(circles, dt):
    for circle in circles:
        circle.x += circle.vx * dt
        circle.y += circle.vy * dt