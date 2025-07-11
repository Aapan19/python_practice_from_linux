class Monster:

    #attribute
    health = 100
    energy = 50

    #methods
    def attack(self, amount):
        print('The monster has attacked!')
        print(f'{amount} damage was dealt')
        self.energy -= amount
        print(f'remaining energy is {self.energy}')

    def move(self, speed):
        print('The monster has moved!')
        print(f'It has a speed of {speed} ms-1')

monster = Monster()
monster.attack(20)
monster.move(30)