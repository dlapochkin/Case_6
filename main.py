"""Case-study Тесселяция
Разработчики:
Кривошапова Д.Е. 35%
Лапочкин Д.А. 40%
Кузнецов А.Д. 30%
"""
import turtle


def main():
    """
    THE MAIN FUNCTION
    :return: None
    """
    colors()
    c1 = color()
    c2 = color()
    quantity = correct_quantity()
    d = diameter(quantity)
    s = side(d)
    draw(c1, c2, d, s, quantity)


def colors():
    """
    COLOR MENU
    :return: None
    """
    print('Допустимые цвета заливки:')
    print('красный', 'синий', 'зеленый', 'оранжевый', 'пурпурный', 'розовый', sep='\n')


def color():
    """
    COLOR INPUT
    :return: colors
    """
    while True:
        c = input('Пожалуйста, введите цвет: ').strip().lower()
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
            print(c, 'не является верным значением.', end=' ')
            continue


def correct_quantity():
    """
    QUANTITY INPUT
    :return: quantity
    """
    n = input('Пожалуйста, введите количество шестиугольников, располагаемых в ряд: ')
    while True:
        if n.isdigit():
            n = int(n)
            if 3 < n < 21:
                quantity = n
                return quantity
            else:
                print('Оно должно быть от 4 до 20.', end=' ')
                n = input('Пожалуйста, повторите попытку: ')
                continue
        else:
            print('Оно должно быть от 4 до 20.', end=' ')
            n = input('Пожалуйста, повторите попытку: ')
            continue


def diameter(n):
    """
    CALCULATES DIAMETER
    :param n: quantity
    :return: diameter
    """
    d = 500 / (2 * n + 1)
    return d


def side(d):
    """
    CALCULATES SIDE
    :param d: diameter
    :return: side
    """
    s = d * 2 / (3 ** 0.5)
    return s


def draw_hexagon(x, y, d, s, col):
    """
    DRAWING HEXAGON
    :param x: coordinate x
    :param y: coordinate y
    :param d: diameter of hexagon
    :param s: side of hexagon
    :param col: color of hexagon
    :return: None
    """
    turtle.up()
    turtle.setposition(x, y)
    turtle.left(90)
    turtle.forward(d)
    turtle.left(120)
    turtle.color('black', col)
    turtle.down()
    turtle.begin_fill()
    for repeat in range(6):
        turtle.forward(s)
        turtle.left(60)
    turtle.end_fill()
    turtle.penup()
    turtle.left(60)
    turtle.forward(s)
    turtle.left(90)


def draw(c1, c2, d, s, q):
    """
    TESSELATION
    :param c1: first color
    :param c2: second color
    :param d: diameter of each hexagon
    :param s: side of each hexagon
    :param q: quantity
    :return: None
    """
    turtle.speed(100)
    o = 0
    i = 0
    y = 250 - s
    for rep_y in range(q):
        x = -250
        if i == 0:
            for rep_x in range(q):
                x = x + 2 * d
                if o % 2 == 0:
                    col = c1
                    o += 1
                else:
                    col = c2
                    o += 1
                draw_hexagon(x, y, d, s, col)
            i = 1
            o += 1
        else:
            x = x - d
            for rep_x in range(q):
                x = x + 2 * d
                if o % 2 == 0:
                    col = c1
                    o += 1
                else:
                    col = c2
                    o += 1
                draw_hexagon(x, y, d, s, col)
            i = 0
        y = y - s - s / 2


main()
turtle.done()
