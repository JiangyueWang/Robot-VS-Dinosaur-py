from dinosaur import Dinosaur


class Herd:

    def __init__(self):
        self.dino_herd = []
        self.creat_herd()

    def add_dino(self, dino):
        self.dino_herd.append(dino)

    def creat_herd(self):
        self.add_dino(Dinosaur("T-rex", 50, 120))
        self.add_dino(Dinosaur("Velociraptor", 30, 100))
        self.add_dino(Dinosaur("Ankylosaurus", 20, 90))

    def display_dino(self):
        for dino in self.dino_herd:
            print(
                f'Dinosaur: {dino.name}\nHealth:{dino.health}\nAttack Power:{dino.attack_power}\n')


# herd_one = Herd()
# herd_one.display_dino()
