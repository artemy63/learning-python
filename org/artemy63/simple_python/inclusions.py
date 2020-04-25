list_numbers = [number1*number2 for number1 in range(0, 10) if number1 < 5 for number2 in range(1, 10) if number2 < 6]
print(str(list_numbers))

dict_numbers = {key : key*3 + 14 for key in range(0, 10)}
print(dict_numbers)

number_list = [number for number in range(0, 8)]
print(number_list)

number_list_2 = [number*2 for number in range(0, 8)]
print(number_list_2)

number_list_3 = [number*3 for number in range(0, 100) if number < 8]
print(number_list_3)


rows = range(1, 3)
cols = range(1, 4)
cells = [[row, col] for row in rows for col in cols]
for cell in cells:
    print(cell)