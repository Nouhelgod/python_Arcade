import arcade

class Engine(arcade.Window):
    def camera_follow(self):
        changed = False

        MARGIN_TOP = self.SCREEN_H // 2 - self.sprite_player.height // 2
        MARGIN_LEFT = self.SCREEN_W // 2 - self.sprite_player.hit_box[0][0] // 2
        MARGIN_BOTTOM = MARGIN_TOP
        MARGIN_RIGHT = MARGIN_LEFT

        b_left = self.view_left + MARGIN_LEFT + self.cell
        if self.sprite_player.left < b_left:
            self.view_left -= b_left - self.sprite_player.left
            changed = True

        b_right = self.view_left + self.SCREEN_W - MARGIN_RIGHT + self.cell//2
        if self.sprite_player.right > b_right:
            self.view_left += self.sprite_player.right - b_right
            changed = True

        b_top = self.view_bottom + self.SCREEN_H - MARGIN_TOP
        if self.sprite_player.top > b_top:
            self.view_bottom += self.sprite_player.top - b_top
            changed = True

        b_bottom = self.view_bottom + MARGIN_BOTTOM
        if self.sprite_player.bottom < b_bottom:
            self.view_bottom -= b_bottom - self.sprite_player.bottom
            changed = True

        if changed:
            self.view_left = int(self.view_left)
            self.view_bottom = int(self.view_bottom)

            arcade.set_viewport(self.view_left, self.SCREEN_W + self.view_left,
                                self.view_bottom, self.SCREEN_H + self.view_bottom)

