def show_magician_name(magician_names):
    for magician_name in magician_names:
        print(magician_name)

def make_great(magician_names):
    greats = []
    while magician_names:
        great = magician_names.pop() + ' the Great'
        greats.append(great)

    while greats:
        magician_names.append(greats.pop())

magician_names = ['Jack', 'Pan']
magician_names_copy = magician_names[:]
make_great(magician_names_copy)
show_magician_name(magician_names)
show_magician_name(magician_names_copy)