import arcade
import player_object

class Engine(arcade.Window):
    def __init__(self):
        self.player = player_object.param()

    def key_press(self, key, modifiers):
        if key == arcade.key.UP:
            self.UP = True
        elif key == arcade.key.DOWN:
            self.DOWN = True
        elif key == arcade.key.LEFT:
            self.LEFT = True
        elif key == arcade.key.RIGHT:
            self.RIGHT = True

    def key_release(self, key, modifiers):
        if key == arcade.key.UP:
            self.UP = False
        elif key == arcade.key.DOWN:
            self.DOWN = False
        elif key == arcade.key.LEFT:
            self.LEFT = False
        elif key == arcade.key.RIGHT:
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