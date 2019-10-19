from collections import OrderedDict

directory = OrderedDict()
directory['me'] = 'mean I'
directory['update'] = 'refresh something'
directory['try'] = 'want to do something'
directory['available'] = 'can use to do something'
directory['phone'] = 'can contact someone'
# directory = {
#     'list': 'storage lots of elements',
#     'variable': 'a element',
#     'tuple': 'can not change',
#     'dictionary': 'a key-value list',
#     'del': 'delete some one',
# }

# print("list: " + directory['list'])
# print("variable: " + directory['variable'])
# print("tuple: " + directory['tuple'])
# print("dictionary: " + directory['dictionary'])
# print("del: " + directory['del'])

for word,mean in directory.items():
    print(word + ": " + mean)

# directory['me'] = 'mean I'
# directory['update'] = 'refresh something'
# directory['try'] = 'want to do something'
# directory['available'] = 'can use to do something'
# directory['phone'] = 'can contact someone'
# print()
# for word,mean in directory.items():
#     print(word + ": " + mean)