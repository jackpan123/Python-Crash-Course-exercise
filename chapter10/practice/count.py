def count_the(filename):
    try:
        with open(filename) as file_object:
            contents = file_object.read()
    except:
        pass
    else:
        number = contents.lower().count('the')
        print(number)

filenames = ['alice.txt', 'siddhartha.txt', 'moby_dick.txt', 'little_women.txt']
for filename in filenames:
    count_the(filename)