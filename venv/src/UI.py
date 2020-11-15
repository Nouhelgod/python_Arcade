import arcade

FONT_H = 10
FONT_C = arcade.color.BLACK
MARGIN_L = 10

class Engine(arcade.Window):

    def set_pos(self, LINE):
        return [MARGIN_L + self.view_left,
                self.SCREEN_H - FONT_H * LINE - self.debug_margin + self.view_bottom]

    def update(self, delta_time):
        self.text_local_frame_counter += 1
        self.text_global_frame_counter += 1
        if self.text_global_frame_counter % 10 == 0:
            self.text_FPS = round(1 / delta_time)

    def draw_debug(self):
        if self.debug_shown:
            LINE = 1
            arcade.draw_text(f'Local frame: {self.text_local_frame_counter}',
                             Engine.set_pos(self, LINE)[0],
                             Engine.set_pos(self, LINE)[1],
                             FONT_C, FONT_H)

            LINE = 2
            arcade.draw_text(f'Global frame: {self.text_global_frame_counter}',
                             Engine.set_pos(self, LINE)[0],
                             Engine.set_pos(self, LINE)[1],
                             FONT_C, FONT_H)

            LINE = 3
            arcade.draw_text(f'FPS: {self.text_FPS}',
                             Engine.set_pos(self, LINE)[0],
                             Engine.set_pos(self, LINE)[1],
                             FONT_C, FONT_H)

            LINE = 4
            arcade.draw_text(f'X: {self.sprite_player.center_x}, Y: {self.sprite_player.center_y}',
                             Engine.set_pos(self, LINE)[0],
                             Engine.set_pos(self, LINE)[1],
                             FONT_C, FONT_H)


    def draw_UI(self):
        if self.restart[0]:
            arcade.draw_text('Loading', self.view_left + self.SCREEN_W / 2,
                             self.view_bottom + self.SCREEN_H / 2,
                             arcade.color.CORAL_RED, 40, anchor_x='center', anchor_y='center')
            self.restart[1] = True