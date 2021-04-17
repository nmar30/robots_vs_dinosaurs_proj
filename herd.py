from dinosaur import Dinosaur


class Herd:
    def __init__(self):
        self.dinosaurs = self.create_herd()

    def create_herd(self):
        dinosaur1 = Dinosaur('Tyrannosaurus Rex', 100)
        dinosaur2 = Dinosaur('Triceratops', 50)
        dinosaur3 = Dinosaur('Velociraptor', 25)
        temp_list = [dinosaur1, dinosaur2, dinosaur3]
        return temp_list