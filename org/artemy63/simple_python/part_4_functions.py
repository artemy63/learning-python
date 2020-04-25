# function can take ANY number of input parameters and produce ANY number of result


def do_nothing():
    pass


def echo(anything):
    return anything + ' ' + anything


print(echo("Rumplestiltskin"))
print(echo('2'))
print('-------------')


def menu(wine, dessert, entree):
    return {'wine': wine, 'dessert': dessert, 'entree': entree}


# positional arguments
print(menu('beer', 'cookies', 'beef'))
# arguments with key words, if both, positional and key-words presented, positional must be specified first
print(menu('beer', entree='cookies', dessert='beef'))
print(menu(entree='beer', wine='cookies', dessert='beef'))
print('-------------')


# NOTE::: do not use mutable type for value by default
def menu_with_default_arg(wine, dessert, entree='chicken'):
    return {'wine': wine, 'dessert': dessert, 'entree': entree}


print(menu_with_default_arg('bordeux', 'pudding', 'beef'))
print(menu_with_default_arg('bordeux', 'pudding'))
print(menu_with_default_arg(dessert='bordeux', wine='pudding'))
print('-------------')


# to get all positional arguments in function it is necessary to use *args
def _func_with_grab_positional_arguments(req_param, another_req_param, *all_other_positional_params):
    print('req_param', req_param, 'and another_req_param', another_req_param)
    print('all other stuff', all_other_positional_params)
    print(all_other_positional_params[0])
    print(all_other_positional_params[1])
    pass


print(_func_with_grab_positional_arguments('req?', 'another_req?', 'pos_arg_1', ['pos_arg_2'], ('pos_arg_3',)))
print('-------------')


def _func_with_grab_positional_and_kwargs_arguments(req_param, *args, **kwargs):
    print('req_param', req_param)
    print('*args', args)
    print('**kwargs', kwargs)
    pass


print(_func_with_grab_positional_and_kwargs_arguments('it is required argument', 'another_req?', 'stuff',
                                                      kw_arg_1=['stuff'], kw_arg_2=('stuff',)))
print('-------------')


# function is object
def run_function(func, *args, **kwargs):
    return func(*args, **kwargs)


print('function is object')
run_function(_func_with_grab_positional_and_kwargs_arguments,
             'required_argument', 'unused positional arg', unused_kw='unused kw arg')
print('-------------')


# inner functions
def outer(saying):
    def inner(quote):
        return "We are knights who say '%s'" % quote

    print(inner(saying))


outer("What the hell is going on???")
print('-------------')


def func_closure(saying):
    def inner_closure():
        return "We are knights who say '%s'" % saying
    return inner_closure
# closure - dynamically created function which knows from where it created, it keeps value of passed argument


a = func_closure("May the force be with you!")
b = func_closure("blah-blah-blah")
print(type(a))
print(a())
print(a == b)
print(b())
print('-------------')


def edit_story(words, func):
    for word in words:
        print(func(word))


def edit_story_func(word):
    return word.capitalize() + '!'


edit_story(['thud', 'meow', 'thud', 'hiss'], edit_story_func)
print('the same with lambda')
edit_story(['thud', 'meow', 'thud', 'hiss'], lambda word: word.capitalize() + '!')
print('-------------')


# decorator
def document_it(func):
    def inner_func(*args, **kwargs):
        print('Running function ', func.__name__)
        print('Positional arguments ', args)
        print('Keyword arguments ', kwargs)
        result = func(*args, **kwargs)
        print('Result ', result)
        return result
    return inner_func


@document_it
def document_me(a, b):
    return a + b


document_me(3, b=42)
print('-------------')


# if there are some decorators first will be applied nearest to function and step by step above
def sum_decorator(func):
    def inner_func(*args, **kwargs):
        result = func(*args, **kwargs)
        return result + 42
    return inner_func


def multiply_decorator(func):
    def inner_func(*args, **kwargs):
        result = func(*args, **kwargs)
        return result * 42
    return inner_func


@multiply_decorator
@sum_decorator
def decore_me_sum_multiply(a, b):
    return a + b


@sum_decorator
@multiply_decorator
def decore_me_multiply_sum(a, b):
    return a + b


print('decore_me_sum_multiply ', decore_me_sum_multiply(3, 4))
print('decore_me_multiply_sum ', decore_me_multiply_sum(3, 4))