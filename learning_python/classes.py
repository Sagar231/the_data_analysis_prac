'''
OOPs 

'''

class MyFirstClass():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def greet(self):
        return f'hey {self.name} your age is {self.age}, thats amazing'

first = MyFirstClass("ananya",23)  #class instance
second = MyFirstClass("Sagar",23)  
print(first.greet())
print(second.greet())



class Warrior():
    def __init__(self,name):
        self.name = name
        self.attack = 100
        self.iq = 50
        self.defence = 60
        self.healing = 0
    
    def kamenameha(self):
        return f'The monster got attacked by power of {self.attack}'
    

class Mage():
    def __init__(self,name):
        self.name = name
        self.attack = 60
        self.iq = 90
        self.defence = 50
        self.healing = 20
        
    def abracadabra(self):
        return f'Monster got freeze by magic'
    
    
    
class Tank():
    def __init__(self,name):
        self.name = name
        self.attack = 80
        self.iq = 30
        self.defence = 100
        self.healing = 0
        
    def armorup(self):
        return f'Defending the team with the power of {self.defence}'

class Healer():
    def __init__(self,name):
        self.name = name
        self.attack = 40
        self.iq = 80
        self.defence = 20
        self.healing = 100
        
    def sanjeevni(self):
        return f"Healed a teammate by {self.healing}"
        
        
Ananya = Mage("Storm_terror")
Sagar = Warrior("Goku")
print(Ananya.abracadabra())
print(Sagar.kamenameha())
        