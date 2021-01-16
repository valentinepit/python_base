"""Начните работу над проектом «Склад оргтехники». Создайте класс, описывающий склад. А также
класс «Оргтехника», который будет базовым для классов-наследников. Эти классы — конкретные типы
оргтехники (принтер, сканер, ксерокс). В базовом классе определите параметры, общие для приведённых типов.
В классах-наследниках реализуйте параметры, уникальные для каждого типа оргтехники."""
import os
class Store():
    otdel = [1, 2]
    assort = {'Printer' : 10,
              'Scaner' : 10,
              'Xerox' : 10
              }
    def item_replace(self, item, o_1, o_2):
        s_1 = int(input(f'Введте номер текущего подразделения\n'))
        s_2 = int(input(f'Введте номер планируемоого подразделения\n'))
        if s_1 == 1 and s_2 == 2:
            o_2.assort[str(item.__class__).split('.')[-1].replace("'>", '')] += 1
            o_1.assort[str(item.__class__).split('.')[-1].replace("'>", '')] -= 1
        elif s_1 ==2 and s_2 ==1:
            o_2.assort[str(item.__class__).split('.')[-1].replace("'>", '')] -= 1
            o_1.assort[str(item.__class__).split('.')[-1].replace("'>", '')] += 1

        else:
            print(f'Ппробуйте снова')



class Otdel(Store):
    assort = {'Printer' : 5,
              'Scaner' : 5,
              'Xerox' : 5
              }
    def __init__(self, num):
        self.num = num

    def item_in(self, item):
        Store.assort[str(item.__class__).split('.')[-1].replace("'>", '')] += 1
        self.assort[str(item.__class__).split('.')[-1].replace("'>", '')] += 1
        print(f'Складские остатки в отделе  {self.assort}')

    def item_out(self, item):
        Store.assort[str(item.__class__).split('.')[-1].replace("'>", '')] -= 1
        self.assort[str(item.__class__).split('.')[-1].replace("'>", '')] -= 1
        print(f'Складские остатки в отделе {self.assort}')




class OrgTechniks():
    def __init__(self, format, voltage):
        self.format = format
        self.voltage = voltage

class Printer(OrgTechniks):
    def __init__(self, colored = False):
        self.colored = colored

class Scaner(OrgTechniks):
    def __init__(self, hand = False):
        self.hand = hand

class Xerox(OrgTechniks):
    def __init__(self, colored = False):
        self.colored = colored

def menu():
    id = int(input(f'Введте идентификатор товара \n Принтер - 1 \n Сканер  - 2 \n Xerox   - 3 \n'))
    os.system('cls') # не работает в Pycharm
    if id == 1:
        c = int(input(f'Введте идентификатор цветности \n Цветной      - 1 \n Черно-белый  - 2 \n'))
    elif id == 2:
        c = int(input(f'Введте идентификатор конфигурации \n Ручной      - 1 \n Планшетный  - 2 \n'))
    elif id == 3:
        c = int(input(f'Введте идентификатор цветности \n Цветной      - 1 \n Черно-белый  - 2 \n'))
    else:
        print('Выберите один из предложенных вариантов')
        menu()
    return [id, c]

def take_item(box, o_1, o_2):
    otd = int(input(f' Из какого отдела берем? \n Первый - 1 \n Второй - 2 \n'))
    if otd == 1:
       o_1.item_out(box)
    elif otd == 2:
       o_2.item_out(box)
    else:
        print('Введите корректный номер отдела')
        take_item(box, o_1, o_2)

def put_item(box, o_1, o_2):
    otd = int(input(f' В какой отдел добавляем? \n Первый - 1 \n Второй - 2 \n'))
    if otd == 1:
       o_1.item_in(box)
    elif otd == 2:
       o_2.item_in(box)
    else:
        print('Введите корректный номер отдела')
        put_item(box, o_1, o_2)

def sklad_menu(sklad, box, o_1, o_2):
    id = int(input(f'Что вы хотите сделать \n Взять со склада - 1 \n Поместить на склад  - 2 \n Переместить   - 3 \n'))
    os.system('cls') # не работает в Pycharm
    if id == 1:
        take_item(box, o_1, o_2)
    elif id == 2:
        put_item(box, o_1, o_2)
    elif id == 3:
        sklad.item_replace(box, o_1, o_2)
    else:
        print('Выберите один из предложенных вариантов')
        sklad_menu(sklad, box, o_1, o_2)
    pusk(sklad, o_1, o_2)

def pusk(sklad, o_1, o_2):
    item = menu()
    if item[0] == 1:
        box = Printer(item[1])
    elif item[0] == 2:
        box = Scaner(item[1])
    elif item[0] == 3:
        box = Xerox(item[1])
    sklad_menu(sklad, box, o_1, o_2)

def main():
    o_1 = Otdel(1)
    o_2 = Otdel(2)
    sklad = Store()
    pusk(sklad, o_1, o_2)


if __name__ == '__main__':
    main()