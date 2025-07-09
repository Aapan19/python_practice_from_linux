# Exercise: 
#1. Create a hero class with 2 parameter: damage and monster
#2. The monster class should have a method that lowers the health __> get_damage(amount)
#3. the hero class should have an attack method that calls the get_damage method from the monster class.. the amount of damage is hero.damage

class Monster:

    def __init__(self,health, energy):
        self.health = health
        self.energy = energy

#2. The monster class should have a method that lowers the health __> get_damage(amount)
    def get_damage(self, amount):
        self.health -= amount
        # print(f'Remaining amount of health {self.health}')


#1. Create a hero class with 2 parameter: damage and monster
class Hero:
    def __init__(self, damage, monster):
        self.damage = damage
        self.monster = monster
    
#3. the hero class should have an attack method that calls the get_damage method from the monster class.. the amount of damage is hero.damage
    def attack(self):
        self.monster.get_damage(self.damage)

monster = Monster(100, 50)


hero = Hero(damage=15, monster=monster)

print(monster.health)
hero.attack()
print(monster.health)
