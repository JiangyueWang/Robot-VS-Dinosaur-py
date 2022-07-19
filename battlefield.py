from robot import Robot
from dinosaur import Dinosaur


class Battlefield:

    def __init__(self):
        self.robot = Robot("Robot 1")
        self.dinosaur = Dinosaur("T-rex", 20)

    def run_game(self):
        pass

    def display_welcome(self):
        print(f'Welcome to an epic battle for the ages!\nOnly one side can win!')

    def battle_phase(self):
        pass

    def display_winner(self):
        pass
