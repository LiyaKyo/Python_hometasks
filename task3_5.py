# 5. Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных слов, взятых из
# трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
# Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг, разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)?
# Сможете ли вы сделать аргументы именованными?

from random import randrange


def get_jokes(n, repeat=False):
    """
    get_jokes()  returns n jokes formed from
    three random words taken from three lists (one from each)
    The "repeat"  is a flag that allows or prohibits repeating words in jokes
    (each word can only be used in one joke)
    """
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    if repeat and n > len(nouns):
        n = len(nouns)
    while n > 0:
        noun_ind, adverb_ind, adjectives_ind = randrange(len(nouns)), randrange(len(adverbs)), randrange(len(adjectives))
        print(f"{nouns[noun_ind]} {adverbs[adverb_ind]} {adjectives[adjectives_ind]}")
        if repeat:
            nouns.remove(nouns[noun_ind])
            adverbs.remove(adverbs[adverb_ind])
            adjectives.remove(adjectives[adjectives_ind])
        n -= 1


get_jokes(6, True)

# Сможете ли вы сделать аргументы именованными? Вот этот момент не поняла


