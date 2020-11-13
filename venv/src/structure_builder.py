import arcade

import spriter

class Engine(arcade.Window):
    def place_fountain(self, x, y):
        x -= 1
        y -= 1

        sprite_fountain = []

        fountain_img = ['sprites/fountain_bottom.png',
                        spriter.flip_horizontal('sprites/fountain_bottom.png'),
                        'sprites/fountain_top.png',
                        spriter.flip_horizontal('sprites/fountain_top.png')]

        for i in range(len(fountain_img)):
            fountain_img[i] = spriter.scale(fountain_img[i], self.SCREEN_SCALE)
            sprite_fountain.append(arcade.Sprite(fountain_img[i]))

        # Bottom left
        sprite_fountain[0].center_x = self.cell * x
        sprite_fountain[0].center_y = self.cell * y

        # Bottom right
        sprite_fountain[1].center_x = self.cell * (x + 1)
        sprite_fountain[1].center_y = self.cell * (y)

        # Top left
        sprite_fountain[2].center_x = self.cell * x
        sprite_fountain[2].center_y = self.cell * (y + 1)

        # Top right
        sprite_fountain[3].center_x = self.cell * (x + 1)
        sprite_fountain[3].center_y = self.cell * (y + 1)

        for i in range(len(sprite_fountain)):
            if i <= 1:
                self.list_tile.append(sprite_fountain[i])
            else:
                self.list_wall.append(sprite_fountain[i])