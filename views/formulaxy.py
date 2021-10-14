x_figma = 666
y_figma = 56
height = 1070
width = 1054
corner_radius = 50.0

#Formula canvas
canvas_x, canvas_y = x_figma + (width/2), y_figma + (height/2)
print(f"Canvas: x: {canvas_x} y: {canvas_y}")

#coordenadas
if corner_radius > height/2:
    corner_radius = height/2

reduce_width = width - (corner_radius*2)
reduce_height = height - 2
x, y = x_figma, y_figma
x = x + corner_radius

print(f"Ancho: {reduce_width}, Alto {reduce_height}, X = {x} Y = {y}")