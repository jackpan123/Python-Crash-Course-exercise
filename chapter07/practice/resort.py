responses = {}

active = True

while active:
    name = input("\nWhat is your name? ")
    response = input("\nIf you could visit one place in the world, where would you go? ")
    responses[name] = response
    repeat = input("Have others people accept this poll?(yes/no) ")
    if repeat == 'no':
        active = False

print("\n--- Poll Result ---")
for name, response in responses.items():
    print(name + " would want to go place is " + response)