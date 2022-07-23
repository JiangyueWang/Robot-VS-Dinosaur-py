from weapon import Weapon


class Robot:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.active_weapon = ""

    def attack(self, dinosaur):
        if dinosaur.health > 0:
            dinosaur.health = dinosaur.health - \
                self.active_weapon.user_selected_weapon_attack_power
            print(f'\n{self.name} attacked {dinosaur.name} with a Power Loader for {self.active_weapon.user_selected_weapon_attack_power}')
        else:
            return None

    def select_weapon(self):
        self.active_weapon = Weapon()
