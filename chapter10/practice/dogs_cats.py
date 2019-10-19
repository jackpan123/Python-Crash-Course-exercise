filenames = ['cats.txt', 'dogs.txt']
for filename in filenames:
    try:
        with open(filename) as cat_object:
            contents = cat_object.read()
    except FileNotFoundError:
        pass
        # print("The file " + filename + " does not exist.")
    else:
        print(contents)

