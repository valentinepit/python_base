'''Создать программно файл в текстовом формате, записать в него построчно данные, вводимые
пользователем.
Об окончании ввода данных свидетельствует пустая строка.
'''
s = 'stroka'
out_f = open("out_file.txt", "w")
while True:
    s = input('Input Your string')
    if s == '':
        break
    out_f.write(s + '\n')
out_f.close()
