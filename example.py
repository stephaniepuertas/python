a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
values = a_dict.values()
# values
# dict_values(['blue', 'apple', 'dog'])
for value in a_dict.values():
    print(value)


a_dict = {'color': 'blue', 'fruit': 'apple', 'pet': 'dog'}
keys = a_dict.keys()
# for key in a_dict.keys():
#     print(key)
for key in a_dict.keys():
    print(key, '->', a_dict[key])