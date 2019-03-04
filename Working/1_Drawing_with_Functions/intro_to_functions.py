import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# define your draw functions
def draw_cloud():
    """ Draw the snow"""
    arcade.draw_ellipse_filled(150, 470, 60, 30, arcade.color.WHITE, 0)
    arcade.draw_ellipse_filled(220, 480, 70, 50, arcade.color.WHITE, 0)
    arcade.draw_ellipse_filled(300, 470, 60, 30, arcade.color.WHITE, 0)

def draw_rollinghills():
    """ Draw rolling hills"""
    arcade.draw_ellipse_filled(800, 0, 400, 200, arcade.color.GREEN_YELLOW, 0)

def main():
    arcade.open_window(SCREEN_WIDTH, SCREEN_HEIGHT, "Drawing with Functions")
    arcade.set_background_color(arcade.color.LIGHT_BLUE)
    arcade.start_render()

   # call your draw functions
    draw_cloud()
    draw_rollinghills()

    # Finish and run
    arcade.finish_render()
    arcade.run()


# Call the main function to get the program started.
main()