'''Реализовать функцию my_func(), которая принимает три позиционных аргумента, и возвращает сумму
 наибольших двух аргументов.'''


def my_func(a,b,c):
    # вывод  двух наибольших чисел из трех
    print(f'сумма двух наибольших аргументов равна {max(a, b, c) + max(min(a, b), min(b, c))}')



print('Введите три числа')
try:
    my_func(int(input()), int(input()), int(input()))
except ValueError:
    print('Числа!!!" Ты знаешь числа?')