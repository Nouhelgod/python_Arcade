import arcade

FONT_H = 10
FONT_C = arcade.color.BLACK
MARGIN_L = 10
LINES = []

class Engine(arcade.Window):

    def get_pos(self, LINE):
        return [MARGIN_L + self.view_left,
                self.SCREEN_H - FONT_H * LINE - self.debug_margin + self.view_bottom]


    def update(self, delta_time):
        self.text_local_frame_counter += 1
        self.text_global_frame_counter += 1
        if self.text_global_frame_counter % 10 == 0:
            self.text_FPS = round(1 / delta_time)


    def draw_text(self, text, LINE):
        pos = Engine.get_pos(self, LINE)
        arcade.draw_text(text, pos[0], pos[1], FONT_C, FONT_H)


    def draw_debug(self):
        if self.debug_shown:
            LINE = 0
            LINES = [f'Local frame: {self.text_local_frame_counter}',
                     f'Global frame: {self.text_global_frame_counter}',
                     f'TPS: {self.text_FPS}',
                     f'Center: X: {self.sprite_player.center_x}, Y: {self.sprite_player.center_y}',
                     f'Change: X: {self.sprite_player.change_x}, Y: {self.sprite_player.change_y}',
                     f'Collisions: {self.text_list_collisions}',
                     f'U: {self.UP}, D: {self.DOWN}, L: {self.LEFT}, R: {self.RIGHT}',
                     f'Inventory: {self.inventory}']

            for i in range(len(LINES)):
                LINE += 1
                Engine.draw_text(self, LINES[i], LINE)


    def draw_UI(self):
        if self.restart[0]:
            arcade.draw_text('Loading', self.view_left + self.SCREEN_W / 2,
                             self.view_bottom + self.SCREEN_H / 2,
                             arcade.color.CORAL_RED, 40, anchor_x='center', anchor_y='center')
            self.restart[1] = True