'''Пользователь вводит месяц в виде целого числа от 1 до 12.
Сообщить к какому времени года относится месяц
(зима, весна, лето, осень). Напишите решения через list и через dict'''

new_dic = {'Зима' : ['Январь', 'Февраль', 'Декабрь'], 'Весна' : ['Март', 'Апрель', 'Май'],
           'Лето' : ['Июнь', 'Июль', 'Август'], 'Осень' : ['Сентябрь', 'Октябрь', 'Ноябрь']}
while True:
    month = input(f'Введите название месяца ')
    flag = False
    for k, i in new_dic.items():
        for n in range(3):
            if month == i[n]:
                print(k)
                flag = True
    if flag == False:
        print('Введите корректное название')


