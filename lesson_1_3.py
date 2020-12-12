num = int(input('Please give me your number 0<n<10 \n')) #ввод изначального числа
if num > 0 and num <10:
    num_1 = num * 10 + num # получаем nn
    num_2 = num * 100 + num_1 # получаем nnn
    print(num + num_1 + num_2)           
else:
    print('Next time give me the RIGHT number')
