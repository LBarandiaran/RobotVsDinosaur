class Dinosaur:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, robot):
        robot.health -= self.attack_power
        print(f"{Dinosaur.name} attacked {Robot.name} and caused {self.attack_power} damage!!!")

    

