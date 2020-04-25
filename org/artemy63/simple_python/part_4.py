# while loop with optional else, else will called when there were NOT break called inside while
source_array = [1, 4, 15, 123]
position = 0
while position < len(source_array):
    print('current element ' + str(source_array[position]))
    position = position + 1
    if position == 5:
        break
else:
    print('Condition for "break" operator does not called')
print('-------------')

for element in source_array:
    print('current element ' + str(element))
print('-------------')

source_dict = {'key1': 'value1', 'key2': 'value2'}
for k, v in source_dict.items():
    print('current key ' + k + ' with current value ' + v)
print('-------------')

# for with else, else called when there were NOT break called inside for
source_array_2 = []
for element in source_array_2:
    print('current element' + str(element))
    break
else:
    print('source_array_2 is empty')
print('-------------')

english = ['Monday', 'Thuesday', 'Wednesday']
french = ('Lundi', 'Mardi', 'Mercredi')
print('english-french dictionary ' + str(dict(zip(english, french))))
print('-------------')

for even_number in [even_number * 2 for even_number in range(1, 6)]:
    print('even_number ' + str(even_number))
print('-------------')

for even_number in [even_number for even_number in range(1, 11) if even_number % 2 == 0]:
    print('even_number ' + str(even_number))
print('-------------')

rows = range(1, 10)
cols = range(1, 10)
for cell in [(row, col) for row in rows if row < 4 for col in cols if col < 3]:
    print('current cell ' + str(cell))
print('-------------')

# new dict with {key_expression: value_expression for expression in iterable}
sentence = 'I never seen before a wild bear'
letters_dict = {letter: sentence.count(letter) for letter in set(sentence) if letter}
print('letters_dict ' + str(letters_dict))
print('sentence set ' + str(set(sentence)))