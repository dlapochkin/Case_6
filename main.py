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