''' Создать текстовый файл (не программно),
 сохранить в нем несколько строк, выполнить подсчет количества строк, количества слов в каждой строке.
'''
f = open('out_file.txt', 'r')
#s = f.readlines()
s = [line.rstrip() for line in f]
print(s)
print(f' в файле {len(s)} строк')
for i in s:
    print(f' количество слов в строке {i} = {len(i.split())}')
f.close()