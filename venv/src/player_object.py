import arcade

import spriter


class param():
    speed = 6
    speed_water = 3

    initial_speed = speed

class Player(arcade.Sprite):
    def __init__(self, SCREEN_SCALE):
        super().__init__()

        self.textures = []

        # Facing left
        texture = arcade.load_texture(spriter.flip_horizontal(
            spriter.scale('sprites/player.png', SCREEN_SCALE)))

        self.textures.append(texture)

        # Facing right
        texture = arcade.load_texture(spriter.scale('sprites/player.png', SCREEN_SCALE))
        self.textures.append(texture)

        # Facing up
        texture = arcade.load_texture(spriter.scale('sprites/player_back.png', SCREEN_SCALE))
        self.textures.append(texture)

        # Facing down
        texture = arcade.load_texture(spriter.scale('sprites/player_front.png', SCREEN_SCALE))
        self.textures.append(texture)

        self.texture = texture
        self.speed = 5

    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.change_x < 0:
            self.texture = self.textures[0]
        elif self.change_x > 0:
            self.texture = self.textures[1]

        elif self.change_y > 0:
            self.texture = self.textures[2]

        elif self.change_y < 0:
            self.texture = self.textures[3]

        # elif self.change_x == self.change_y:
        #     self.texture = self.textures[3]
