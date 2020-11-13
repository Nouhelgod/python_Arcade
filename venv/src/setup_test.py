import arcade

import spriter
import structure_builder
import player_object


class Engine(arcade.Window):
    # def __init__(self):
    #     self.player = player_object.param

    def setup(self, SCREEN_W, SCREEN_H, SCREEN_SCALE):

        # Player
        self.list_player = arcade.SpriteList()
        self.SCREEN_SCALE = SCREEN_SCALE
        print(f'{type(self.SCREEN_SCALE)} setup')
        player_img = spriter.scale('sprites/player.png', self.SCREEN_SCALE)
        self.sprite_player = arcade.Sprite(player_img)
        self.sprite_player.center_x = 0
        self.sprite_player.center_y = 0
        self.list_player.append(self.sprite_player)

        # self.sprite_player = player_object.Player(self.SCREEN_SCALE)
        # self.sprite_player.center_x = 1
        # self.sprite_player.center_y = 1
        # self.list_player.append(self.sprite_player)




        # Grass
        self.list_tile = arcade.SpriteList(use_spatial_hash=True)

        grass_img = spriter.scale('sprites/grass.png', self.SCREEN_SCALE)
        for x in range(0, SCREEN_W, self.cell):
            for y in range(0, SCREEN_H, self.cell):
                grass = arcade.Sprite(grass_img)
                grass.center_x = x
                grass.center_y = y
                self.list_tile.append(grass)

        # Walls
        self.list_wall = arcade.SpriteList(use_spatial_hash=True)

        wall_img = spriter.scale('sprites/wall.png', self.SCREEN_SCALE)
        self.sprite_wall = arcade.Sprite(wall_img)

        self.sprite_wall.center_x = 0
        self.sprite_wall.center_y = self.cell*2
        self.list_wall.append(self.sprite_wall)

        structure_builder.Engine.place_fountain(self, 2, 4)
        structure_builder.Engine.place_fountain(self, 6, 4)
        structure_builder.Engine.place_fountain(self, 10, 10)

        # Initiate physics engine
        self.physics = arcade.PhysicsEngineSimple(self.sprite_player, self.list_wall)