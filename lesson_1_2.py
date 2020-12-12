time = int(input('Please give me your secondnds \n')) #ввод изначального количества секунд
h = time // 3600 # получаем часы
m = (time-h*3600) // 60 # получаем минуты
s = time % 60 #а это секунды
print(f'The time is: {h}:{m}:{s}')           

