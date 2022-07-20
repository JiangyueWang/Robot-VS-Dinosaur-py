from operator import le


class Weapon:

    # def __init__(self, name, attack_power):
    #     self.name = name
    #     self.attack_power = attack_power

    def __init__(self):
        self.name = ['weapon_1', 'weapon_2', 'weapon_3']
        self.attack_power = [10, 35, 21]
        self.user_selected_weapon_name = ""
        self.user_selected_weapon_attack_power = 0
        self.select_weapon()

    def select_weapon(self):
        for i in range(1, len(self.name)+1):
            print(f'choose {i} for weapon {self.name[i-1]}')
        self.user_selected_weapon = int(input('enter here: '))
        
        for i in range(1, len(self.name)):
            if self.user_selected_weapon == i:
                self.user_selected_weapon_name = self.name[i-1]
                self.user_selected_weapon_attack_power = self.attack_power[i-1]
    