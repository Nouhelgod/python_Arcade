import arcade
import player_object

class Engine(arcade.Window):
    def __init__(self):
        self.player = player_object.param()

        self.keys_UP = [arcade.key.UP, arcade.key.W]
        self.keys_DOWN = [arcade.key.DOWN, arcade.key.S]
        self.keys_LEFT = [arcade.key.LEFT, arcade.key.A]
        self.keys_RIGHT = [arcade.key.RIGHT, arcade.key.D]

        self.key_debug = arcade.key.F3

    def key_press(self, key, modifiers):

        # Movement
        if key in self.keys_UP:
            self.UP = True
        elif key in self.keys_DOWN:
            self.DOWN = True
        elif key in self.keys_LEFT:
            self.LEFT = True
        elif key in self.keys_RIGHT:
            self.RIGHT = True

        # Restart
        if key == arcade.key.R:
            self.restart[0] = True


    def key_release(self, key, modifiers):

        # Movement
        if key in self.keys_UP:
            self.UP = False
        elif key in self.keys_DOWN:
            self.DOWN = False
        elif key in self.keys_LEFT:
            self.LEFT = False
        elif key in self.keys_RIGHT:
            self.RIGHT = False

        # Restart
        if key == arcade.key.R:
            if self.restart[1]:
                self.level.Engine.setup(self)
                self.restart[1] = False
                self.restart[0] = False

        if key == self.key_debug:
            self.debug_shown = not self.debug_shown


    def update(self):
        self.sprite_player.center_x = int(round(self.sprite_player.center_x))
        self.sprite_player.center_y = int(round(self.sprite_player.center_y))
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

