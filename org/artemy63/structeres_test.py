drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'vodka', 'kahlua'},
    'manhattan': {'rye', 'bitters', 'vermouth'},
    'screwdriver': {'vodka', 'orange juice'}
}

for name, content in drinks.items():
    print('Coctail {} with ingredients {}'.format(name, content))
    if 'vodka' in content:
        print('vodka in ' + str(content))


for name, content in drinks.items():
    print(content & {'vermouth', 'orange juice'})
    if content & {'vermouth', 'orange juice'}:
        print('In this coctail {} present vermouth or orange juice'.format(name))

for name, content in drinks.items():
    if 'vodka' in content and not content & {'cream', 'vermouth'}:
        print('In this coctail {} present vodka and doesn''t present nor cream or vermouth'.format(name))

bruss = drinks['black russian']
wruss = drinks['white russian']

print('bruss & (intersection) wruss ' + str(bruss & wruss))
print('bruss | (union) wruss ' + str(bruss | wruss))
print('bruss - (difference) wruss ' + str(bruss - wruss))
print('wruss - (difference) bruss ' + str(wruss - bruss))
print('wruss ^ (simmetric_difference) bruss ' + str(wruss ^ bruss))
print('wruss <= (issubset) bruss ' + str(wruss <= bruss))
print('bruss => (issubset) wruss ' + str(bruss <= wruss))


