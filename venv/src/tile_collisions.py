import arcade

import player_object


class Engine(arcade.Window):
    def __init__(self):
        self.player = player_object.param()

    def update(self):
        self.list_water.update()

        water_collision = arcade.check_for_collision_with_list(self.sprite_player, self.list_water)

        if water_collision != []:
            self.player.speed = self.player.speed_water
        else:
            self.player.speed = self.player.initial_speed