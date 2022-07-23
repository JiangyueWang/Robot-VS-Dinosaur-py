import random
from fleet import Fleet
from herd import Herd


class Battlefield:

    def __init__(self):

        self.fleet = Fleet()
        self.user_selected_robot_count = 0
        # self.user_selected_robot = ""
        self.herd = Herd()
        self.rand_generated_dino_count = 0
        # self.generated_dino = ""
        self.game_on = True
        self.health_above_zero = True

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
        #     print("***Robot turn***")
        #     # display dino options, so user can pick the one that gets attacked
        #     # call dinosaur_options here
        #     user_dinosaur_choice= int(input("Make selection"))
        #     self.fleet.robot_fleet[user_robot_choice].attack(self.herd.dinosaur_herd.user_dinosaur_choice)
        #     # afer attack check the dino health, if 0 or lower then remove from herd list

    def run_game(self):
        self.display_welcome()
        # display list of robot
        self.robot_option()
        # user selects a robot and weapon for the selected robot
        self.select_robot()
        # randomly generated dinosaour
        self.generate_dino()
        self.battle_phase()
        # self.display_winner()

    def is_game_on(self):

        if self.rand_generated_dino_count > 2:
            return False
        elif self.user_selected_robot_count > 2:
            return False
        else:
            return True

    def check_health(self):
        if self.user_selected_robot.health <= 0:
            return False
        elif self.rand_generate_dino.health <= 0:
            return False
        else:
            return True

    def battle_phase(self):

        print("\n----Battle Starts----\n")

        while self.game_on:
            self.game_on = self.is_game_on()
            self.health_above_zero = self.check_health()
            while self.health_above_zero:
                # robot attacks
                self.user_selected_robot.attack(self.rand_generate_dino)
                self.health_above_zero = self.check_health()
                # display dinasour health
                print(
                    f'{self.rand_generate_dino.name} with {self.rand_generate_dino.health} remaining!')
                if self.health_above_zero == False:
                    break
                # dinasour attacks
                self.rand_generate_dino.attack(self.user_selected_robot)
                self.health_above_zero = self.check_health()

                # display robot health
                print(
                    f'{self.user_selected_robot.name} with {self.user_selected_robot.health} remaining!')
                if self.health_above_zero == False:
                    break
            if self.user_selected_robot.health <= 0:
                # remove robot from the fleet
                self.fleet.robot_fleet.remove(self.user_selected_robot)
                self.game_on = self.is_game_on()
                # display list of robot
                self.robot_option()
                # user selects a robot and weapon for the selected robot
                self.select_robot()
            if self.rand_generate_dino.health <= 0:
                # remove dino from the herd
                self.herd.dino_herd.remove(self.rand_generate_dino)
                self.game_on = self.is_game_on()
                # re-generate dino
                self.generate_dino()

        print("Game OVER!")
        # def battle_phase(self):

        #     # while len(self.fleet.robot_fleet) > 0 and len(self.herd.dinosaur_herd) > 0:
        #     # call robot turn
        #     # dino turn "if" herd list is greater than 0
        #     # call dino turn

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

        # def dinosaur_turn(self):
        #     pass

        # def robot_options(self):
        #     counter = 0
        #     for robot in self.fleet.robot_fleet:
        #         print(f'Press {counter} to select {robot.name}')
        #         counter += 1

        # def dinosaur_options(self):
        #     pass

    def display_winner(self):
        if self.robot.health <= 0:
            print(f'{self.dinosaur.name} wins')
        else:
            print(f'{self.robot.name} wins')
