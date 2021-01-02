'''Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет) и метод running
(запуск). Атрибут реализовать как приватный. В рамках метода реализовать переключение светофора в режимы:
красный, желтый, зеленый. Продолжительность первого состояния (красный) составляет 7 секунд,
второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение. Переключение между режимами
должно осуществляться только в указанном порядке (красный, желтый, зеленый). Проверить работу примера,
создав экземпляр и вызвав описанный метод.
Задачу можно усложнить, реализовав проверку порядка режимов, и при его нарушении выводить соответствующее
сообщение и завершать скрипт.'''

from tkinter import *
import time

class TraficLight(Tk):
    __color = 0
    def __init__(self):
        self.state = 0
        super().__init__()
        self.title('Светофор')
        self.canvas = c = Canvas(self, width=70, height=190, bg="black")
        self.r = c.create_oval(10, 10, 60, 60, fill="red")
        self.y = c.create_oval(10, 70, 60, 120, fill="gray")
        self.g = c.create_oval(10, 130, 60, 180, fill="gray")
        c.pack()
        self.update()
        time.sleep(7)

    def running(self):
        if self.state == 0:
            self.state = 1
            self.canvas.itemconfigure(self.r, fill='gray')
            self.canvas.itemconfigure(self.y, fill='yellow')
            self.canvas.itemconfigure(self.g, fill='gray')
            self.after(2000, self.running)
        elif self.state == 1:
            self.state = 2
            self.canvas.itemconfigure(self.y, fill='gray')
            self.canvas.itemconfigure(self.g, fill='green')
            self.after(7000, self.running)
        elif self.state == 2:
            self.state = 3
            self.canvas.itemconfigure(self.g, fill='gray')
            self.canvas.itemconfigure(self.y, fill='yellow')
            self.after(2000, self.running)
        else:
            self.state = 0
            self.canvas.itemconfigure(self.r, fill='red')
            self.canvas.itemconfigure(self.y, fill='gray')
            self.after(7000, self.running)


obj = TraficLight()
obj.running()
obj.mainloop()