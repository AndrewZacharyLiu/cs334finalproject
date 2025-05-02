import math
from classes import *
def handle_collision(c1, c2):
    dx = c2.x - c1.x
    dy = c2.y - c1.y
    dist = math.hypot(dx, dy)

    collided = dist < (c1.radius + c2.radius)
    if not collided:
        return False

     # Check if either object is non-collidable or if one is an obstacle
    if not c1.collidable and isinstance(c2, Obstacle):
        return False
    if not c2.collidable and isinstance(c1, Obstacle):
        return False
    # Unit normal and tangent vectors
    nx = dx / dist
    ny = dy / dist
    tx = -ny
    ty = nx

    # Velocities
    v1x, v1y = c1.vx, c1.vy
    v2x, v2y = c2.vx, c2.vy

    # Masses (using radius squared)
    m1 = c1.radius ** 2
    m2 = c2.radius ** 2

    # Project velocities onto normal and tangent
    v1n = v1x * nx + v1y * ny
    v1t = v1x * tx + v1y * ty
    v2n = v2x * nx + v2y * ny
    v2t = v2x * tx + v2y * ty

    # New normal velocities after 1D elastic collision
    v1n_new = (v1n * (m1 - m2) + 2 * m2 * v2n) / (m1 + m2)
    v2n_new = (v2n * (m2 - m1) + 2 * m1 * v1n) / (m1 + m2)

    # Convert back to x/y
    if c1.collidable:
        c1.vx = v1n_new * nx + v1t * tx
        c1.vy = v1n_new * ny + v1t * ty
    if c2.collidable:
        c2.vx = v2n_new * nx + v2t * tx
        c2.vy = v2n_new * ny + v2t * ty

    overlap = (c1.radius + c2.radius) - dist
    if overlap > 0:
        correction_ratio = overlap / (m1 + m2)
        if c1.collidable:
            c1.x -= nx * correction_ratio * m2
            c1.y -= ny * correction_ratio * m2
        if c2.collidable:
            c2.x += nx * correction_ratio * m1
            c2.y += ny * correction_ratio * m1
    return True
