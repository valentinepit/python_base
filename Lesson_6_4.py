'''4.	Реализуйте базовый класс Car.
●	у класса должны быть следующие атрибуты: speed, color, name, is_police (булево). А также методы:
 go, stop, turn(direction), которые должны сообщать, что машина поехала, остановилась, повернула (куда);
●	опишите несколько дочерних классов: TownCar, SportCar, WorkCar, PoliceCar;
●	добавьте в базовый класс метод show_speed, который должен показывать текущую скорость автомобиля;
●	для классов TownCar и WorkCar переопределите метод show_speed. При значении скорости свыше 60 (TownCar)
и 40 (WorkCar) должно выводиться сообщение о превышении скорости.

Создайте экземпляры классов, передайте значения атрибутов. Выполните доступ к атрибутам, выведите результат.
 Вызовите методы и покажите результат.
.'''


class Car:
    def __init__(self, speed, color, name, is_police):
        self.s = speed
        self.c = color
        self.n = name
        self.i = is_police
        self.go()

    def go(self):
        print(f'{self.n} is started')

    def stop(self):
        print(f'{self.n} is stoped')

    def turn(self, direction):
        if direction == 'l':
            print(f'{self.n} is turned left')
        else:
            return (f'{self.n} is terned right')

    def show_speed(self):
        return self.s

class TownCar(Car):
    def show_speed(self):
        if self.s > 60:
            return self.s, f'Warning!!! You speed is too high!!!'

class WorkCar(Car):
    def show_speed(self):
        if self.s > 40:
            return self.s, f'Warning!!! You speed is too high!!!'

class PoliceCar(Car):
    pass

class GolfCar(Car):
    pass

polly = PoliceCar(60, 'white', 'Polly', True)
print(polly.show_speed())
harv = WorkCar(60, 'Green', 'Harvey', False)
print(harv.show_speed())
harv.turn('l')
merl = TownCar(65, 'Yellow', 'Merlin', False)
print(f'{merl.n} is {merl.c}')
