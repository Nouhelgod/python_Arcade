import arcade
from PIL import Image

# git test 1

import setup_test
import player_controls
import camera_controls

SCREEN_W = 640
SCREEN_H = 480
SCREEN_TITLE = 'Build'
SPRITE_RESOLUTION = 16

SCREEN_SCALE = 2

# hello github!

class Engine(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_W, SCREEN_H, SCREEN_TITLE)
        arcade.set_background_color(arcade.csscolor.GHOST_WHITE)

        # Sprites scaling initiation
        self.SCREEN_SCALE = SCREEN_SCALE
        self.SPRITE_RESOLUTION = SPRITE_RESOLUTION

        self.cell = self.SCREEN_SCALE * self.SPRITE_RESOLUTION

        # Sprite lists initiation
        self.list_player = None
        self.list_tile = None
        self.list_wall = None
        
        # Sprite images initiation
        self.sprite_player = None

        # Physics initiation
        self.physics = None

        # Keys initiation
        self.UP = False
        self.DOWN = False
        self.LEFT = False
        self.RIGHT = False

        # Player controls initiation
        self.player_controls = player_controls.Engine
        self.player_controls.__init__(self)

        # Scrolling initiation
        self.view_bottom = 0
        self.view_left = 0

    def setup(self):
        setup_test.Engine.setup(self, SCREEN_W, SCREEN_H, SCREEN_SCALE)

    def on_key_press(self, key, modifiers):
        self.player_controls.key_press(self, key, modifiers)

    def on_key_release(self, key, modifiers):
        self.player_controls.key_release(self, key, modifiers)

    def on_update(self, delta_time: float):
        # self.player_controls = player_controls.Engine(self)
        self.player_controls.update(self)
        self.physics.update()

        camera_controls.Engine.camera_follow(self, SCREEN_H, SCREEN_W)

    def on_draw(self):
        arcade.start_render()
        self.list_tile.draw()
        self.list_wall.draw()
        self.list_player.draw()
        
        
def main():
    window = Engine()
    window.setup()
    arcade.run()


if __name__ == '__main__':
    main()