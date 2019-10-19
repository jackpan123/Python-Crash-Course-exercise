favorite_numbers = {
    'sadiash': [6, 11, 43],
    'jack': [11, 9],
    'sam': [7],
    'john': [18, 17],
    'james': [23, 24],
}

# print("Sadiash favorite number is " + str(favorite_numbers['sadiash']) + ".")
# print("Jack favorite number is " + str(favorite_numbers['jack']) + ".")
# print("Sam favorite number is " + str(favorite_numbers['sam']) + ".")
# print("John favorite number is " + str(favorite_numbers['john']) + ".")
# print("James favorite number is " + str(favorite_numbers['james']) + ".")

for name, numbers in favorite_numbers.items():
    if len(numbers) == 1:
        print("\n" + name.title() + "'s favorite number is " + str(numbers[0]))
    else:
        print("\n" + name.title() + "'s favorite numbers are:")
        for number in numbers:
            print("\t" + str(number))