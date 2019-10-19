def make_sandwich(*ingredients):
    """概述三明治材料"""
    print("This sandwich has:")
    for ingredient in ingredients:
        print("- " + ingredient)

make_sandwich('chicken')
make_sandwich('chicken', 'egg')
make_sandwich('chicken', 'egg', 'tomato')
