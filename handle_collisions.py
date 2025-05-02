from handle_collision import handle_collision
from classes import *
def handle_collisions(circles):
    res = False
    for i in range(0, len(circles)):
        for j in range(i + 1, len(circles)):
            temp_res = handle_collision(circles[i], circles[j])
            if (isinstance(circles[i], Agent)):
                res = temp_res or res      
    return res