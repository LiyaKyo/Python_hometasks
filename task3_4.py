# 4. * (вместо задачи 3) Написать функцию thesaurus_adv(), принимающую в качестве аргументов строки
# в формате «Имя Фамилия» и возвращающую словарь, в котором ключи — первые буквы фамилий,
# а значения — словари, реализованные по схеме предыдущего задания и содержащие записи, в которых
# фамилия начинается с соответствующей буквы. Например:
# >>>thesaurus_adv("Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева")
# {
#     "А": {
#         "П": ["Петр Алексеев"]
#     },
#     "С": {
#         "И": ["Иван Сергеев", "Инна Серова"],
#         "А": ["Анна Савельева"]
#     }
# }


def thesaurus_adv(names):
    """"
     lname_char - the first character of the first name
     fname_char - the first character of the last name
     char_names - list of first names for one character
     если нет словаря с ключом (первая буква фамилии), то создаем для этой ключа словарь.
     Добавляем туда ключ (первая буква имени) и значение (создаем массив и добавляем аргумент "Имя Фамилия").
     Если значение с ключом (первая буква фамилии) существует, то проверяем существует ли значение у ключа
     (первая буква имени). Если есть, то сохраняем значение списка во временную переменную, добавляем новый аргумент
     "Имя Фамилия" и перезаписываем в значение данного ключа. Если у ключа (первая буква имени) нет значения, то
     создаем новый список и добавляем туда аргумент "Имя Фамилия"
     """
    d = {}
    char_names = []
    for name in names:
        lname_char = name[name.find(' ') + 1]
        fname_char = name[0]
        if d.get(lname_char):
            if (d[lname_char].get(fname_char)):
                char_names = d[lname_char][fname_char]
                print(char_names)
                char_names.append(name)
                d[lname_char][fname_char] = char_names
            else:
                d[lname_char][fname_char] = []
                d[lname_char][fname_char].append(name)
        else:
            d[lname_char] = {}
            d[lname_char][fname_char] = []
            d[lname_char][fname_char].append(name)
    return d


names = ["Иван Сергеев", "Инна Серова", "Петр Алексеев", "Илья Иванов", "Анна Савельева"]
print(thesaurus_adv(names))
