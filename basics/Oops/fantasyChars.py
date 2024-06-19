class User():
    def __init__(self,email):
        self.email = email
    def sign_in(self):
        print("Logged in")
        
class Human(User):
    def __init__(self, name,power,email):
        super().__init__(email)
        self.name = name
        self.power = power
    
    def attack(self):
        print(f'attacking with power of {self.power}')
        
class Wizard(User):
    def __init__(self,name,power,email):
        super().__init__(email)
        self.name = name
        self.power = power
    
    def attack(self):
        print(f'attacking with power of {self.power}')

human1 = Human('Escanor',120,'esca@gmai.com')
wiz1 = Wizard('Magi',110,'magi@gmai.com')

print(human1.attack())