def document_it(func):
    def inner(*args, **kwargs):
        print('function name', func.__name__, 'with positional arguments', args, 'and key words arguments', kwargs)
        result = func(*args, **kwargs)
        print('result of computation', result)
        return result

    return inner


def multiply(arg1, arg2):
    return arg1*arg2


# мануальное присваивание декоратора
res_1 = document_it(multiply)
print(type(res_1))
res_1(10, 13)


@document_it
def divide(arg1, arg2):
    return arg1/arg2


divide(16, 8)


print('------')


def document_it_2(func):
    def inner(*args, **kwargs):
        print('document_it_2 start work with positional arguments', args, 'and key words arguments', kwargs)
        result = func(*args, **kwargs)
        return result*result

    return inner


# Каждая функция может иметь более одного декоратора
# Декоратор, размещенный ближе всего к функции (прямо над def), будет выполнен первым
# а затем — тот, что находится сразу над ним.
@document_it_2
@document_it
def divide_in_int(arg1, arg2):
    return arg1//arg2


divide_in_int(16, 3)