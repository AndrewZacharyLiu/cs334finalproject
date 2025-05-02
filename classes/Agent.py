from .Circle import Circle

class Agent(Circle):
    def __init__(self, x, y, vx, vy, radius):
        super().__init__(x, y, vx, vy, radius, outline_color=(0, 0, 255), arrow_color=(0, 0, 0), collidable=True)
        self.hit = False