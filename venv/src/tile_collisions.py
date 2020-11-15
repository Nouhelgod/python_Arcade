import arcade

import player_object


class Engine(arcade.Window):
    def check_collision_list(self, list):
        if list in self.text_list_collisions:
            in_list = True
        else:
            in_list = False

        return in_list


    def __init__(self):
        self.player = player_object.param()

    def update(self):

        # list_water
        self.list_water.update()
        water_collision = arcade.check_for_collision_with_list(self.sprite_player, self.list_water)

        if water_collision != []:
            self.player.speed = self.player.speed_water

            if not Engine.check_collision_list(self, 'list_water'):
                self.text_list_collisions.append('list_water')

        else:
            self.player.speed = self.player.initial_speed

            if Engine.check_collision_list(self, 'list_water'):
                self.text_list_collisions.remove('list_water')

        #list_tiles
        self.list_tile.update()
        tile_collision = arcade.check_for_collision_with_list(self.sprite_player, self.list_tile)

        if tile_collision != []:
            if not Engine.check_collision_list(self, 'list_tile'):
                self.text_list_collisions.append('list_tile')

        else:
            if Engine.check_collision_list(self, 'list_tile'):
                self.text_list_collisions.remove('list_tile')