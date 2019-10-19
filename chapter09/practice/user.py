class User():
    """用户类"""

    def __init__(self, first_name, last_name, location, field):
        self.first_name = first_name
        self.last_name = last_name
        self.location = location
        self.field = field
        self.login_attempts = 0

    
    def decribe_user(self):
        """介绍自己"""
        print("My name is " + self.first_name.title() + " " + self.last_name.title()
            + " and I am live in " + self.location.title() + ", And I learning " + self.location)

    def greet_user(self):
        """个性化问候"""
        print("Hello! " + self.first_name.title() + " " + self.last_name.title())

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0

# jack = User('jack', 'pan', 'fuzhou', 'software')
# jack.decribe_user()
# jack.greet_user()
# jack.increment_login_attempts()
# jack.increment_login_attempts()
# print(jack.login_attempts)
# jack.reset_login_attempts()
# print(jack.login_attempts)

# mess = User('mess', 'pan', 'fuan', 'sale')
# mess.decribe_user()
# mess.greet_user()