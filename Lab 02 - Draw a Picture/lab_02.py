import arcade
#Set the window
arcade.open_window(800, 600, "Drawing Example")
# Set the background color
arcade.set_background_color(arcade.color.WHITE)
# Get ready to draw
arcade.start_render()
#lo que es el campo
arcade.draw_lrtb_rectangle_filled(18, 782, 582, 18, arcade.color.BLACK)
arcade.draw_lrtb_rectangle_filled(20, 780, 580, 20, arcade.color.GREEN)
# Midcamp lane
arcade.draw_lrtb_rectangle_filled(390, 410, 600, 0, arcade.color.WHITE)
arcade.draw_circle_filled(400, 300, 35, arcade.color.WHITE)
arcade.draw_circle_filled(400, 300, 15, arcade.color.GREEN)
#Porteria no se como se dice jaja salu3(izquierda)
arcade.draw_lrtb_rectangle_filled(20, 100, 450, 150, arcade.color.WHITE)
arcade.draw_lrtb_rectangle_filled(40, 100, 430, 170, arcade.color.GREEN)
#Porteria no se como se dice jaja salu3(derecha)
arcade.draw_lrtb_rectangle_filled(700, 780, 450, 150, arcade.color.WHITE)
arcade.draw_lrtb_rectangle_filled(700, 760, 430, 170, arcade.color.GREEN)
#Españita
arcade.draw_lrtb_rectangle_filled(500, 650, 400, 370, arcade.color.RED)
arcade.draw_lrtb_rectangle_filled(500, 650, 370, 340, arcade.color.YELLOW)
arcade.draw_lrtb_rectangle_filled(500, 650, 340, 310, arcade.color.RED)
#AE
arcade.draw_triangle_filled(130, 330, 250, 330, 190, 500, arcade.color.RED)
arcade.draw_triangle_filled(150, 330, 230, 330, 190, 450, arcade.color.GREEN)
arcade.draw_lrtb_rectangle_filled(160, 220, 400, 380, arcade.color.RED)
arcade.draw_lrtb_rectangle_filled(230, 320, 340, 330, arcade.color.RED)
arcade.draw_lrtb_rectangle_filled(210, 320, 420, 410, arcade.color.RED)
arcade.draw_lrtb_rectangle_filled(190, 320, 498, 488, arcade.color.RED)
# --- Finish drawing ---
arcade.finish_render()

# Keep the window up until someone closes it.
arcade.run()