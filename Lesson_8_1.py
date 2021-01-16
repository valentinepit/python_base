"""Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата
«день-месяц-год». В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года
(например, месяц — от 1 до 12). Проверить работу полученной структуры на реальных данных."""


class Date:

    def __init__(self, date):
        self.date = date

    @staticmethod
    def format(data):
        try:
            d = map(int, data.split('-'))
            return list(d)
        except ValueError:
            return f' {data} is not valid'


    @classmethod
    def valid(cls, obj):
        if type(cls.format(obj)) == str:
            return f' Data not valid'
        if cls.format(obj)[0] > 31 or cls.format(obj)[0] < 1:
            return f'Wrong day {cls.format(obj)[0]}'
        elif cls.format(obj)[1] > 12 or cls.format(obj)[1] < 1:
            return f' Wrong month {cls.format(obj)[1]}'
        elif cls.format(obj)[2] > 2021 or cls.format(obj)[2] < 1:
            return f' Wrong year {cls.format(obj)[2]}'
        return  f'{cls.format(obj)[0]}-{cls.format(obj)[1]}-{cls.format(obj)[2]}'


f = "0-13-2020"
print(Date.valid(f))