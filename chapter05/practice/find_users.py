current_users = ['jack', 'sam', 'john', 'pan', 'tom']
new_users = ['Jack', 'Lili', 'Yao', 'Pan', 'Mess']

for new_user in new_users:
    if new_user.lower() in current_users:
        print(new_user + " already be userd, Please use others.")
    else:
        print(new_user + " is valid!")