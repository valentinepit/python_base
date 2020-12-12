a = int(input('Please give me first day result \n')) #ввод показателей первого дня
b = int(input('Please give me required result \n')) #ввод показателей искомого дня
i = 1 # счетчик дней
while a < b :
    a = a*0.1 + a # увеличиваем a на 10%
    i = i + 1 # увеличиваем счетчик дней
print("You need to treining for ",i , " day(s)")    


