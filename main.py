
c = 0
def color(c):
    print('Допустимые цвета заливки:')
    print('красный','синий','зеленый','оранжевый','пурпурный','розовый',sep='\n')
    while True:
        c = input('Пожалуйста, введите цвет: ').strip().lower()
        if c == 'зеленый' or c == 'зелёный':
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

        else:
            print('Оно должно быть от 4 до 20.', end=' ')
            n = input('Пожалуйста, повторите попытку: ')
            continue

print(correct_quantity(n))

def d(n):
    d=500/(2*n+1)
    return d

def s(d):
    s=d*2/(3**0.5)
    return s