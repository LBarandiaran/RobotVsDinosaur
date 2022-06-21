from dinosaur import Dinosaur
from robot import Robot



class Battlefield:
    def __init__(self):
        self.robot = Robot("Mr.Roboto", 50, "Flamethrower")
        self.dinosaur = Dinosaur("Rex", 50, 25)

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print("")
        print(f"Welcome to Robot VS Dinosaur!  Mr.Roboto is battling Rex in a battle for the ages!!!")

        

    def battle_phase(self):
        if robot.health >= 1:
            print(f"Mr. Roboto attacked Rex and caused 25 damage")


        

    def display_winner(self):
        pass

