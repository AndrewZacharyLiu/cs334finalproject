from classes import Obstacle
from recalc_vo import recalc_vo
def recalc_vos(circles, agent):
    for circle in circles:
        if isinstance(circle, Obstacle):
            recalc_vo(circle, agent)
