# 2. * (вместо задачи 1) Доработать предыдущую функцию в num_translate_adv(): реализовать корректную работу
# с числительными, начинающимися с заглавной буквы — результат тоже должен быть с заглавной

def num_translate_adv(str):
    rus_num = ('один', 'два', 'три', 'четыре', 'пять', 'шесть', 'семь', 'восемь', 'девять', 'десять')
    eng_num = ('one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten')
    printed_check = False
    for i in range(len(rus_num)):
        str_capit = eng_num[i].lower().capitalize()
        if str == eng_num[i]:
            print(rus_num[i])
            printed_check = True
        elif str == str_capit:
            print(rus_num[i].capitalize())
            printed_check = True
        else:
            continue
    if (printed_check == False):
        print('None')


num_translate_adv(input())
