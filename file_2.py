# Написать функцию thesaurus(), принимающую в качестве аргументов
# имена сотрудников и возвращающую словарь, в котором ключи — первые буквы
# имён, а значения — списки, содержащие имена, начинающиеся с
# соответствующей буквы. Например:
# >>> thesaurus("Иван", "Мария", "Петр", "Илья")
# {
#     "И": ["Иван", "Илья"],
#     "М": ["Мария"], "П": ["Петр"]
# }
# Подумайте: полезен ли будет вам оператор распаковки?
# Как поступить, если потребуется сортировка по ключам?
# Можно ли использовать словарь в этом случае?
def thesaurus(*args):
    name_list=set()
    for name in args:
        name_list.add(name[0])
    name_dict={}.fromkeys(name_list)
    print(name_dict)
    print(id(name_dict))
    for key in name_dict.keys():
        name_list=[]
        for name in args:
            if name[0]==key:
                name_list.append(name)
        name_dict[key]=name_list
    print(name_dict)
    print(id(name_dict))




thesaurus('Сега','Сява','Даня','Петя')
