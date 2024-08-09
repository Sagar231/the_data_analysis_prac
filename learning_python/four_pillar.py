class Player():
    def __init__(self,name):
        self.name = name
    
    def hpincrease(self):
        return " you hp increased by 300"

class Warrior(Player):
    def __init__(self,name):
        super().__init__(name)
        self.attack = 100
    
    def kamenameha(self):
        return f'The monster got attacked by power of {self.attack}'
    
    

class Mage(Player):
    def __init__(self,name):
        super().__init__(name)
        self.attack = 60
        
    def abracadabra(self):
        return f'Monster got freeze by magic'
        
Ananya = Mage("Storm_terror")
Sagar = Warrior("Goku")
print(Ananya.abracadabra())
print(Sagar.kamenameha())
print(Ananya.hpincrease())