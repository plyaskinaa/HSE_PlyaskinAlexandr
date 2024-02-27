'''
1.1. Создайте ряд функций для проведения математических вычислений:
 функция вычисления факториала числа (произведение натуральных чисел от 1
до n). Принимает в качестве аргумента число, возвращает его факториал;
'''
def factorial(number):
    from math import factorial
    result = factorial(number)
    return result
number = int(input('Введите число: '))
print(factorial(number))
'''
1.2. поиск наибольшего числа из трёх. Принимает в качестве аргумента кортеж из
трёх чисел, возвращает наибольшее из них;
'''
def search_the_largest(*args):
    a, b, c = args[0, 1, 2]
    if a > b and a > c:
        print(a)
    elif b > a and b > c:
        print(b)
    elif c > a and c > b:
        print(c)
        '''
        1.3. расчёт площади прямоугольного треугольника. Принимает в качестве аргумента
        размер двух катетов треугольника. Возвращает площадь треугольника.
        '''

        def S(leg_1, leg_2):
            result = (leg_1 + leg_2) / 2
            return result

        leg_1 = float(input('Длина первого катета: '))
        leg_2 = float(input('Длина второго катета: '))
        print(S(leg_1, leg_2))
        '''