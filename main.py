import turtle, math
turtle.speed(0)

def area():
    turtle.up()
    turtle.left(90)
    turtle.forward(250)
    turtle.left(90)
    turtle.down()
    turtle.forward(250)
    for n in range(3):
        turtle.left(90)
        turtle.forward(500)
    turtle.left(90)
    turtle.forward(250)

def draw_hexagon(x, y, side_len, color):
    turtle.up()
    turtle.setposition(x, y)
    turtle.left(90)
    turtle.forward()
    turtle.left(120)
    turtle.down()
    for repeat in range(6):
        turtle.forward(side_len)
        turtle.left(60)

def draw():
    c = 0
    i = 0
    y = 250 - d / 2
    for repy in range(n):
        x = -250
        if i == 0:
            for repx in range():
                x = x + d
                if c = 0:
                    color = c1
                    c = 1
                else:
                    color = c2
                    c = 0
                draw_hexagon(x, y, s, color)
        else:
            x = x + d / 2
            for repx in range():
                x = x + d
                if c = 0:
                    color = c1
                    c = 1
                else:
                    color = c2
                    c = 0
                draw_hexagon(x, y, s, color)

area()
turtle.done()