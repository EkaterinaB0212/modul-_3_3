def print_params(a = 1, b = 'строка', c = True):
    print(a, b, c)
print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [2, "stroka", False]
values_dict = {'a': values_list[0], 'b':values_list[1], 'c':values_list[2]}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [3, 'STROKA']
print_params(*values_list_2)
