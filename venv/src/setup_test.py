import arcade

import spriter
import structure_builder
import player_object


class Engine(arcade.Window):
    def setup(self):

        self.list_tile = arcade.SpriteList(use_spatial_hash=True)
        self.list_wall = arcade.SpriteList(use_spatial_hash=True)
        self.list_water = arcade.SpriteList(use_spatial_hash=True)

        # Player
        self.list_player = arcade.SpriteList()

        self.sprite_player = player_object.Player(self.SCREEN_SCALE)
        self.sprite_player.center_x = self.SCREEN_W // 2
        self.sprite_player.center_y = self.SCREEN_H // 2
        self.list_player.append(self.sprite_player)

        # Grass
        grass_img = spriter.scale('sprites/grass.png', self.SCREEN_SCALE)
        for x in range(0, self.SCREEN_W, self.cell):
            for y in range(0, self.SCREEN_H, self.cell):
                grass = arcade.Sprite(grass_img)
                grass.center_x = x
                grass.center_y = y
                self.list_tile.append(grass)

        # Walls
        wall_img = spriter.scale('sprites/wall.png', self.SCREEN_SCALE)
        self.sprite_wall = arcade.Sprite(wall_img)

        self.sprite_wall.center_x = 0
        self.sprite_wall.center_y = self.cell*2
        self.list_wall.append(self.sprite_wall)

        # Fountains
        structure_builder.Engine.place_fountain(self, 2, 4)
        structure_builder.Engine.place_fountain(self, 6, 4)
        structure_builder.Engine.place_fountain(self, 10, 10)

        # Water
        structure_builder.Engine.place_pound(self, 1, -3, 10, 4)

        # Initiate physics engine
        self.physics = arcade.PhysicsEngineSimple(self.sprite_player, self.list_wall)