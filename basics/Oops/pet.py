class Animal():
    def __init__(self):
        self.is_alive = True
        self.can_breath= True
   
    

class Mammals(Animal):
    def __init__(self):
        super().__init__()
        
    def make_sound(self):
        return "Some generic mammal sound"

class Birds(Animal):
    def __init__(self):
        super().__init__()
        
    def make_sound(self):
        return "chirp chirp"


class Fishes(Animal):
    def __init__(self):
        super().__init__()
        
    def make_sound(self):
        return "blub blub"

def main():
    generic_mammal = Mammals()
    print(generic_mammal.make_sound())
    
main()