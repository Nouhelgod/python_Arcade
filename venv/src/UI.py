import arcade

class Engine(arcade.Window):
    def update(self, delta_time):
        self.text_frame_counter += 1
        if self.text_frame_counter % 21 == 0:
            self.text_FPS = round(1 / delta_time)

    def draw_debug(self):
        if self.debug_shown:
            arcade.draw_text(f'frame {self.text_frame_counter}', 10 + self.view_left,
                             10 + self.view_bottom, arcade.csscolor.BLACK, 15)

            arcade.draw_text(f'FPS: {self.text_FPS}', 10 + self.view_left,
                             40 + self.view_bottom, arcade.csscolor.BLACK, 15)

    def draw_UI(self):
        if self.restart[0]:
            arcade.draw_text('Loading', self.view_left + self.SCREEN_W / 2, self.view_bottom + self.SCREEN_H / 2,
                             arcade.color.CORAL_RED, 40, anchor_x='center', anchor_y='center')
            self.restart[1] = True