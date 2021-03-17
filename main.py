import turtle()
turtle.speed(10)

c = 0
def color(c):
    while True:
        c = input('Пожалуйста, введите цвет: ')
        if c == 'зеленый':
            c = 'green'
            return c
        elif c == 'красный':
            c = 'red'
            return c
        elif c == 'синий':
            c = 'blue'
            return c
        elif c == 'оранжевый':
            c = 'orange'
            return c
        elif c == 'желтый':
            c = 'yellow'
            return c
        elif c == 'пурпурный':
            c = 'purple'
            return c
        elif c == 'розовый':
            c = 'pink'
            return c
        else:
            print(c, 'не является верным значением.',end = ' ')
            continue
print(color(c))

n = 0
quantity = 0
n = input('Пожалуйста, введите количество шестиугольников, располагаемых в ряд: ')
def correct_quantity(n):
    while True:
        if n.isdigit() == True:
            n = int(n)
            if n > 3 and n < 21:
                quantity = n
                return quantity
            else:
                print('Оно должно быть от 4 до 20.', end=' ')
                n = input('Пожалуйста, повторите попытку: ')
                continue
print(correct_quantity(n))

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
                if c == 0:
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
                if c == 0:
                    color = c1
                    c = 1
                else:
                    color = c2
                    c = 0
                draw_hexagon(x, y, s, color)

area()
draw()
turtle.done()