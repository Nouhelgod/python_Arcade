import arcade

import spriter


class param():
    speed = 5

class Player(arcade.Sprite):
    def __init__(self, SCREEN_SCALE):
        super().__init__()


        player_sprite = spriter.scale('sprites/player.png', SCREEN_SCALE)

        self.textures = []

        texture = arcade.load_texture(spriter.flip_horizontal(player_sprite))
        self.textures.append(texture)

        texture = arcade.load_texture(spriter.scale('sprites/player.png', SCREEN_SCALE))
        self.textures.append(texture)

        self.texture = texture
        self.speed = 5

    def update(self):
        print(f'{self.center_x}, {self.center_y}')
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.change_x < 0:
            self.texture = self.textures[0]
        elif self.change_x > 0:
            self.texture = self.textures[1]

