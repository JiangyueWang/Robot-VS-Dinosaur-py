
from robot import Robot
from dinosaur import Dinosaur


class Battlefield:

    def __init__(self):
        self.robot = Robot("Robot 1")
        self.dinosaur = Dinosaur("T-rex", 50)

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print(f'Welcome to an epic battle for the ages!\nOnly one side can win!\n')

    def battle_phase(self):

        self.is_game_on = True
        while self.is_game_on:
            # robot attacks
            # show robot attack power and dinosaur remain health
            print(f'{self.robot.name} attacked {self.dinosaur.name} with a Power Loader for {self.robot.active_weapon.user_selected_weapon_attack_power}')
            self.dinosaur.health = self.dinosaur.health - \
                self.robot.active_weapon.user_selected_weapon_attack_power
            print(f'{self.dinosaur.name} has {self.dinosaur.health} helath remaining')
            print(f'\n')
            # dinosaur attacks
            # show dinosaur attack power and robot remain health
            print(
                f'{self.dinosaur.name} attacked {self.robot.name} with a Power Loader for {self.dinosaur.attack_power}')
            self.robot.health = self.robot.health - self.dinosaur.attack_power
            print(f'{self.robot.name} has {self.robot.health} health remaining')
            print(f'\n')

            # if robot and dinosaur health is not zero battle starts
            # if robot and dinosaur health is not zero battle starts
            if self.robot.health <= 0 or self.dinosaur.health <= 0:
                self.is_game_on = False
            else:
                self.is_game_on = True

    def display_winner(self):
        if self.robot.health <= 0:
            print(f'{self.dinosaur.name} wins')
        else:
            print(f'{self.robot.name} wins')
