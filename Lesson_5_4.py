'''  Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Необходимо написать программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские. Новый блок строк должен записываться в новый
текстовый файл.
'''
from google_trans_new import google_translator
def trans(num, ln_from='en', ln_to='ru'):
    # переводим с языка from на язык to
    translator = google_translator()
    translate_text = translator.translate(num, lang_tgt=ln_to, lang_src=ln_from)
    return (translate_text)

with open ('numbers.txt') as f:
    s = [line.rstrip().split() for line in f]
    with open ('new_numbers.txt', 'w') as new:
        for i in range(len(s)):
            s[i][0] = trans(s[i][0]).rstrip()
            new.write(' '.join(s[i]) + "\n")
