class User:
    def __int__(self, name, email, password):
        self.name = name

        self.email = email
        self.password = password

    def register(self):
        print("I can register")

    def login(self):
        print("I can login")
        
class Admin(User):
    def __init__(self, name, email, password):
        super().__int__(name, email, password)
        
    def suspend(self):
        print("I can suspend a user")
        
