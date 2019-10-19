# filename = 'guest.txt'

# with open(filename, 'w') as file_object:
#     name = input("Enter your name:")
#     file_object.write(name)

filename = 'guest_book.txt'

with open(filename, 'a') as file_object:
    while True:
        prompt = "Enter you name,Please: \n"
        prompt += "(enter 'q' to quit)"
        name = input(prompt)
        if name == 'q':
            break
        else:
            print("Hello! " + name.title())
            name += " is come.\n"
            file_object.write(name)

        
        