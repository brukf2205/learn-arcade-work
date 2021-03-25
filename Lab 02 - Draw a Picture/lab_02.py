# Import the "arcade" library
import arcade
def sun():
    # Draw a sun
    arcade.draw_circle_filled(500, 550, 40, arcade.color.YELLOW)

    # Rays to the left, right, up, and down
    arcade.draw_line(500, 550, 400, 550, arcade.color.GREEN, 3)
    arcade.draw_line(500, 550, 600, 550, arcade.color.PURPLE, 3)
    arcade.draw_line(500, 550, 500, 450, arcade.color.NYANZA, 3)
    arcade.draw_line(500, 550, 500, 650, arcade.color.TULIP, 3)

    # Diagonal rays
    arcade.draw_line(500, 550, 550, 600, arcade.color.NEON_CARROT, 3)
    arcade.draw_line(500, 550, 550, 500, arcade.color.AMETHYST, 3)
    arcade.draw_line(500, 550, 450, 600, arcade.color.BITTER_LIME, 3)
    arcade.draw_line(500, 550, 450, 500, arcade.color.CEIL, 3)
def tree_one():
    # Draw a tree using triangles
    arcade.draw_rectangle_filled(400, 320, 20, 60, arcade.csscolor.SIENNA)
    arcade.draw_triangle_filled(400, 400, 370, 320, 430, 320, arcade.csscolor.DARK_GREEN)
def tree_two():
    # Another tree, with a trunk and arc for top
    arcade.draw_rectangle_filled(300, 320, 20, 60, arcade.csscolor.SIENNA)
    arcade.draw_arc_filled(300, 340, 60, 100, arcade.csscolor.DARK_GREEN, 0, 180)
def tree_three():
    # Draw a tree using a polygon with a list of points
    arcade.draw_rectangle_filled(500, 320, 20, 60, arcade.csscolor.SIENNA)
    arcade.draw_polygon_filled(((500, 400),
                                (480, 360),
                                (470, 320),
                                (530, 320),
                                (520, 360)
                                ),
                               arcade.csscolor.DARK_GREEN)
def open_window():

    # From the "arcade" library, use a function called "open_window"
    # Set the window title to "Drawing Example"
    # Set the and dimensions (width and height)
    arcade.open_window(800, 600, "A Beautiful Sunday")
    arcade.start_render()


open_window()
# Draw the cement
arcade.draw_lrtb_rectangle_filled(0, 800, 200, 0, arcade.color.BROWN_NOSE)

sun()
tree_one()
tree_two()
tree_three()


# --- Finish drawing ---
arcade.finish_render()

# Keep the window up until someone closes it.

arcade.run()

