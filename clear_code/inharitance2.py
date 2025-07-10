
class Monster:

    def __init__(self, health, energy):
        self.health = health
        self.energy = energy

    def attack(self, amount):
        print('The monster has attacked!')
        print(f'{amount} dsmsge was dealt')
        self.energy -= amount

    def move(self, speed):
        print('The monster has moved')
        print(f'It has a speed of {speed}')

class Shark(Monster):
    def __init__(self, speed):
        
        self.speed = speed

    def bite(self):
        print('The shark has betten')

    def move(self):
        print('Shark has moved')
        print(f'Speed of the shark is {self.speed}')

shark = Shark(120)
print(shark.health)
shark.move()