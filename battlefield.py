import random
from fleet import Fleet
from herd import Herd


class Battlefield:

    def __init__(self):

        self.fleet = Fleet()
        self.herd = Herd()

    def display_welcome(self):
        print(f'Welcome to an epic battle for the ages!\nOnly one side can win!\n')

    def robot_option(self):
        # display the list of robots in fleet
        print('Here is the list of robot your can selected from')
        self.counter = 0
        for robot in self.fleet.robot_fleet:
            print(f'Choose {self.counter} to select {robot.name}')
            self.counter += 1

    def select_robot(self):
        # user selects robot from the fleet
        print("\n----Selecting Robot----")
        self.user_selected_robot_count += 1
        self.user_selected_num = int(input("Make selection for robot: "))
        self.user_selected_robot = self.fleet.robot_fleet[self.user_selected_num]
        # user selects weapon for the selected robot
        self.user_selected_robot.select_weapon()
        # user selected weapon info
        # weapon name: self.user_selected_robot.active_weapon.user_selected_weapon_name
        # weapon attack power: self.user_selected_robot.active_weapon.user_selected_weapon_attack_power
        print(
            f'\nRobot: {self.user_selected_robot.name}\nHealth:{self.user_selected_robot.health}\nWeapon: {self.user_selected_robot.active_weapon.user_selected_weapon_name}\nAttack power: {self.user_selected_robot.active_weapon.user_selected_weapon_attack_power}')

    def generate_dino(self):
        self.rand_generated_dino_count += 1
        print('\n----Generating Dinosaour----')
        self.rand_generate_dino_index = random.randint(
            0, len(self.herd.dino_herd)-1)
        self.rand_generate_dino = self.herd.dino_herd[self.rand_generate_dino_index]
        print(
            f'\nDinosaur: {self.rand_generate_dino.name}\nHealth:{self.rand_generate_dino.health}\nAttack Power:{self.rand_generate_dino.attack_power}')

    def run_game(self):
        self.display_welcome()
        # display list of robot
        self.robot_option()
        # user selects a robot and weapon for the selected robot
        self.select_robot()
        # randomly generated dinosaour
        self.generate_dino()
        self.battle_phase()
        self.display_winner()

    def battle_phase(self):

        print("\n----Battle Starts----\n")

        while True:

            while True:
                # robot attacks
                self.user_selected_robot.attack(self.rand_generate_dino)
                # display dinasour health
                print(
                    f'{self.rand_generate_dino.name} with {self.rand_generate_dino.health} remaining!')
                if self.rand_generate_dino.health <= 0:
                    break
                
                # dinasour attacks
                self.rand_generate_dino.attack(self.user_selected_robot)
                # display robot health
                print(
                    f'{self.user_selected_robot.name} with {self.user_selected_robot.health} remaining!')
                if self.user_selected_robot.health <= 0:
                    break

            if self.user_selected_robot.health <= 0:
                # remove robot from the fleet
                self.fleet.robot_fleet.remove(self.user_selected_robot)
                # if no robots in the fleet break the loop
                if len(self.fleet.robot_fleet) == 0:
                    break
                else:
                    # display list of robot
                    self.robot_option()
                    # user selects a robot and weapon for the selected robot
                    self.select_robot()

            if self.rand_generate_dino.health <= 0:
                # remove dino from the herd
                self.herd.dino_herd.remove(self.rand_generate_dino)
                # if no dinos in the herd break the loop
                if len(self.herd.dino_herd) == 0:
                    break
                else:
                    # re-generate dino
                    self.generate_dino()

    def display_winner(self):
        if len(self.fleet.robot_fleet) == 0:
            print(
                f'\nThere are {len(self.fleet.robot_fleet)} robots in the Fleet')
            print(f'Dino Herd wins')
        else:
            print(f'\nThere are {len(self.herd.dino_herd)} dinos in the Herd')
            print(f'Robot Fleet wins')

        # def battle_phase(self):


        #     self.is_game_on = True
        #     while self.is_game_on:
        #         # robot attacks
        #         # show robot attack power and dinosaur remain health
        #         # print(f'{self.robot.name} attacked {self.dinosaur.name} with a Power Loader for {self.robot.active_weapon.user_selected_weapon_attack_power}')
        #         self.dinosaur.health = self.dinosaur.health - \
        #             self.robot.active_weapon.user_selected_weapon_attack_power
        #         print(f'{self.dinosaur.name} has {self.dinosaur.health} helath remaining')
        #         print(f'\n')
        #         # dinosaur attacks
        #         # show dinosaur attack power and robot remain health
        #         print(
        #             f'{self.dinosaur.name} attacked {self.robot.name} with a Power Loader for {self.dinosaur.attack_power}')
        #         self.robot.health = self.robot.health - self.dinosaur.attack_power
        #         print(f'{self.robot.name} has {self.robot.health} health remaining')
        #         print(f'\n')

        #         # if robot and dinosaur health is not zero battle continues
        #         if self.robot.health <= 0 or self.dinosaur.health <= 0:
        #             self.is_game_on = False
        #         else:
        #             self.is_game_on = True


