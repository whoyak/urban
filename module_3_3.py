def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params(b = 25)
print_params(c=[1,2,3])
value_list = [1, 'Слово', False]
value_dict = {'a': 25, 'b':'Hello', 'c': True}
print_params(*value_list)
print_params(**value_dict)
value_list_2 = [25,'Word']
print_params(*value_list_2,42)
