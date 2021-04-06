import arcade

import player_object
import spriter

class Engine(arcade.Window):
    def __init__(self):
        self.player = player_object.param()
        self.list_ui_inventory = arcade.SpriteList()

        self.slot_resolution = 48
        self.slot_weapon_pos = [0, 0]

        # Weapon slot
        self.slot_weapon_sprite = spriter.scale('sprites/inv_slot_weapon.png', 3)
        self.slot_weapon = arcade.Sprite(self.slot_weapon_sprite)

    def set_slot_pos(self, cell):
        slot_x = (self.SCREEN_W // 2 + self.view_left) - (self.sprite_inv_w // 2) + (self.slot_resolution // 2) + (self.slot_resolution * cell[0])
        slot_y = (self.SCREEN_H // 2 + self.view_bottom) - (self.sprite_inv_h // 2) + (self.slot_resolution // 2) + (self.slot_resolution * cell[1])

        return  [slot_x, slot_y]

    def get_slot_pos(self, cell):
        range_x = [cell[0] - (self.slot_resolution // 2) , cell[0] + (self.slot_resolution // 2)]
        range_y = [cell[1] - self.slot_resolution - (self.slot_resolution // 2), cell[1] - self.slot_resolution + (self.slot_resolution // 2)]
        #print([range_x, range_y])
        return [range_x, range_y]

    def draw_selector(self, x, y):
        self.slots = [Engine.get_slot_pos(self, self.slot_weapon_pos_true)]
        if x in range(self.slots[0][0][0], self.slots[0][0][1]):
            if y in range(self.slots[0][1][0], self.slots[0][1][1]):
                print('weapon')
                self.outline = arcade.draw_rectangle_outline(self.slot_weapon_pos_true[0], self.slot_weapon_pos_true[1],
                                              self.slot_resolution, self.slot_resolution, arcade.color.RED, 3)


    def update(self):
        self.sprite_inv_w = 320
        self.sprite_inv_h = 240
        self.sprite_inv_c = arcade.color.GRAY_BLUE

        # Inventory window
        self.sprite_inv = arcade.draw_rectangle_filled(
            self.SCREEN_W // 2 + self.view_left , self.SCREEN_H // 2 + self.view_bottom,
            self.sprite_inv_w, self.sprite_inv_h,
            self.sprite_inv_c)

        # Weapon slot
        self.slot_weapon_pos_true = Engine.set_slot_pos(self, self.slot_weapon_pos)
        self.slot_weapon.center_x = self.slot_weapon_pos_true[0]
        self.slot_weapon.center_y = self.slot_weapon_pos_true[1]
        self.list_ui_inventory.append(self.slot_weapon)
