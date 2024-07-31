def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params()
print_params(b=25)
print_params( a='sdf', c=[192, 3, 18])
values_list = [2, 5.7, 'hello']
values_dict = {'a': 23, 'b': False, 'c': (3, 4, 5.6)}
print_params(*values_list)
print_params(**values_dict)
values_list_2 = [2, 'hi']
print_params(*values_list_2, 42)