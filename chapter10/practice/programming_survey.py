filename = 'programming_reason.txt'

with open(filename, 'a') as file_object:
    while True:
        prompt = "Please input your like programming reason: \n"
        prompt += "(when you completed and input 'q' to quit)"
        reason = input(prompt)
        if reason == 'q':
            break
        else:
            reason += "\n"
            file_object.write(reason)