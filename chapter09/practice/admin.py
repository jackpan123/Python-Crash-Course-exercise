from user import User
class Privileges():

    def __init__(self, privileges=['can add post', 'can delete post', 'can ban user']):
        self.privileges = privileges

    def show_privileges(self):
        for privilege in self.privileges:
            print("- " + privilege)

class Admin(User):
    """管理员的简单尝试"""
    def __init__(self, first_name, last_name, location, field):
        super().__init__(first_name, last_name, location, field)
        self.privileges = Privileges()

    
