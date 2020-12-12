num = int(input('Please give me your number \n')) #ввод изначального числа
big_one = 0 # максимальная цифра равна 0
if num < 10 and num > -10: # отсечение цифр от чисел
    print(num)
else:
    if num < 0: # приводим к положительному значению
        num = num * -1
    while num >=10:  # пока есть больше одного разряда 
        if num % 10 > big_one: # если остаток от деления на 10 больше максимального, то меняем значение максимального
            big_one = num % 10
        num = num // 10 # сокращаем разряд на 1
    print (big_one)    
