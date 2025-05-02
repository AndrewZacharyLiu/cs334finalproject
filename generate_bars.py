from classes import Obstacle
import random
def left_bars(circles, radius, gap, speed, x, top, bottom):
    y = top + random.uniform(-gap / 2, gap / 2)
    step = 2 * radius + gap
    while y <= bottom:
        circles.append(Obstacle(x, y, speed, 0, radius, collidable=False))
        y += step

def right_bars(circles, radius, gap, speed, x, top, bottom):
    y = top + random.uniform(-gap / 2, gap / 2)
    step = 2 * radius + gap
    while y <= bottom:
        circles.append(Obstacle(x, y, -speed, 0, radius, collidable=False))
        y += step

def top_bars(circles, radius, gap, speed, y, left, right):
    x = left + random.uniform(-gap / 2, gap / 2)
    step = 2 * radius + gap
    while x <= right:
        circles.append(Obstacle(x, y, 0, speed, radius, collidable=False))
        x += step

def bottom_bars(circles, radius, gap, speed, y, left, right):
    x = left + random.uniform(-gap / 2, gap / 2)
    step = 2 * radius + gap
    while x <= right:
        circles.append(Obstacle(x, y, 0, -speed, radius, collidable=False))
        x += step

def generate_bars(circles, radius, gap, speed):

    direction = random.choice(['left', 'right', 'up', 'down'])

    if direction == 'left':
        left_bars(circles, radius, gap, speed, -150, -150, 150)

    elif direction == 'right':

        right_bars(circles, radius, gap, speed, 150, -150, 150)

    elif direction == 'up':

        top_bars(circles, radius, gap, speed, -150, -150, 150)

    elif direction == 'down':
        bottom_bars(circles, radius, gap, speed, 150, -150, 150)
