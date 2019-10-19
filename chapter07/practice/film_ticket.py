prompt = "\nPlease enter the you age:"
prompt += "\n(Enter 'quit' when you are finished.)"

# while True:
#     age = input(prompt)
#     if age == 'quit':
#         break
#     age = int(age)

#     if age < 3:
#         print("You are free ticket")
#     elif age <= 12:
#         print("You are $10 for a ticket")
#     else:
#         print("You are $15 for a ticket")


# age = ''
# while age != 'quit':
#     age = input(prompt)

#     if age != 'quit':
#         age = int(age)

#         if age < 3:
#             print("You are free ticket")
#         elif age <= 12:
#             print("You are $10 for a ticket")
#         else:
#             print("You are $15 for a ticket")

active = True
while active:
    age = input(prompt)
    if age == 'quit':
        active = False
    else:
        age = int(age)

        if age < 3:
            print("You are free ticket")
        elif age <= 12:
            print("You are $10 for a ticket")
        else:
            print("You are $15 for a ticket")
        