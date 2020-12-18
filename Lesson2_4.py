'''Пользователь вводит строку из нескольких слов, разделённых пробелами.
Вывести каждое слово с новой строки. Строки необходимо пронумеровать.
Если в слово длинное, выводить только первые 10 букв в слове.'''

stroka = input('Enter Your string ').rstrip().split()
for i in range(len(stroka)):
    if len(stroka[i]) > 10:
        print(i + 1, stroka[i][0:10])
    else:
        print(i + 1, stroka[i])



