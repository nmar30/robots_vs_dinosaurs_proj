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
        print('______________________________________')

    def battle(self):
        if
        print('Who would you like to battle as?')
        print('Press 1 for Robot and 2 for Dino')
        choice = int(input('Enter #:'))
        if choice == 1:
            print('Please select from the following:')
            self.show_robo_options()
            selected_robot = int(input('Enter #'))
            self.robo_turn(selected_robot)
        elif choice == 2:
            print('Please select from the following:')
            self.show_dino_options()
            selected_dino = int(input('Enter #'))
            self.dino_turn(selected_dino)
        else:
            choice = int(input("Please enter 1 or 2")) ###neeeds loopye

    def dino_turn(self, dinosaur):
        print('Who would you like to battle?')
        self.show_robo_options()
        selected_robot = int(input('Enter #'))
        self.herd[dinosaur].attack(self.fleet[selected_robot])
        print(f'{self.herd[dinosaur].type} attacked {self.fleet[selected_robot].name}')


    def robo_turn(self, robot):
        print('Who would you like to battle?')
        self.show_dino_options()
        selected_dino = int(input('Enter #'))
        self.fleet[robot].attack(self.herd[selected_dino])
        print(f'{self.fleet[robot].name} attacked {self.herd[selected_dino].type}')

    def show_dino_options(self):
        i = 0
        while i < len(self.herd):
            print(f'{i}. {self.herd[i].type} | Health: {self.herd[i].health}%')
            i = i + 1

    def show_robo_options(self):
        i = 0
        while i < len(self.fleet):
            print(f'{i}. {self.fleet[i].name} | Health: {self.fleet[i].health}%')
            i = i + 1

    def display_winners(self):
        pass