from fleet import Fleet
from herd import Herd


class Battlefield:
    def __init__(self):
        self.fleet = Fleet().robots
        self.herd = Herd().dinosaurs

    def run_game(self):
        run = input("Would you like to run the game? ")
        if run == 'yes':
            return True
        elif run == 'no':
            return False
        else:
            run = input("please enter yes or no only: ")

    def display_welcome(self):
        print('Welcome to Dino Vs Robots')
        print('Your challengers Are')
        i = 0
        string_fleet = ''
        while i < len(self.fleet):
            string_fleet += f' {self.fleet[i].name} '
            i = i + 1
        print(string_fleet)
        print('VS')
        j = 0
        string_herd = ''
        while j < len(self.fleet):
            string_herd += f' {self.herd[j].type} '
            j = j + 1
        print(string_herd)

    def battle(self):
        print('Who would you like to battle as?')
        print('Press 1 for Robot and 2 for Dino')
        choice = int(input('Enter #:'))
        if choice == 1:
            print('Please select from the following:')
            i = 0
            while i < len(self.fleet):
                print(f'{i}. ' + self.fleet[i].name)
                i = i + 1
            select_dino = int(input('Enter #'))
            self.dino_turn(select_dino)
        elif choice == 2:
            print('Please select from the following:')
            i = 0
            while i < len(self.herd):
                print(self.herd[i].type)
                i = i + 1
            select_robot = int(input('Enter #'))
            self.robo_turn(select_robot)
        else:
            choice = int(input("Please enter 1 or 2"))

    def dino_turn(self, dinosaur):
        pass

    def robo_turn(self, robot):
        pass

    def show_dino_opponent_options(self):
        pass

    def show_robo_opponent_options(self):
        pass

    def display_winners(self):
        pass