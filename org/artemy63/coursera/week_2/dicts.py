dict_1 = {}
dict_2 = dict()
print('dict_1 =', dict_1, 'and dict_2 =', dict_2)

collections_dict = {
    'mutable' : ['list', 'set'],
    'immutable' : ['tuple']
}
print('collections_dict.get("mutable") =', collections_dict.get('mutable'))
print('collections_dict.get("not_existence") =', collections_dict.get('not_existence', 'default if not found'))

#проверка вхождения
print('"mutable" in collections_dict', 'mutable' in collections_dict)
print('"transient" in collections_dict', 'transient' in collections_dict)

#добавление элемента
collections_dict['new_element'] = ['what_is_love']
print(collections_dict)

#удаление эдемента
del collections_dict['immutable']
print(collections_dict)

#итерирование
for key in collections_dict:
    print('collections_dict key = {}'.format(key))

for key, value in collections_dict.items():
    print('collections_dict key {} with value {}'.format(key, value))