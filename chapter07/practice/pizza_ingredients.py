prompt = "\nPlease enter the name of a ingredient you have want:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    ingredient = input(prompt)
    if ingredient == 'quit':
        break
    
    print("Already add " + ingredient + "!")