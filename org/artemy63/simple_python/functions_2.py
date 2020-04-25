
# Функции в Python являются объектами первого класса.
# Вы можете присвоить их переменным, использовать как аргументы для других функций и возвращать из функций


def hard42():
    """just returns 42 in any case"""
    return '42'


def echo(func):
    print(func())


# TypeError: 'list' object is not callable
# hard42 = ['100500']


echo(hard42)
help(hard42)


def multiply(arg1, arg2):
    print(arg1*arg2)


def sum(arg1, arg2):
    print(arg1 + arg2)


def do_call_func(func, arg1, arg2):
    func(arg1, arg2)


do_call_func(sum, 3, 4)
do_call_func(multiply, 3, 4)


# inner functions
def outer(saying):
    def inner(quote):
        return "We are knights who say '%s'" % quote

    print(inner(saying))


outer("Ну нихуя ж себе")


def func_closure(saying):
    def inner_closure():
        return "We are knights who say '%s'" % saying
    return inner_closure


a = func_closure("Ёпта")
b = func_closure("Блеать")
print(type(a))
print(a())
print(a == b)
print(b())
