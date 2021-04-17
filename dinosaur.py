class Dinosaur:
    def __init__(self, type, attack_power):
        self.type = type
        self.health = 100
#        self.energy = 0
        self.attack_power = attack_power

    def attack(self, robot):
        robot.health = robot.health - self.attack_power