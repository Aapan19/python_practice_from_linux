# private Attribute 
# hasattr and setattr
# doc

class Monster:
    '''A Monster that has some attribute''' # to see in __doc__
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

        # private Attribute 
        self._id = 5 # Actually this called protective and private starts with double underscore __id = 4

    def attack(self, amount):
        print('The Monster has attacked')
        print(f'{amount} energy has been dealt')
        self.energy -= amount

    def move(self, speed):
        print('The monster has moved')
        print(f'It has a speed of {speed} ')

monster = Monster(50, 20)

# hasattr and setattr
# hasattr(object, 'attribute')
print(hasattr(monster, 'health'))
setattr(monster, 'weapon', 'sword')
# monster.weapon = sword
print(monster.weapon)

new_attribute = (['weapon', 'Axe'], ['armor', 'shield'], ['potion', 'mana'])
for attr,value in new_attribute:
    setattr(monster, attr, value)
print(vars(monster))

# Doc
# print(monster.__doc__)

help(monster)