import random
import math
from test_velocity import test_velocity
def sample_velocities(circles, agent, x_max, y_max):

    if test_velocity(circles, [0, 0], agent) is None:
        return [0, 0]
    if (test_velocity(circles, [agent.vx, agent.vy], agent) is None):
        return [agent.vx, agent.vy]
    
    best_velocity = None
    best_magnitude = float('inf')

    # if unable to select best non colliding velocity, pick velocity with furthest collision time
    best_effort_velocity = None
    best_effort_collision_time = None

    #offset_range = granularity / 4
    # Sample systematically
    for vx in range(0 - x_max, x_max + 1 , 3):  # scale by 10 to handle floating points
        for vy in range(0 - y_max, y_max + 1, 3):
            vx = vx
            vy = vy
            

            # Ensure the velocity is within the bounds
            vx = max(min(vx, x_max), -x_max)
            vy = max(min(vy, y_max), -y_max)
            res = test_velocity(circles, [vx, vy], agent)
            if res is None:  # Means it's a safe velocity
                mag = math.hypot(vx, vy)
                if mag < best_magnitude:
                    best_magnitude = mag
                    best_velocity = [vx, vy]
            elif best_velocity is None:
                if (best_effort_velocity is None):
                    best_effort_velocity = [vx, vy]
                    best_effort_collision_time = res
                else:
                    if (res > best_effort_collision_time):
                        best_effort_velocity = [vx, vy]
                        best_effort_collision_time = res


    if best_velocity is not None:
        return best_velocity 
    else:
        return best_effort_velocity
