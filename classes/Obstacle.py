from .Circle import Circle

class Obstacle(Circle):
    def __init__(self, x, y, vx, vy, radius, collidable):
        color = (255, 0, 0)
        if not collidable:
            color = (255, 80, 0)
        super().__init__(x, y, vx, vy, radius, outline_color=color, arrow_color=(0, 0, 0), collidable=collidable)
        
        # Equivalent to MATLAB struct
        self.velocity_obstacle = {
            'time_horizon_radius': 0,
            'theta': 0,
            'beta': 0
        }