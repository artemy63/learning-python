years_list = []
first_year = 1983
for i in range(first_year, first_year + 5):
    years_list.append(i)
print("initial years_list is", years_list)

print("third birth day was in", years_list[3])


things = ['mozarrella', 'cinderella', 'salmonella']
# no affect
things[2].capitalize()
print('no affect ' + str(things))
# there is affect
things[2] = things[2].capitalize()
print('affected ' + str(things))

things[0].upper()
print('no affect ' + str(things))
things[0] = things[0].upper()
print('affect ' + str(things))

del things[2]
print('deleted ' + str(things))

surprise = ['Groucho', 'Chico', 'Harpo']
print(surprise[-1].lower()[::-1].capitalize())

e2f = {
    'dog': 'chien',
    'cat': 'chat',
    'walrus': 'morse'
}
print("e2f['walrus']", e2f['walrus'])

f2e = {}
for name, value in e2f.items():
    f2e[value] = name
print('f2e = ' + str(f2e))
print("f2e[chien]", f2e.get('chien', 'emptyValue'))
print("f2e[not_existent]", f2e.get('not_existent', 'emptyValue'))

print('set(e2f.keys() = ' + str(set(e2f.keys())))
print('list(e2f.keys() = ' + str(list(e2f.keys())))


life = {
    'animals': {
        'cats': ['Henry', 'Grumpy', 'Lucy'],
        'octopi': {},
        'emus': {}
    },
    'plants': {},
    'other': {}
}

print('life keys() = ' + str(set(life.keys())))
print('life[animals] keys() = ' + str(list(life['animals'].keys())))
print('life[animals][cats] keys() = ' + str(life['animals']['cats']))
