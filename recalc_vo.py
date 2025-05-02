import math

def recalc_vo(obstacle, agent):
    T = 5.5  # time horizon
    vec_x = obstacle.x - agent.x
    vec_y = obstacle.y - agent.y
    d = math.hypot(vec_x, vec_y)  # equivalent to norm([x, y])

    theta = math.atan2(vec_y, vec_x)
    if d == 0 or (obstacle.radius + agent.radius) / d > 1:  #
        beta = math.pi / 2  # VO covers all directions towards it
    else:
        beta = math.asin((obstacle.radius + agent.radius) / d)

    time_horizon_radius = max(0, (d - (obstacle.radius + agent.radius) ) / T)

    obstacle.velocity_obstacle['theta'] = theta
    obstacle.velocity_obstacle['beta'] = beta
    obstacle.velocity_obstacle['time_horizon_radius'] = time_horizon_radius
