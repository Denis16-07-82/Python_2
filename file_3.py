# Реализовать функцию get_jokes(), возвращающую n шуток, сформированных из трех случайных
# слов, взятых из трёх списков (по одному из каждого):
# nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
# adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
# adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
# Например:
# >>> get_jokes(2)
# ["лес завтра зеленый", "город вчера веселый"]
# Документировать код функции.
# Сможете ли вы добавить еще один аргумент — флаг,
# разрешающий или запрещающий повторы слов в шутках
# (когда каждое слово можно использовать только в одной шутке)?
# Сможете ли вы сделать аргументы именованными?
from random import sample


def get_jokes(n=3, replay=1):
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    my_list = []
    if replay == 1:
        for ln in range(n):
            iter_nouns = sample(nouns, len(nouns))
            iter_adverbs = sample(adverbs, len(adverbs))
            iter_adjectives = sample(adjectives, len(adjectives))
            my_list.append(f'{iter_nouns[0]} {iter_adverbs[0]} {iter_adjectives[0]}')
        print(my_list)
    else:
        iter_nouns = sample(nouns, len(nouns))
        iter_adverbs = sample(adverbs, len(adverbs))
        iter_adjectives = sample(adjectives, len(adjectives))
        for ln in range(min(len(nouns), n)):
            my_list.append(f'{iter_nouns[ln]} {iter_adverbs[ln]} {iter_adjectives[ln]}')
        print(my_list)


get_jokes(12, 1)
