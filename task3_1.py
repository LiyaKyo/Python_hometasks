# 1. Написать функцию num_translate(), переводящую числительные от 0 до 10 c английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"

def num_translate(str):
    rus_num = ('один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять')
    eng_num = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten')
    printed_check = False
    for i in range(len(rus_num)):
        if str == eng_num[i]:
            print(rus_num[i])
            printed_check = True
    if (printed_check == False):
        print('None')

num_translate(input())
