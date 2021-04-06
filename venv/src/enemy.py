import arcade

class Enemy(arcade.Sprite):
    def __init__(self):
        self.speed = None
        self.textures = []
        self.damage = None
        self.agressive = None

    def print_speed(self):
        print(self.speed)


class Zombie(Enemy):
    def __init__(self):
        self.speed = 5

class Skeleton(Enemy):
    def __init__(self):
        self.speed = 6
