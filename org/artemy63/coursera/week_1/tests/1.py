#найти сумму цифр, из которых состоит строка.

import sys

str_with_numbers = sys.argv[1]
print('It is necessary to find sum of numbers in str =', str_with_numbers)

sum = 0
for digit in str_with_numbers:
    print('current digit is', digit)
    sum += int(digit)

print('result is', sum)