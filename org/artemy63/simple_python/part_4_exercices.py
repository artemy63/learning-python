# coding=utf-8
print([3, 2, 1, 0])
print('---')
print(list(range(3, -1, -1)))
print('-----')

# создать список, который содержит нечетные числа в диапазоне range(10).
print([number for number in range(10) if number % 2 == 1])
print('-----')

# создать словарь используя вызов range(10), чтобы получить ключи, и возведите их в квадрат, чтобы получить их значения.
print({key: key * key for key in range(10) if key % 2 == 1})
print('-----')

print({key for key in range(12) if key % 2 == 0})
print('-----')


def gen_ex(start=0, end=10, step=1):
    while start < end:
        current_element = 'Got ' + str(start)
        yield current_element
        start += step


for gen_elem in gen_ex(0, 12):
    print('generator gives me ', gen_elem)
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

movies = [item for item in zip(titles, plots)]
print(movies)
print('-----')

movies = {key: item for key, item in zip(titles, plots)}
print(movies)
