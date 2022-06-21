from dinosaur import Dinosaur
from weapon import Weapon


class Robot:
    def __init__(self, name, health, active_weapon):
        self.name = name
        self.health = health
        self.active_weapon = active_weapon


    def attack(self, dinosaur):
        dinosaur.health -= self.weapon.attack_power
        print(f"{dinosaur.name} was attacked and now has {dinosaur.health} health remaining")
        
       
