import arcade
import player_object

class Engine(arcade.Window):
    def __init__(self):
        self.player = player_object.param()
        self.list_ui_inventory = arcade.SpriteList()


    def update(self):
        self.sprite_inv_w = 320
        self.sprite_inv_h = 240
        self.sprite_inv_c = arcade.color.GRAY_BLUE

        self.sprite_inv = arcade.draw_rectangle_filled(
            self.SCREEN_W // 2 + self.view_left , self.SCREEN_H // 2 + self.view_bottom,
            self.sprite_inv_w, self.sprite_inv_h,
            self.sprite_inv_c
        )