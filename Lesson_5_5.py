'''Создать (программно) текстовый файл, записать в него программно набор чисел, разделенных пробелами.
 Программа должна подсчитывать сумму чисел в файле и выводить ее на экран.
'''
from random import randint


def f_of_nums(name):
# подготавливаем файл с числами
    with open(name, 'w') as f:
        for i in range(10):
            f.write(str(randint(5, 25)) + ' ')


f_name = 'nums.txt'
f_of_nums(f_name)
with open(f_name) as f_read:
    s = [int(i) for i in f_read.readline().split()]
    #print(s)
    sum = 0
    for i in s:
        sum += i
print(f'сумма чисел в файле = {sum}')
