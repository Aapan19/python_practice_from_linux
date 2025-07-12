class Monster:

    #attribute
    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    #methods
    def attack(self, amount):
        print('The monster has attacked!')
        print(f'{amount} damage was dealt')
        self.energy -= amount
        print(f'remaining energy is {self.energy}')

    def move(self, speed):
        print('The monster has moved!')
        print(f'It has a speed of {speed} ms-1')

monster = Monster(100, 50)
monster.attack(20)
monster.move(30)