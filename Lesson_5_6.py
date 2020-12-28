'''Необходимо создать (не программно) текстовый файл, где каждая строка описывает учебный предмет
и наличие лекционных, практических и лабораторных занятий по этому предмету и их количество.
Важно, чтобы для каждого предмета не обязательно были все типы занятий. Сформировать словарь, содержащий
название предмета и общее количество занятий по нему. Вывести словарь на экран.
Примеры строк файла:
Информатика: 100(л) 50(пр) 20(лаб).
Физика: 30(л) — 10(лаб)
Физкультура: — 30(пр) —

Пример словаря:
{“Информатика”: 170, “Физика”: 40, “Физкультура”: 30}
'''
import re


def plan(name):
    # подготавливаем файл с числами
    with open(name) as f:
        s = [line.rstrip() for line in f]
    return s


f = 'plan.txt'
lst = plan(f)
print(lst)
sum = 0
#Следующая строчка не хочет складывать значения!!!! ЗАРАЗА. выдает только последнее
shadule = {re.findall('[А-я]{4,}', i)[0]: sum + int(re.findall('\d+'.strip(), i)[k]) for i in lst for k in
           range(len(re.findall('\d+'.strip(), i)))}
for i in lst:
    sum = 0
    for k in range(len(re.findall('\d+'.strip(), i))):
        sum = sum + int((re.findall('\d+'.strip(), i)[k]))
    shadule[re.findall('[А-я]{4,}', i)[0]] = sum

print(shadule)