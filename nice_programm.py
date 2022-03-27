from math import factorial, pi, sqrt
def inputNum(text = ""):
   return int(input("\t" + text))
def log(*arg):
    print("\t", *arg)
log('1 - сложение')
log('2 - вычитание')
log('3 - умножение')
log('4 - деление')
log('5 - возвести в факториал')
log('6 - возвести в квадрат')
log('7 - вычесление корня')
log('8 - вычисление значения синуса')
log('9 - вычисление значения косинуса')
log('10 - нахождение площадей,периметров и обьемов')
log('Выберете действие:')
action = inputNum()
if action == 1:
    log('Введите первое слaгаемое:')
    a = inputNum()
    log('Введите  второе  слaгаемое:')
    b = inputNum()
    log('Введите третье слaгаемое:')
    c = inputNum()
    d = a + b + c
    log('Сумма чисел',a,',',b,',',c,'в сумме дает',d)
elif action == 2:
    log('Введите уменьшаемое:')
    a = inputNum()
    log('Введите вычитаемое:')
    b = inputNum()
    d = a - b
    log('Разность чисел',a,'и',b,'дает',d)
elif action == 3:
    log('Введите первый множитель:')
    a = inputNum()
    log('Введите  второй множитель:')
    b = inputNum()
    log('Введите третий множитель:')
    c = inputNum()
    d = a * b * c
    log(d)
elif action == 4:
    log('Введите делимое:')
    a = inputNum()
    log('Введите делитель:')
    b = inputNum()
    d = a / b
    log(d)
elif action == 5:
    log('Введите число, которое хотите возвести в факториал:')
    a = inputNum()
    d = factorial(a)
    log(d)
elif action == 6:
    log('Введите число, которое хотите возвести в квадрат:')
    a = inputNum()
    d = a*a
    log(d)
elif action == 7:
    log('Введите число,из которого хотите найти корень:')
    a = inputNum()
    d = sqrt (a)
    log(d)
elif action == 8:
    log('Введите значение катета:')
    x = inputNum()
    log('Введите значение гипотенузы:')
    y = inputNum()
    d = x / y
    log(d)
elif action == 9:
    log('Введите значение катета:')
    x = inputNum()
    log('Введите значение гипотенузы:')
    y = inputNum()
    d = x / y
    log(d)
elif action == 10:
    log('1 - периметры')
    log('2 - площади')
    log('3 - объемы')
    log('Выберете дальнейшее действие:')
    nextAction = inputNum()
    if nextAction == 1:
        log('1 - круг')
        log('2 - прямоугольник/параллелограмм')
        log('3 - квадрат/ромб')
        log('4 - треугольник')
        log('5 - трапеция')
        log('Введите номер фигуры')
        shapes = inputNum()
        if shapes == 1:
            log('1 - вся окружность')
            log('2 - длина дуги')
            log('Выбирайте размер:')
            size = inputNum()
            if size == 1:
                log('Введите значение радиуса:')
                r = inputNum()
                Q = 2 * pi* r
                log(Q)
            if size == 2:
                log('Введите значение радиуса:')
                r = inputNum()
                log('Введите значение угла:')
                b = inputNum()
                Q = ( b * pi* r)/180
                print(Q)
        if shapes == 2:
            log('Введите значение  одной стороны:')
            a = inputNum()
            log('Введите значение другой стороны:')
            b = inputNum()
            P = (a+b)*2
            log(P)
        if shapes == 3:
            log('Введите значение стороны:')
            a = inputNum()
            P = a * 4
            log(P)
        if shapes == 4:
            log('Какоц вид треугольника?')
            log('1 - произвольный')
            log('2 - Равнобедренный')
            log('3 - равносторонний')
            log('Выберите вид треугольника:')
            typeOfTriangle = inputNum()
            if typeOfTriangle == 1:
                log('Введите значение первой стороны:')
                a = inputNum()
                log('Введите значение первой стороны:')
                b = inputNum()
                log('Введите значение первой стороны:')
                c = inputNum()
                P = a + b + c
                log(P)
            if typeOfTriangle == 2:
                log('Введите значение боковой стороны:')
                a = inputNum()
                log('Введите значение основания треугольника:')
                b = inputNum()
                P = a * 2 + b
                log(P)
            if typeOfTriangle == 3:
                log('Введите значение стороны:')
                a = inputNum()
                P = a * 3
                log(P)
        if shapes == 5:
            log('1 - произвольная')
            log('2 - равнобедренная')
            log('Выберете вид трапеции:')
            typeOfTrapezoid = inputNum()
            if typeOfTrapezoid == 1:
                log('Введите значение первой стороны:')
                a = inputNum()
                log('Введите значение второй стороны:')
                b = inputNum()
                log('Введите значение третьей стороны:')
                c = inputNum()
                log('Введите значение четвертой стороны:')
                d = inputNum()
                P = a + b + c + d
                log(P)
            if typeOfTrapezoid == 2:
                log('Введите длину боковой стороны:')
                a = inputNum()
                log('Введите длину верхнего основания:')
                b = inputNum()
                log('Введите длину нижнего основания стороны:')
                c = inputNum()
                P = a * 2 + b + c
                log(P)
    if nextAction == 2:
        log('1 - круг')
        log('2 - прямоугольник')
        log('3 - квадрат')
        log('4 - треугольник')
        log('5 - трапеция')
        log('6 - ромб')
        log('7 - параллелограмм')
        log('Введите номер фигуры:')
        shapes = inputNum()
        if shapes == 1:
                log('Введите значение радиуса:')
                r = inputNum()
                Q = pi* r * r
                log(Q)
        if shapes == 2:
            log('Введите значение  одной стороны:')
            a = inputNum()
            log('Введите значение другой стороны:')
            b = inputNum()
            S = a * b
            log(S)
        if shapes == 3:
            log('Введите значение стороны:')
            a = inputNum()
            S = a * a
            log(S)
        if shapes == 4:
            log('Введите значение стороны:')
            a = inputNum()
            log('Введите значение высоты:')
            b = inputNum()
            S = a * b
            log(S)
        if shapes == 5:
            log('Введите значение основания стороны:')
            a = inputNum()
            log('Введите значение основания стороны:')
            b = inputNum()
            log('Введите значение высоты:')
            h = inputNum()
            S =(a + b * h) / 2
            log(S)
        if  shapes == 6:
            log('1 - 1/2 произведение диагоналей')
            log('2 - сторона и высота ')
            log('Выберете способ:')
            methodOfFinding = inputNum()
            if methodOfFinding == 1:
                log('Введите длину  первой диагонали:')
                d1 = inputNum()
                log('Введите длину второй диагонали:')
                d2 = inputNum()
                S = 0.5 * d1 * d2
                log(S)
            else:
                log('Введите значение основания:')
                a = inputNum()
                log('Введите значение высоты:')
                h = inputNum()
                S = a * h
                log(S)
        if shapes == 7:
              log('Введите значение основания:')
              a = inputNum()
              log('Введите значение высоты:')
              h = inputNum()
              S = a * h
              log(S)
    if nextAction == 3:
        log('1 - куб')
        log('2 - шар')
        log('3 - параллелепипед')
        log('Введите номер фигуры:')
        Z = inputNum()
        if shapes == 1:
            log('Введите размер грани')
            a = inputNum()
            V = a**3
            print(V)
        if shapes == 2:
            log('Введите значение радиуса')
            r = inputNum()
            V = 3/4 * pi* r
            print(V)
        if shapes == 3:
           log('Bведите размер площади основания')
           S = inputNum()
           log('Bведите длину высоты')
           h = inputNum()
           V = S * h
           print(V)