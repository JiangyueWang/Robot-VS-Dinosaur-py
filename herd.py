from dinosaur import Dinosaur


class Herd:

    def __init__(self):
        self.herd = []
        self.creat_herd()

    def add_dino(self, dino):
        self.herd.append(dino)

    def creat_herd(self):
        self.add_dino(Dinosaur("T-rex", 50, 150))
        self.add_dino(Dinosaur("Velociraptor", 30, 130))
        self.add_dino(Dinosaur("Ankylosaurus", 20, 120))

    def display_dino(self):
        for dino in self.herd:
            print(
                f'Dinosaur: {dino.name}\nHealth:{dino.health}\nAttack Power:{dino.attack_power}\n')


herd_one = Herd()
herd_one.display_dino()
