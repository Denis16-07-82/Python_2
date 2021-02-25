# Написать функцию num_translate(), переводящую числительные от 0 до 10 c
# английского на русский язык. Например:
# >>> num_translate("one")
# "один"
# >>> num_translate("eight")
# "восемь"
# Если перевод сделать невозможно, вернуть None.
# Подумайте, как и где лучше хранить информацию, необходимую
# для перевода: какой тип данных выбрать, в теле функции или снаружи.
def num_translate():
    words_dict={'one':'один','two':'два','three':'три','four':'четыре','five':'пять','six':'шесть','seven':'семь','eight':'восемь','nine':'девять','ten':'десять'}
    data_key=input('Введите число от одного до десяти на английском: ')
    if data_key==data_key.lower():
        print(words_dict.get(data_key))
    elif data_key==data_key.capitalize():
        print(words_dict.get(data_key.lower()).capitalize())


num_translate()
