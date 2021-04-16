from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs = self.create_herd()

    def create_herd(self):
        dinosaur1 = Dinosaur('Tyrannosaurus Rex', 10)
        dinosaur2 = Dinosaur('Triceratops', 10)
        dinosaur3 = Dinosaur('Velociraptor', 10)
        temp_list = [dinosaur1, dinosaur2, dinosaur3]
        return temp_list