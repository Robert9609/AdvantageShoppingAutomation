import random

class User:
    def __init__(self, username):
        self.username = username
        self.email = User.generate_static_email()     # User email: 234@test.com
        
    def generate_email_for_object(self):
        return f"Credentials: {self.username}.{self.email}"

    @staticmethod
    def generate_static_email():
        return f"{random.randint(100, 999)}@test.com"
    
obj_1 = User("Robert")
print(obj_1.generate_email_for_object())

print(User.generate_static_email())