from math import factorial, pi, sqrt

def inputNum(text = ""):
   return int(input("\t" + text))

def log(*arg):
    print("\t", *arg)

def pickAction():
    log('1 - сложение')
    log('2 - вычитание')
    log('3 - умножение')
    log('4 - деление')
    log('5 - возвести в факториал')
    log('6 - возвести в квадрат')
    log('7 - вычесление корня')
    log('8 - нахождение площадей,периметров и обьемов')
    log('Выберете действие:')
    return inputNum()

action = pickAction()
def addition():
    log('Введите первое слaгаемое:')
    a = inputNum()
    log('Введите  второе  слaгаемое:')
    b = inputNum()
    log('Введите третье слaгаемое:')
    c = inputNum()
    d = a + b + c
    log('Сумма чисел',a,',',b,',',c,'в сумме дает',d)

def subtraction():
    log('Введите уменьшаемое:')
    a = inputNum()
    log('Введите вычитаемое:')
    b = inputNum()
    d = a - b
    log('Разность чисел',a,'и',b,'дает',d)

def multiplication():
    log('Введите первый множитель:')
    a = inputNum()
    log('Введите  второй множитель:')
    b = inputNum()
    log('Введите третий множитель:')
    c = inputNum()
    d = a * b * c
    log(d)

def division():
    log('Введите делимое:')
    a = inputNum()
    log('Введите делитель:')
    b = inputNum()
    d = a / b
    log(d)

def factorial():
    log('Введите число, которое хотите возвести в факториал:')
    a = inputNum()
    d = factorial(a)
    log(d)

def squareNumber():
    log('Введите число, которое хотите возвести в квадрат:')
    a = inputNum()
    d = a*a
    log(d)

def rootNumber():
    log('Введите число,из которого хотите найти корень:')
    a = inputNum()
    d = sqrt (a)
    log(d)

def subAction():
    log('1 - периметры')
    log('2 - площади')
    log('3 - объемы')
    log('Выберете дальнейшее действие:')
    return inputNum()

def figure():
    log('1 - круг')
    log('2 - прямоугольник/параллелограмм')
    log('3 - квадрат/ромб')
    log('4 - треугольник')
    log('5 - трапеция')
    log('Введите номер фигуры')
    return inputNum()

def circleSize():
    log('1 - вся окружность')
    log('2 - длина дуги')
    log('Выбирайте размер:')
    return inputNum()

def formulaСircumference():
    log('Введите значение радиуса:')
    r = inputNum()
    Q = 2 * pi* r
    log(Q)
def arcLengthFormula():
    log('Введите значение радиуса:')
    r = inputNum()
    log('Введите значение угла:')
    b = inputNum()
    Q = ( b * pi* r)/180
    log(Q)

def figureTwo():
    log('Введите значение  одной стороны:')
    a = inputNum()
    log('Введите значение другой стороны:')
    b = inputNum()
    P = (a+b)*2
    log(P)

def figureThree():
    log('Введите значение стороны:')
    a = inputNum()
    P = a * 4
    log(P)
def figureFour():
    log('Какоц вид треугольника?')
    log('1 - произвольный')
    log('2 - Равнобедренный')
    log('3 - равносторонний')
    log('Выберите вид треугольника:')
    return inputNum()

def arbitraryTriangle():
    log('Введите значение первой стороны:')
    a = inputNum()
    log('Введите значение второй стороны:')
    b = inputNum()
    log('Введите значение третьей стороны:')
    c = inputNum()
    P = a + b + c
    log(P)

def isoscelesTriangle():
    log('Введите значение боковой стороны:')
    a = inputNum()
    log('Введите значение основания треугольника:')
    b = inputNum()
    P = a * 2 + b
    log(P)

def equilateralTriangle():
    log('Введите значение стороны:')
    a = inputNum()
    P = a * 3
    log(P)

def figureFive():
    log('1 - произвольная')
    log('2 - равнобедренная')
    log('Выберете вид трапеции:')
    return inputNum()

def arbitraryTrapezoid():
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

def isoscelesTrapezoid():
    log('Введите длину боковой стороны:')
    a = inputNum()
    log('Введите длину верхнего основания:')
    b = inputNum()
    log('Введите длину нижнего основания стороны:')
    c = inputNum()
    P = a * 2 + b + c
    log(P)

def secondFigures():
    log('1 - круг')
    log('2 - прямоугольник')
    log('3 - квадрат')
    log('4 - треугольник')
    log('5 - трапеция')
    log('6 - ромб')
    log('7 - параллелограмм')
    log('Введите номер фигуры:')
    return inputNum()

def squaresFiguresOne():
    log('Введите значение радиуса:')
    r = inputNum()
    Q = pi* r * r
    log(Q)

def squaresFiguresTwo():
    log('Введите значение  одной стороны:')
    a = inputNum()
    log('Введите значение другой стороны:')
    b = inputNum()
    S = a * b
    log(S)

def squaresFiguresThree():
    log('Введите значение стороны:')
    a = inputNum()
    S = a * a
    log(S)

def squaresFiguresFour():
    log('Введите значение стороны:')
    a = inputNum()
    log('Введите значение высоты:')
    b = inputNum()
    S = a * b
    log(S)

def squaresFiguresFive():
    log('Введите значение основания стороны:')
    a = inputNum()
    log('Введите значение основания стороны:')
    b = inputNum()
    log('Введите значение высоты:')
    h = inputNum()
    S =(a + b * h) / 2
    log(S)

def squaresFiguresSix():
    log('1 - 1/2 произведение диагоналей')
    log('2 - сторона и высота ')
    log('Выберете способ:')
    return inputNum()

def formulaForFindingOne():
    log('Введите длину  первой диагонали:')
    d1 = inputNum()
    log('Введите длину второй диагонали:')
    d2 = inputNum()
    S = 0.5 * d1 * d2
    log(S)

def formulaForFindingTwo():
    log('Введите значение основания:')
    a = inputNum()
    log('Введите значение высоты:')
    h = inputNum()
    S = a * h
    log(S)

def squaresFiguresSeven():
    log('Введите значение основания:')
    a = inputNum()
    log('Введите значение высоты:')
    h = inputNum()
    S = a * h
    log(S)

def volumeFigures():
    log('1 - куб')
    log('2 - шар')
    log('3 - параллелепипед')
    log('Введите номер фигуры:')
    return inputNum()

def volumeFigureOne():
    log('Введите размер грани')
    a = inputNum()
    V = a**3
    print(V)

def volumeFigureTwo():
    log('Введите значение радиуса')
    r = inputNum()
    V = 3/4 * pi* r
    print(V)

def volumeFigureThree():
    log('Bведите размер площади основания')
    S = inputNum()
    log('Bведите длину высоты')
    h = inputNum()
    V = S * h
    print(V)
if action == 1:
    addition()

elif action == 2:
    subtraction()

elif action == 3:
    multiplication()

elif action == 4:
    division()

elif action == 5:
    factorial()

elif action == 6:
    squareNumber()

elif action == 7:
    rootNumber()

elif action == 8:
    nextAction = subAction()

    if nextAction == 1:
        shapes = figure()

        if shapes == 1:
            size = circleSize()

            if size == 1:
                formulaСircumference()

            else:
                arcLengthFormula()

        if shapes == 2:
            shapes = figureTwo()

        if shapes == 3:
            shapes = figureThree()

        if shapes == 4:
            typeOfTriangle = figureFour()

            if typeOfTriangle == 1:
                arbitraryTriangle()

            if typeOfTriangle == 2:
                isoscelesTriangle()
            else:
               equilateralTriangle()

        if shapes == 5:
            typeOfTrapezoid = figureFive()

            if typeOfTrapezoid == 1:
                arbitraryTrapezoid()

            else:
                isoscelesTrapezoid()

    if nextAction == 2:
        shapes = secondFigures()

        if shapes == 1:
            squaresFiguresOne()

        if shapes == 2:
            squaresFiguresTwo()

        if shapes == 3:
           squaresFiguresThree()

        if shapes == 4:
            squaresFiguresFour()

        if shapes == 5:
            squaresFiguresFive()

        if  shapes == 6:
            methodOfFinding = squaresFiguresSix()

            if methodOfFinding == 1:
                formulaForFindingOne()

            else:
                formulaForFindingTwo()

        if shapes == 7:
            squaresFiguresSeven()

    if nextAction == 3:
        shapes = volumeFigures()

        if shapes == 1:
            volumeFigureOne()

        if shapes == 2:
            volumeFigureTwo()

        if shapes == 3:
            volumeFigureThree()