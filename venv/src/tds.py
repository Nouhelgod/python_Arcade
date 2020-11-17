import arcade
from PIL import Image

import setup_test
import player_controls
import camera_controls
import tile_collisions
import UI
import inventory


SCREEN_W = 640
SCREEN_H = 480
SCREEN_TITLE = 'Build'
SPRITE_RESOLUTION = 16

SCREEN_SCALE = 4

class Engine(arcade.Window):
    def __init__(self):
        # Game window initiation
        super().__init__(SCREEN_W, SCREEN_H, SCREEN_TITLE)
        arcade.set_background_color(arcade.csscolor.GHOST_WHITE)

        # Controller initiation
        gamepades = arcade.get_joysticks()
        if gamepades:
            self.gamepad = gamepades[0]
            self.gamepad.open()
            self.gamepad.on_joybutton_press = self.on_joybutton_press
            self.gamepad.on_joybutton_release = self.on_joybutton_release
            self.gamepad.on_joyhat_motion = self.on_joyhat_motion
            self.gamepad.on_joyaxis_motion = self.on_stick_move

        else:
            self.joystick = None

        # Sprites scaling initiation
        self.SCREEN_SCALE = SCREEN_SCALE
        self.SPRITE_RESOLUTION = SPRITE_RESOLUTION
        self.cell = self.SCREEN_SCALE * self.SPRITE_RESOLUTION

        # Window parameters initiation
        self.SCREEN_W = SCREEN_W
        self.SCREEN_H = SCREEN_H
        self.SCREEN_TITLE = SCREEN_TITLE

        # Sprite lists initiation
        self.list_player = None
        self.list_tile = None
        self.list_wall = None
        self.list_water = None
        self.list_ui_inventory = None
        
        # Sprite images initiation
        self.sprite_player = None

        # Physics initiation
        self.physics = None

        # Keys initiation
        self.UP = False
        self.DOWN = False
        self.LEFT = False
        self.RIGHT = False

        # Tile collisions initiation
        self.collisions_tile = tile_collisions.Engine
        self.collisions_tile.__init__(self)

        # Player controls initiation
        self.player_controls = player_controls.Engine
        self.player_controls.__init__(self)
        self.can_move = True

        # Invintory initiation
        self.player_inventory = inventory.Engine
        self.player_inventory.__init__(self)

        # Scrolling initiation
        self.view_bottom = 0
        self.view_left = 0

        # Level initiation
        self.level = None

        # GUI initiation
        self.UI = UI
        self.debug_pos = 0
        self.debug_margin = 5
        self.inventory = False

        # GUI text initiation
        self.debug_shown = False
        self.text_global_frame_counter = 0
        self.text_local_frame_counter = 0
        self.text_FPS = 0
        self.restart = [False, False]
        self.text_list_collisions = []


    def setup(self):
        self.level = setup_test
        self.level.Engine.setup(self)


    def on_stick_move(self, _joystick, axis, value):
        self.player_controls.stick_move(self, axis, value)


    def on_joybutton_press(self, _joystick, button):
        print(button)
        self.player_controls.key_press(self, button, None)


    def on_joybutton_release(self, _joystick, button):
        self.player_controls.key_release(self, button, None)


    def on_joyhat_motion (self, _joystick, hat_x, hat_y):
        self.player_controls.hat_move(self, hat_x, hat_y)


    def on_key_press(self, key, modifiers):
        self.player_controls.key_press(self, key, modifiers)


    def on_key_release(self, key, modifiers):
        self.player_controls.key_release(self, key, modifiers)


    def on_update(self, delta_time: float):
        self.player_controls.update(self)
        self.collisions_tile.update(self)
        self.UI.Engine.update(self, delta_time)
        self.sprite_player.update()
        self.physics.update()
        self.player_inventory.update(self)

        camera_controls.Engine.camera_follow(self)


    def on_draw(self):
        arcade.start_render()
        self.list_tile.draw()
        self.list_wall.draw()
        self.list_player.draw()
        self.list_water.draw()
        self.UI.Engine.draw_UI(self)
        self.UI.Engine.draw_debug(self)

        if self.inventory:
            self.player_inventory.update(self)


def main():
    window = Engine()
    window.setup()
    arcade.run()


if __name__ == '__main__':
    main()