'''5.	Реализовать класс Stationery (канцелярская принадлежность).
●	определить в нём атрибут title (название) и метод draw (отрисовка). Метод выводит сообщение
 «Запуск отрисовки»;
●	создать три дочерних класса Pen (ручка), Pencil (карандаш), Handle (маркер);
●	в каждом классе реализовать переопределение метода draw. Для каждого класса метод должен выводить
уникальное сообщение;
●	создать экземпляры классов и проверить, что выведет описанный метод для каждого экземпляра.

.'''


class Stationery:
    def __init__(self, title):
        self.t = title

    def draw(self):
        print('Запуск отрисовки')

class Pencil(Stationery):
    def draw(self):
        print(f'Запуск отрисовки карандашом инструмент - {self.t}')

class Pen(Stationery):
    def draw(self):
        print(f'Запуск отрисовки ручкой инструмент - {self.t}')

class Hendle(Stationery):
    def draw(self):
        print(f'Запуск отрисовки инструмент - {self.t}')

p = Pen('ручка')
p.draw()

pn = Pencil('карандаш')
pn.draw()

h = Hendle('маркер')
h.draw()
