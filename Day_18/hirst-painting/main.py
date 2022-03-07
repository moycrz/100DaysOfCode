import random
import turtle as turtle_module
from create_palette_class import CreateColors

# color_palette = [
#     (229, 228, 226), (225, 223, 224), (199, 175, 117), (124, 36, 24), (210, 221, 213), (168, 106, 57),
#     (222, 224, 227), (186, 158, 53), (6, 57, 83), (109, 67, 85), (113, 161, 175), (22, 122, 174),
#     (64, 153, 138), (39, 36, 36), (76, 40, 48), (9, 67, 47), (90, 141, 53), (181, 96, 79), (132, 40, 42),
#     (210, 200, 151), (141, 171, 155), (179, 201, 186), (172, 153, 159), (212, 183, 177), (176, 198, 203),
#     (150, 115, 120), (202, 185, 190), (40, 72, 82), (46, 73, 62), (47, 66, 82), (115, 134, 139)
# ]

color_palette = CreateColors('image.jpg', 38)
color_palette = color_palette.create_palette()

## Option 1 (it's mine)

# screen = turtle_module.Screen()
# screen.colormode(255)
#
# tim = turtle_module.Turtle()
# tim.shape("circle")
# tim.pensize(20)
# screen_size = screen.screensize()
# x = (screen_size[0] / 2) * -1
# y = (screen_size[1] / 2) * -1
#
# for _ in range(10):
#     tim.penup()
#     tim.setposition(x, y)
#     y += 50
#     tim.pendown()
#     tim.forward(1)
#     for _ in range(10):
#         tim.color(random.choice(color_palette))
#         tim.forward(1)
#         tim.penup()
#         tim.forward(50)
#         tim.pendown()

## Option 2 (teacher's choose)
turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
tim.setheading(225)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots + 1):
    tim.dot(20, random.choice(color_palette))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)


screen = turtle_module.Screen()
screen.exitonclick()
