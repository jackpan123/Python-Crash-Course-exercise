print("A sample addition machine.\n")
print("Enter 'q' to quit")

while True:
    first_number = input("First number: ")
    if first_number == 'q':
        break
    second_number = input("Second number: ")
    if second_number == 'q':
        break
    
    try:
        sum = int(first_number) + int(second_number)
    except ValueError:
        print("You must input numeric!")
    else:
        print(sum)