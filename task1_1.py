duration = int(input())
days, hours, minutes, result = 0, 0, 0, ''
if duration // (24*60*60) > 0:
    days = duration // (24*60*60)
    result = f'{days} дн '
    duration = duration % (24*60*60)
if duration // (60*60) > 0:
    hours = duration // (60*60)
    duration = duration % (60*60)
    result += f'{hours} час '
if duration // 60 > 0:
    minutes = duration // 60
    result += f'{minutes} мин '
seconds = duration % 60
result += f'{seconds} сек'
print(result)

# Можно ли использовать цикл для проверки работы кода сразу для нескольких значений продолжительности,
# будет ли тут полезен список? 

duration = int(input())
divider = [24*60*60, 60*60, 60]
time_text = ('дн', 'час', 'мин', 'сек')
result = ''
for i in range(3):
    if duration // divider[i] > 0:
        result += f'{duration // divider[i]} {time_text[i]} '
        duration = duration % divider[i]
result += f'{duration} {time_text[3]}'
print(result)
