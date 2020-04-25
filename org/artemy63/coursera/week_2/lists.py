#списки
empty_list = []
print(empty_list)

empty_list_2 = list()
print(empty_list_2)

none_list = [None]*4
print(none_list)

str_list = 'Some_string'*3
print(str_list)

collections = ['list', 'tuple', 'dict', 'set']
print(collections, 'and it length = ', len(collections))
print('first element in collection = ', collections[0])
print('last element in collection = ', collections[-1])

#lists can be changed
collections[3] = 'frozenset'
print('it is possible to change lists :', collections)

user_data = [
    ['aaa', 4.4],
    ['sss', 3]
]
print(user_data)

print('------')
#срезы
range_list = list(range(10))
print('range_list', range_list)
print('range_list[1:3]', range_list[1:3])
print('range_list[2:]', range_list[2:])
print('range_list[:6]', range_list[:6])
print('range_list[::2]', range_list[::2])
print('range_list[::-1]', range_list[::-1])
print('range_list[5:1:-1]', range_list[5:1:-1])
print('------')

#итерирование
for collection in collections:
    print('Learning {}...'.format(collection))

#with index
for idx, collection in enumerate(collections):
    print('#{} {}'.format(idx, collection))

#изменение
collections.append('OrderedDict')
print('collections after adding element', collections)

#расширение списка другим списком
collections.extend(['ponyset', 'unicorndict'])
print('collections after extend', collections)