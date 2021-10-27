# Необходимо обработать список — обособить каждое целое число (вещественные не трогаем) кавычками
# (добавить кавычку до и кавычку после элемента списка, являющегося числом) и дополнить нулём до двух целочисленных
# разрядов:
# ['в', '"', '05', '"', 'часов', '"', '17', '"', 'минут', 'температура', 'воздуха', 'была', '"', '+05', '"', 'градусов']

time_data = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
i = 0
while i < (len(time_data)):
    if time_data[i].isdigit() == True:
        if len(time_data[i]) < 2:
            time_data[i] = '0' + time_data[i]
        time_data.insert(i, '"')
        time_data.insert(i+2, '"')
        i += 2
    if time_data[i][0] == '+':
        num = time_data[i].replace('+', '')
        if num.isdigit() == True:
            if len(num) < 2:
                time_data[i] = time_data[i][0] + '0' + time_data[i][1]
            time_data.insert(i, '"')
            time_data.insert(i + 2, '"')
            i += 2
    i += 1
print(time_data)

# Сформировать из обработанного списка строку:
# в "05" часов "17" минут температура воздуха была "+05" градусов

s, count_quote = '', 0
for i in range(len(time_data)):
    s += time_data[i]
    if time_data[i] == '"':
        count_quote += 1
    if count_quote % 2 != 1:
        s += " "
print(s)
