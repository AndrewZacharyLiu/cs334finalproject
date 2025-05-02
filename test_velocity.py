

import math
from classes import Obstacle

'''def test_velocity(circles, velocity):
    for circle in circles:
        if isinstance(circle, Obstacle):
            vx_fixed = velocity[0] - circle.vx
            vy_fixed = velocity[1] - circle.vy
            d = math.hypot(vx_fixed, vy_fixed)

            vo = circle.velocity_obstacle
            if d >= vo['time_horizon_radius']:
                angle_val = math.atan2(vy_fixed, vx_fixed)
                lower_bound = vo['theta'] - vo['beta']
                upper_bound = vo['theta'] + vo['beta']

                if lower_bound <= angle_val <= upper_bound:
                    #collision will happen, do collision formula for
                    return False
    return True'''

def test_velocity(circles, velocity, agent):
    closest_collision_time = None
    for circle in circles:
        if isinstance(circle, Obstacle):
            rel_vx = velocity[0] - circle.vx
            rel_vy = velocity[1] - circle.vy
            A = rel_vx**2 + rel_vy**2
            B = 2 * ((agent.x - circle.x) * rel_vx + (agent.y - circle.y) * rel_vy)
            C = (agent.x - circle.x)**2 + (agent.y - circle.y)**2 - (circle.radius + agent.radius)**2
            discriminant = B**2 - 4 * A * C
            if discriminant < 0:
            # No real solutions, meaning no collision
                continue
            if (A == 0):
                continue
            t1 = (-B + math.sqrt(discriminant)) / (2 * A)
            t2 = (-B - math.sqrt(discriminant)) / (2 * A)
            sol = None
            if t1 >= 0 and t1 <= t2 and t1 <= 5.5: # 6 is time horizon, ignore times great than 6
                sol = t1
            elif t2 >= 0 and t2 <= t1 and t2 <= 5.5:
                sol = t2
            else:
                continue
            
            # replace best_result with the closest collision time we have found
            if (sol is not None):
                if (closest_collision_time is not None):
                    if (sol < closest_collision_time):
                        closest_collision_time = sol
                else:
                    closest_collision_time = sol
    #returns closest collision time, or None if no predicted collision within time horizon
    return closest_collision_time



