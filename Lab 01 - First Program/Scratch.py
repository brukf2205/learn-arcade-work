import arcade
arcade.open_window(500, 600, "Drawing Example")
arcade.set_background_color(arcade.csscolor.GREY)
arcade.start_render()
arcade.draw_lrtb_rectangle_filled(0, 599, 300, 0, arcade.csscolor.CHOCOLATE)
arcade.draw_circle_filled(100, 350, 50, arcade.csscolor.GREEN)
arcade.draw_circle_filled(240, 350, 50, arcade.csscolor.YELLOW)
arcade.draw_circle_filled(375, 350, 50, arcade.csscolor.RED)
arcade.draw_rectangle_outline(0,599,300,0, arcade.csscolor.BLUE)
arcade.draw_text("Abstract at its finest!",50, 230,
                 arcade.color.BLACK, 24)
arcade.finish_render()
arcade.run()







