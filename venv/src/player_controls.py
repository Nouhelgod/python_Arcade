import arcade
import player_object

class Engine(arcade.Window):
    def __init__(self):
        self.player = player_object.param()

        self.keys_UP = [arcade.key.UP, arcade.key.W]
        self.keys_DOWN = [arcade.key.DOWN, arcade.key.S]
        self.keys_LEFT = [arcade.key.LEFT, arcade.key.A]
        self.keys_RIGHT = [arcade.key.RIGHT, arcade.key.D]

    def key_press(self, key, modifiers):
        if key in self.keys_UP:
            self.UP = True
        elif key in self.keys_DOWN:
            self.DOWN = True
        elif key in self.keys_LEFT:
            self.LEFT = True
        elif key in self.keys_RIGHT:
            self.RIGHT = True

    def key_release(self, key, modifiers):
        if key in self.keys_UP:
            self.UP = False
        elif key in self.keys_DOWN:
            self.DOWN = False
        elif key in self.keys_LEFT:
            self.LEFT = False
        elif key in self.keys_RIGHT:
            self.RIGHT = False

        # Reset
        if key == arcade.key.R:
            self.level.Engine.setup(self)


    def update(self):
        self.sprite_player.change_y = 0
        self.sprite_player.change_x = 0

        if 1:
            if self.UP and not self.DOWN:
                self.sprite_player.change_y = self.player.speed
            elif self.DOWN and not self.UP:
                self.sprite_player.change_y = -self.player.speed

            if self.RIGHT and not self.LEFT:
                self.sprite_player.change_x = self.player.speed
            elif self.LEFT and not self.RIGHT:
                self.sprite_player.change_x = -self.player.speed

            if self.UP and self.LEFT:
                self.sprite_player.change_y = self.player.speed // 2 +1
                self.sprite_player.change_x = -self.player.speed // 2 +1

            if self.UP and self.RIGHT:
                self.sprite_player.change_y = self.player.speed // 2 +1
                self.sprite_player.change_x = self.player.speed // 2 +1

            if self.DOWN and self.LEFT:
                self.sprite_player.change_y = -self.player.speed // 2 +1
                self.sprite_player.change_x = -self.player.speed // 2 +1

            if self.DOWN and self.RIGHT:
                self.sprite_player.change_y = -self.player.speed // 2 +1
                self.sprite_player.change_x = self.player.speed // 2 +1