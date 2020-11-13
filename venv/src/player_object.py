import arcade

import spriter


class param():
    speed = 5

class Player(arcade.Sprite):
    def __init__(self, SCREEN_SCALE):
        super().__init__()
        self.SCREEN_SCALE = SCREEN_SCALE
        print(f'{type(SCREEN_SCALE)} player')
        print(f'{type(self.SCREEN_SCALE)} self.player')
        player_sprite = spriter.scale('sprites/player.png', self.SCREEN_SCALE)


        self.textures = []

        texture = arcade.load_texture(spriter.flip_horizontal(player_sprite))
        self.textures.append(texture)

        texture = arcade.load_texture('sprites/grass.png')
        self.textures.append(texture)

        self.texture = texture
        self.speed = 5

    def update(self):
        print(f'{self.center_x}, {self.center_y}')
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.change_x < 0:
            self.texture = textures[1]
        elif self.change_x > 0:
            self.texture = self.textures[0]

