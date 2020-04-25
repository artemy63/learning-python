from builtins import print


def menu(wine, dessert, entree):
    return {'wine': wine,
            'dessert': dessert,
            'entree': entree
            }


print(menu('пивасик', 'печеньки', 'мясо'))
print(menu('пивасик', entree='печеньки', dessert='мясо'))
print(menu(entree='пивасик', wine='печеньки', dessert='мясо'))


def _func_with_def_arg(wine, dessert, entree='chicken'):
    return {'wine': wine, 'dessert': dessert, 'entree': entree}


print(_func_with_def_arg('bordeux', 'pudding', 'beef'))
print(_func_with_def_arg('bordeux', 'pudding'))
print(_func_with_def_arg(dessert='bordeux', wine='pudding'))
#incorrect
# print(_func_with_def_arg('bordeux'))


def _func_with_grab_all_params(req_param, another_req_param, *all_other_params):
    print('req_param', req_param, 'and another_req_param', another_req_param)
    print('all other stuff', all_other_params)
    print(all_other_params[0])
    print(all_other_params[1])
    pass


print(_func_with_grab_all_params('req?', 'another_req?', 'stuff', ['stuff'], ('stuff',)))


def _func_with_grab_all_kwargs_params(req_param, *args, **kwargs):
    print('req_param', req_param)
    print('*args', args)
    print('**kwargs', kwargs)
    pass


print(_func_with_grab_all_kwargs_params('req?', 'another_req?', 'stuff', hueta_huet=['stuff'], epanrot=('stuff',)))

animal = "петух"
print('animal', animal)
def change_and_print_global_var():
    global animal
    animal = " петушок"
change_and_print_global_var()
print('animal changed', animal)
print('------')
print('globals()', globals())


