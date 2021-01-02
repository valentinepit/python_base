'''3.	Реализовать базовый класс Worker (работник).
●	определить атрибуты: name, surname, position (должность), income (доход);
●	последний атрибут должен быть защищённым и ссылаться на словарь, содержащий элементы: оклад и премия,
например, {"wage": wage, "bonus": bonus};
●	создать класс Position (должность) на базе класса Worker;
●	в классе Position реализовать методы получения полного имени сотрудника (get_full_name) и дохода с
 учётом премии (get_total_income);
●	проверить работу примера на реальных данных: создать экземпляры класса Position, передать данные, проверить
значения атрибутов, вызвать методы экземпляров.

.'''


class Worker:
    def __init__(self, name, surname, position, income):
        self.n = name
        self.s = surname
        self.p = position
        self.i = income


class Position(Worker):

    def get_full_name(self):
        return self.n, self.s

    def get_total_income(self):
        return self.i['wage'] + self.i['bonus']


director = Position('Ivan', 'Ivanov', 'Boss', {'wage': 500, 'bonus': 250})
driver = Position('Michail', 'Freedman', 'driver', {'wage': 50, 'bonus': 10})
print(*director.get_full_name(), ' have an income', director.get_total_income())
print(*driver.get_full_name(), ' have an income', driver.get_total_income())
