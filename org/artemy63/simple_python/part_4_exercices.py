# coding=utf-8
number_list_1 = [3, 2, 1, 0]
print(number_list_1)
print('---')

number_list_2 = list(range(3, -1, -1))
print(number_list_2)
print('-----')

# создать список, который содержит нечетные числа в диапазоне range(10).
even_numbers = [number for number in range(10) if number % 2 == 1]
print(even_numbers)
print('-----')

# создать словарь используя вызов range(10), чтобы получить ключи, и возведите их в квадрат, чтобы получить их значения.
dict_ex = {key: key*key for key in range(12) if key % 2 == 1}
print(dict_ex)
print('-----')

set_ex = {key for key in range(12) if key % 2 == 0}
print(set_ex)
print('-----')


def gen_ex(start=0, end=10, step=1):
    while start < end:
        current_element = 'Got ' + str(start)
        yield current_element
        start += step


gen_ex_list = list(gen_ex(0, 12))
print(gen_ex_list)
print('-----')


def decorator_ex(func):
    print('start func', func.__name__)

    def inner_func(*args, **kwargs):
        result = func(*args, **kwargs)
        print('result', result)
        return result

    print('end func', func.__name__)
    return inner_func


@decorator_ex
def func_with_decorator_ex(arg1, arg2):
    return arg1 - arg2


res = func_with_decorator_ex(4, 13)
print(res)
print('------')

titles = ['Creature of Habit', 'Crewel Fate']
plots = ['A nun turns into a monster', 'A haunted yarn shop']

kortezh_ex = [item for item in zip(titles, plots)]
print(kortezh_ex)
print('-----')

dict_ex = {key: item for key, item in zip(titles, plots)}
print(dict_ex)
