from datetime import datetime


def get_time_in_seconds():
    """
    This is doc for function get_time_in_seconds
    :return: time in milliseconds from till
    """

    return datetime.now().timestamp()


print('get_time_in_seconds()', get_time_in_seconds())
print('get_time_in_seconds.__name__', get_time_in_seconds.__name__)
print('get_time_in_seconds.__doc__', get_time_in_seconds.__doc__)
print('------')


# позиционные аргументы
def split_tags(input_str):
    tag_set = set()
    for cur_tag in input_str.split(', '):
        tag_set.add(cur_tag)

    return tag_set


input_str = 'python, java, go'
print('calling {} with params {}'.format(split_tags.__name__, input_str))
print(split_tags(input_str))
print('------')


# именованные аргументы
def greeting(greeting, name):
    return '{}, {}!'.format(greeting, name)


print(greeting('Hello', 'world'))
print(greeting(greeting='Hi', name='Tomofey'))
print('------')


# аргументы по умолчанию
def default_greeting(greeting='Hello', name='it\'s me...'):
    return '{}, {}!'.format(greeting, name)


print('default_greeting()', default_greeting())
print('default_greeting("Hi")', default_greeting(greeting='Hi'))
print('------')


# *args
def printer(*args):
    print(type(args))
    print(args)
    for arg in args:
        print('current argument =', arg)


letter_list = ['a', 'b', 'c']
printer(letter_list)
printer(*letter_list)
printer(1, 2, 3, 4, 5)
print('------')


# **kwargs
def printer_2(**kwargs):
    print(type(kwargs))
    print(kwargs)
    for key, item in kwargs.items():
        print('printer_2 {} with value {}'.format(key, item))


printer_2(a=12, b=-3)
payload = {
    'user': 101,
    'maney': 10200,
    'feedback': {
        'first': 'yes',
        'second': 'no'
    }
}
printer_2(payload=payload)
# printer_2(payload)
printer_2(**payload)


def printer_3(*args, **kwargs):
    print(type(kwargs))
    print(args, kwargs)
    for key, item in kwargs.items():
        print('printer_3 {} with value {}'.format(key, item))

print('-------')
printer_3(payload)
printer_3(**payload)
printer_3(payload, **payload)